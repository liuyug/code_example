#include <Python.h>

int main(int argc, char *argv[])
{
    Py_Initialize() ;
    PyObject* PyFileObject = PyFile_FromString(argv[1], "r");
    PyRun_SimpleFile(PyFile_AsFile(PyFileObject), argv[1]);
    Py_Finalize();
    return 0;
}
