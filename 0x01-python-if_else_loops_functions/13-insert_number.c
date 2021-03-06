#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the first node of the linked list
 * @number: the number to be inserted
 *
 * Return: listint_t* - the address of the new node, or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *leader, *trailer, *new;

	leader = *head;
	leader = leader->next;
	trailer = *head;
	new = malloc(sizeof(*new));

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if(*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	if (leader == NULL || trailer->n > number)
	{
		if (trailer->n > number)
		{
			new->next = *head;
			*head = new;
			return (new);
		}
		new->next = trailer->next;
		trailer->next = new;
		return (new);
	}
	while (leader)
	{
		if (leader->n >= number && trailer->n <= number)
		{
			new->next = leader;
			trailer->next = new;
			break;
		}
		leader = leader->next;
		trailer = trailer->next;
		if (leader == NULL)
		{
			new->next = NULL;
			trailer->next = new;
		}
	}
	return (new);
}
