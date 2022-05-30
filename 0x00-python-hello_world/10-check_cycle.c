#include "lists.h"

/**
 * check_cycle - checks whether a singly linked list has a cycle in it or not
 * @list: pointer to a linked list
 *
 * Return: 1 if list is a cycle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	slow_p = list;
	fast_p = list;

	while (slow_p && fast_p)
	{
		if (fast_p->next == NULL)
			return (0);
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}

	return (0);
}
