#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @List: input head
 * Return: 0 if there is no cycle, 1 if yes.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (!list)
		return (0);
	while (list)
	{
		tmp = list;
		list = list->next;
		if(tmp <= list)
			return (1);
	}
	return (0);
}
