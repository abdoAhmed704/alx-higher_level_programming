#include "lists.h"
/**
 * check_cycle - a function in C that checks if a
 * singly linked list has a cycle in it.
 *
 * @list: pointer to the first node
 *
 * Return: (1) if it's cycle and (0) if it's not
*/
int check_cycle(listint_t *list)
{
	listint_t *first = list, *second = list;

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
