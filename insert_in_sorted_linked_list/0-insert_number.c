#include <stdlib.h>
#include "lists.h"


/**
 * Exersice 0. - Insert in sorted linked list
 * @head: double pointer
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	/* Create a new node */
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	/* insertion at the beginning or when list is empty */
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* treverse the list to find the correct spot */
	current = *head;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	/* insert new node between prev and current */
	prev->next = new_node;
	new_node->next = current;

	return (new_node);
}
