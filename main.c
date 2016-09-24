#include <python3.5/Python.h>

extern "C"
PyObject *add(PyObject *add_callback) {
    int ok;
    PyObject *result;
    PyObject *arg_list = NULL;
    printf("Start function add\n");

    arg_list = Py_BuildValue("()", NULL);
    printf("Build arg tuple %p\n", arg_list);
    // Check if add_callback is callable
    if(PyCallable_Check(add_callback)) {
        printf("callback object is callable\n");
		result = PyObject_Call(add_callback, arg_list, NULL);
	} else {
		printf("Object is not callable\n");
		Py_RETURN_NONE;
	}

    return result;
}

extern "C"
int sum(int a, int b) {
    return a + b;
}


int main() {
    return 0;
}