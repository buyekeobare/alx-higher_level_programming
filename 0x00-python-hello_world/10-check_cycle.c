#include "lists.h"

/**
 * check_cycle - Function to check if cycle exists in a list
 * @list: pointer to head of linked_list
 * Return: 1 if cycle exists, 0 if it doesn't
 **/

int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	if (list == NULL || list->next == NULL)
		return (0);
	temp1 = temp2 = list;
	while (temp1 != NULL)
	{
		temp1 = temp1->next;
		if (temp1 == NULL)
			return (0);
		temp2 = temp2->next;
		temp1 = temp1->next;
		if (temp1 == temp2)
			return (1);
	}

	return (0);
}