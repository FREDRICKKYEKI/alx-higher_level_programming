#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info - prints a python list info
 *
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item - PyList_GetItem(p, i);
		printf("Element %ld:v%s\n", i, Py_TYPE(item)->tp_name);
	}
}
