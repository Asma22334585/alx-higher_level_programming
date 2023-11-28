#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number
 * Return: pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *new;

	node = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (node->next != NULL)
	{
		if ((node->next)->n >= number)
		{
			new->next = node->next;
			node->next = new;
			return (new);
		}
		node = node->next;
	}
	new->next = NULL;
	node->next = new;
	return (new);
}
