#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: Pointer to a PyObject (assumed to be a Python list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++) {
		PyObject *item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: Pointer to a PyObject (assumed to be a Python bytes object)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *data;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	data = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);

	printf("  first %ld bytes: ", (size < 10) ? size : 10);
	for (i = 0; i < size && i < 10; i++) {
		printf("%02hhx", data[i]);
		if (i < 9)
			printf(" ");
	}
	printf("\n");
}

