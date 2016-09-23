package main

// #cgo pkg-config: python3
// #define Py_LIMITED_API
// #include <Python.h>
//extern void Foo();
//static inline void CallMyFunction(void* f) {
//    void (*func)() = f;
//    func();
//    printf("Hello, world %p!!!\n", f);
//}
//extern void BeforeTest();
//static inline void before_test(void* f) {
//    void (*func)() = f;
//    func();
//}
//extern void AfterTest();
//static inline void after_test(void* f) {
//    void (*func)() = f;
//    func();
//}
//extern void ReadyConn();
//static inline void ready_conn(void* f) {
//    void (*func)() = f;
//    func();
//}
import "C"
import (
	"fmt"
	"unsafe"
)


/* Super strange thing, when import is make like
	import (
		"C"
		"fmt"
		)
   Code doesnt work with" "could not determine kind of name for C.PyObject"
*/

//export Sum
func Sum(a, b int) int {
	return a + b
}

//export Foo
func Foo(f unsafe.Pointer) {
	C.CallMyFunction(f)
}

func beforeTest(f unsafe.Pointer) {
	fmt.Printf("Before test hook")
	C.before_test(f)
}

func afterTest(f unsafe.Pointer) {
	fmt.Printf("After test hook")
	C.before_test(f)
}

func ready(f unsafe.Pointer) {
	fmt.Printf("Connections are ready")
	C.ready_conn(f)
}

// NOTE: Calling C function pointers is currently not supported https://golang.org/cmd/cgo/
//export Run
func Run(h *C.char, port, threadCount, msize, listenQueue C.int,
	 readyToConnect *C.PyObject, beforeTest *C.PyObject,
	 afterTest *C.PyObject) *C.PyObject {
	host := C.GoString(h)
	fmt.Printf("host %s port %d th_count %d msize %d listen_queue %d",
		host,
		port,
		threadCount,
		msize,
		listenQueue)

	var args *C.PyObject
	//var kwargs *C.PyObject
	args = C.PyTuple_New(0);
	//kwargs = C.Py_BuildValue("{s:i}","b", 5)

	if C.PyCallable_Check(readyToConnect) == 0 {
		C.PyObject_Call(readyToConnect, args, nil)
	} else {
		fmt.Printf("Object is not callable")
	}

	return C.PyLong_FromLongLong(0)
}

//export RunTest
func RunTest(h *C.char, port, threadCount, msize, listenQueue int,
	readyConn, before, after unsafe.Pointer) int {
	localAddr := C.GoString(h)
	fmt.Printf("Start Test")
	fmt.Printf("LocalAddr: %s LocalPort: %d ThreadCount: %d Msize: %d ListenQueue: %d",
		localAddr, port, threadCount, msize, listenQueue)
	beforeTest(before)
	afterTest(after)
	ready(readyConn)

	return 0
}

func main() {

}
