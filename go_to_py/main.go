package main

import (
	"C"
	"fmt"
)

//export Sum
func Sum(a, b int) int {
	return a + b
}

//export Run
func Run(h *C.char, port, threadCount, msize, listenQueue C.int) int {
	host := C.GoString(h)
	fmt.Printf("host %s port %d th_count %d msize %d listen_queue %d",
		host,
		port,
		threadCount,
		msize,
		listenQueue)

	return 0
}

func main() {

}
