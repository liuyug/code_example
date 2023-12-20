#include <Python.h>

int main(int argc, char *argv[])
{
    Py_SetProgramName(argv[0]);  /* optional but recommended */
    Py_Initialize();
    PyRun_SimpleString(argv[1]);
    Py_Finalize();
    return 0;
}
