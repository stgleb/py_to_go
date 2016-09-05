#include <python2.7/Python.h>

extern "C"
PyObject *add(PyObject *add_callback, PyObject *args) {
    int ok;
    int i, j;
    PyObject *result;
    PyObject *arg_list;

    // Check arg tuple
    if (!PyTuple_Check(args) || PyTuple_Size(args) < 2) {
        fprintf(stderr, "invalid input parameter\n");
        Py_RETURN_NONE;
    }
    // Parse arguments
    ok = PyArg_ParseTuple(args, "ii", &i, &j);

    if(!ok) {
        fprintf(stderr, "error while parsing args\n");
        Py_RETURN_NONE;
    }
    // build args tuple
    arg_list = Py_BuildValue("(ii)", i, j);

    // Check if add_callback is callable
    if(PyCallable_Check(add_callback) == 0) {
		result = PyObject_Call(add_callback, arg_list, NULL);
	} else {
		fprintf(stderr, "Object is not callable\n");
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