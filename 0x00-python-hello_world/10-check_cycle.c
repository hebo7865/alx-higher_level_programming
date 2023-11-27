#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to list we check
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *low, *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	low = list->next;
	fast = list->next->next;

	while (low && fast && fast->next)
	{
		if (low == fast)
		{
			return (1);
		}

		low = low->next;
		fast = fast->next->next;
	}
	return (0);
}
