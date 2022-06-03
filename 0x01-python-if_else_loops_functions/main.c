#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - create list and test insert in NULL / empty list
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	print_listint(head);

	printf("-----------------\n");

	insert_node(&head, 972);

	print_listint(head);

	free_listint(head);

	return (0);
}

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

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
	new->next = NULL;

	if(*head == NULL)
	{
		*head = new;
		return (new);
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
