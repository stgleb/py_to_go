/* Created by "go tool cgo" - DO NOT EDIT. */

/* package command-line-arguments */

/* Start of preamble from import "C" comments.  */


#line 3 "/home/stgleb/workspace/py_to_go/main.go"

 #define Py_LIMITED_API
 #include <Python.h>
 extern void Foo();
static inline void CallMyFunction(void* f) {
    void (*func)() = f;
    func();
    printf("Hello, world %p!!!\n", f);
}
 extern void BeforeTest();
static inline void before_test(void* f) {
    void (*func)() = f;
    func();
}
 extern void AfterTest();
static inline void after_test(void* f) {
    void (*func)() = f;
    func();
}
 extern void ReadyConn();
static inline void ready_conn(void* f) {
    void (*func)() = f;
    func();
}



/* End of preamble from import "C" comments.  */


/* Start of boilerplate cgo prologue.  */

#ifndef GO_CGO_PROLOGUE_H
#define GO_CGO_PROLOGUE_H

typedef signed char GoInt8;
typedef unsigned char GoUint8;
typedef short GoInt16;
typedef unsigned short GoUint16;
typedef int GoInt32;
typedef unsigned int GoUint32;
typedef long long GoInt64;
typedef unsigned long long GoUint64;
typedef GoInt64 GoInt;
typedef GoUint64 GoUint;
typedef __SIZE_TYPE__ GoUintptr;
typedef float GoFloat32;
typedef double GoFloat64;
typedef float _Complex GoComplex64;
typedef double _Complex GoComplex128;

/*
  static assertion to make sure the file is being used on architecture
  at least with matching size of GoInt.
*/
typedef char _check_for_64_bit_pointer_matching_GoInt[sizeof(void*)==64/8 ? 1:-1];

typedef struct { const char *p; GoInt n; } GoString;
typedef void *GoMap;
typedef void *GoChan;
typedef struct { void *t; void *v; } GoInterface;
typedef struct { void *data; GoInt len; GoInt cap; } GoSlice;

#endif

/* End of boilerplate cgo prologue.  */

#ifdef __cplusplus
extern "C" {
#endif


extern GoInt Sum(GoInt p0, GoInt p1);

extern void Foo(void* p0);

// NOTE: Calling C function pointers is currently not supported https://golang.org/cmd/cgo/

extern PyObject* Run(char* p0, int p1, int p2, int p3, int p4, PyObject* p5, PyObject* p6, PyObject* p7);

extern GoInt RunTest(char* p0, GoInt p1, GoInt p2, GoInt p3, GoInt p4, void* p5, void* p6, void* p7);

#ifdef __cplusplus
}
#endif
