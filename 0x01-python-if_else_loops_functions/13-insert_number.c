#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: input value
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp1;

	tmp1 = *head;
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || new_node->n <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{
		while (tmp1->next != NULL && tmp1->next->n < new_node->n)
		{
			tmp1 = tmp1->next;
		}
		new_node->next = tmp1->next;
		tmp1->next = new_node;
		return (new_node);
	}

}
