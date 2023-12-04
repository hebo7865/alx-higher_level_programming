#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	return (palind(head, *head));
}

/**
 * palind - to check if palindrome
 * @head: head of list
 * @end: list end
 * Return: always 0
*/
int palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
	{
		return (-1);
	}
	if (palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
