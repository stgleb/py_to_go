import ctypes
import os

TIME_CB = ctypes.CFUNCTYPE(None)


def get_listen_param(count):
    if count < 15:
        return int(count // 5)
    if count < 100:
        return max(count // 10, 3)
    return max(count // 20, 10)


def add_c(a, b):
    binary = ctypes.cdll.LoadLibrary("bin/main.c.so")
    func = getattr(binary, "sum")
    func.restype = ctypes.c_int

    func.argtypes = [
        ctypes.c_int,
        ctypes.c_int,
    ]

    return func(a, b)


def add_c_with_callback(a, b):
    def add(x, y):
        return x + y

    binary = ctypes.cdll.LoadLibrary("bin/main.c.so")
    func = getattr(binary, "add")

    return func(add, (a, b))


def add_go(a, b):
    binary = ctypes.cdll.LoadLibrary("bin/main.go.so")
    func = getattr(binary, "Sum")
    func.restype = ctypes.c_int

    func.argtypes = [
        ctypes.c_int,
        ctypes.c_int,
    ]

    return func(a, b)


def run_test_go(fname, params, ready_to_connect, before_test, after_test):
    binary = ctypes.cdll.LoadLibrary("bin/main.go.so")
    func = getattr(binary, fname)
    func.restype = ctypes.c_int

    func.argtypes = [ctypes.POINTER(ctypes.c_char),  # local ip
                     ctypes.c_int,                   # local port
                     ctypes.c_int,                   # params.count
                     ctypes.c_int,                   # msize
                     ctypes.c_int,                   # listen value
                     TIME_CB,
                     TIME_CB,
                     TIME_CB
                     ]
    host = "127.0.0.1".encode("utf-8") + b"\x00"
    func(host,
         8080,
         1024,
         1024 * 64,
         get_listen_param(256),
         TIME_CB(ready_to_connect),
         TIME_CB(before_test),
         TIME_CB(after_test))


def run_callback():
    binary = ctypes.cdll.LoadLibrary("bin/main.go.so")
    func = getattr(binary, "Foo")
    func.restype = ctypes.c_int
    times = []

    def callback():
        print("Hello, from callback")
        times.append(os.times())

    CALLBACK = ctypes.CFUNCTYPE(None)
    func.argtypes = [
        CALLBACK
    ]

    func(CALLBACK(callback))


def run_test():
    binary = ctypes.cdll.LoadLibrary("bin/main.go.so")
    func = getattr(binary, "RunTest")
    func.restype = ctypes.c_int
    times = []

    def stamp():
        times.append(os.times())

    def ready_func():
        print("Ready")

    CALLBACK = ctypes.CFUNCTYPE(None)
    func.restype = ctypes.c_int
    func.argtypes = [ctypes.POINTER(ctypes.c_char),  # local ip
                     ctypes.c_int,                   # local port
                     ctypes.c_int,                   # params.count
                     ctypes.c_int,                   # msize
                     ctypes.c_int,                   # listen value
                     CALLBACK,
                     CALLBACK,
                     CALLBACK]

    func("127.0.0.1".encode(),
         8000,
         1000,
         65535,
         1000,
         CALLBACK(ready_func),
         CALLBACK(stamp),
         CALLBACK(stamp))


if __name__ == "__main__":
    run_test()
    # print(add_c(1, 2))
    # print(add_c_with_callback(3, 4))
    # print(add_go(1, 2))

    # def ready_to_connect():
    #     print("Hello")
    #
    # times = []
    #
    # def stamp():
    #     times.append(os.times())
    #
    # run_test_go("Run", "",
    #             ready_to_connect,
    #             stamp,
    #             stamp)
