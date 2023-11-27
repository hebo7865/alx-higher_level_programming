#include <stdio.h>
#include <stdlib.h>
#include "limits.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to list we check
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *low = list, *fast = list;

	while (fast && fast->next)
	{
		low = low->next;
		fast = fast->next;
		if (low == fast)
		{
			return (1);
		}
	}
	return (0);
}
