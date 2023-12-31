#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * palindrome -  checks if a singly linked list is a palindrome.
 * @head: head list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if(!head || !*head)
		return (1);
	return (palind(head, *head));
}
/**
 * palind - is palindrome or not
 * @head: head list
 * @end: end list
 */
int palind(listint_t ** head, listint_t *end)
{
	if (!end)
		return (1);
	if (palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
