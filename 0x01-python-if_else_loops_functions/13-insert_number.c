#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

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

	leader = *head->next;
	trailer = *head;
	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(*new));

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (leader == NULL)
	{
		if (trailer->n >= number)
		{
			new->next = trailer;
			*head = new;
		}
		trailer->next = new;
	}
	while (leader)
	{
		if (leader->n >= number && trailer->n <= number)
		{
			trailer->next = new;
			new->next = leader;
		}
		leader = leader->next;
		trailer = trailer->next;
	}
	return (new);
}
