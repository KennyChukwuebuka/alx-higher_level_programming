#include <Python.h>
/**
 * print_python_list_info - Cpython function
 * @p: params
 *
 * Return: pyhton list
 */

#include <Python.h>

void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Invalid argument: Not a Python list.\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	if (size > 0)
	{
		PyObject *last_element = PyList_GetItem(p, size - 1);

		printf("[*] Element %ld: %s\n", size - 1,
				Py_TYPE(last_element)->tp_name);
	}

	printf("[*] Element %ld: %s\n", p->ob_refcnt, Py_TYPE(p)->tp_name);
}
