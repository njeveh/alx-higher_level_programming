#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first list element
 * Return: 0 if list is not a palindrome or 1 if list is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *start, *end;
	int i, size = 0;

	start = *head;
	end = *head;
	if (*head == NULL)
		return (1);
	while (start)
	{
		++size;
		start = start->next;
	}
	start = *head;
	while (size)
	{
		for (i = 0; i < size - 1; ++i)
		{
			end = end->next;
		}
		if (start->n != end->n)
			return (0);
		size -= 2;
		start = start->next;
		end = start;
	}
	return (1);
}
