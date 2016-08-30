import ctypes


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


def add_go(a, b):
    binary = ctypes.cdll.LoadLibrary("bin/main.go.so")
    func = getattr(binary, "Sum")
    func.restype = ctypes.c_int

    func.argtypes = [
        ctypes.c_int,
        ctypes.c_int,
    ]

    return func(1, 2)


def run_test_go(fname, params, ready_to_connect, before_test, after_test):
    binary = ctypes.cdll.LoadLibrary("bin/main.go.so")
    func = getattr(binary, fname)
    func.restype = ctypes.c_int

    func.argtypes = [ctypes.POINTER(ctypes.c_char),   # local ip
                     ctypes.c_int,                   # local port
                     ctypes.c_int,                   # params.count
                     ctypes.c_int,                   # msize
                     ctypes.c_int,                   # listen value
                    ]
    host = "127.0.0.1".encode("utf-8") + b"\x00"
    func(host,
         8080,
         1024,
         1024 * 64,
         get_listen_param(256))

if __name__ == "__main__":
    # print(add_c(1, 2))
    # print(add_go(1, 2))
    run_test_go("Run", "", "", "", "")

