#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a list is a cycle.
 * @list: pointer to the head of the list.
 * Return: 0 if there is no cycle, and 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_step, *fast_step;

	if (!list)
		return (0);
	slow_step = fast_steps = list;
	while (slow_step && fast_steps && fast_steps->next)
	{
		slow_step = slow_step->next;
		fast_steps = fats_steps->next->next;
		if (slow_step == fast_steps)
			return (1);
	}
	return (0);
}