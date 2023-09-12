#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - palindrome function
 * @head: param
 * Return: Always 0 OR 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *ele_slow = *head;
	listint_t *ele_fast = *head;
	listint_t *ele_prev = NULL;
	listint_t *ele_tp;
/*check empty list or list with single element is palindrome*/
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
/*find the middle of list and reverse the first*/
	while (ele_fast != NULL && ele_fast->next != NULL)
	{
		ele_fast = ele_fast->next->next;
/*reverse first half of the list*/
		ele_tp = ele_slow;
		ele_slow = ele_slow->next;
		ele_tp->next = ele_prev;
		ele_prev = ele_tp;
	}
/*if list has odd number of ele, skip middle ele*/
	if (ele_fast != NULL)
	{
		ele_slow = ele_slow->next;
	}
/*compare reversed first half with second half*/
	while (ele_slow != NULL)
	{
		if (ele_prev->n != ele_slow->n)
		{
			return (0);/*not a palindrome*/
		}
		ele_prev = ele_prev->next;
		ele_slow = ele_slow->next;
	}
	return (1);/*palindrome*/
}
