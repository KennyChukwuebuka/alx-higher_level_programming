#include <Python.h>
/**
 * print_python_list_info - Cpython function
 * @p: params
 *
 * Return: pyhton list
 */

void print_python_list_info(PyObject *p)
{

	if (!PyList_Check(p))
	{
		printf("Invalid argument: Not a Python list.\n");
		return;
	}


	Py_ssize_t size = PyList_Size(p);


	Py_ssize_t ref_count = p->ob_refcnt;


	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	if (size > 0)
	{
		printf("[*] Element %ld: %s\n", size - 1,
				Py_TYPE(PyList_GetItem(p, size - 1))->tp_name);
	}

	printf("[*] Element %ld: %s\n", ref_count, Py_TYPE(p)->tp_name);
}