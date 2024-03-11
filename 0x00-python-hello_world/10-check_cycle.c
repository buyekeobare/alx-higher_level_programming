#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *down = list;
	listint_t *up = list;

	if (!list)
		return (0);

	while (down && up && up->next)
	{
		down = down->next;
		up = up->next->next;
		if (down == up)
			return (1);
	}

	return (0);
}