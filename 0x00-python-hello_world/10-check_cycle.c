#include "lists.h"

/**
 * check_cycle - Function that check cycle
 * @list: Params
 * Return: 1 OR 0
 */
int check_cycle(listint_t *list)
{

	listint_t *check_slow_cycle = list;
	listint_t *check_fast_cycle = list;

	if (!list)
		return (0);

	while (check_slow_cycle && check_fast_cycle && check_fast_cycle->next)
	{
		check_slow_cycle = check_slow_cycle->next;
		check_fast_cycle = check_fast_cycle->next->next;

		if (check_slow_cycle == check_fast_cycle)
			return (1);
	}
	return (0);
}
