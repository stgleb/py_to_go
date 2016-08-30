package main

// #cgo pkg-config: python3
// #define Py_LIMITED_API
// #include <Python.h>
import "C"
import "fmt"


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

//export Run
func Run(h *C.char, port, threadCount, msize, listenQueue C.int,
	 readyToConnect *C.PyCFunction, beforeTest *C.PyCFunction,
	 afterTest *C.PyCFunction) *C.PyObject {
	host := C.GoString(h)
	fmt.Printf("host %s port %d th_count %d msize %d listen_queue %d",
		host,
		port,
		threadCount,
		msize,
		listenQueue)

	return C.PyLong_FromLongLong(0)
}

func main() {

}
