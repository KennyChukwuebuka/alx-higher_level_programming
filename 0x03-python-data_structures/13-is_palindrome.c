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
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;
/*check empty list or list with single element is palindrome*/
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
/*find the middle of list and reverse the first*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
/*reverse first half of the list*/
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
/*if list has odd number of ele, skip middle ele*/
	if (fast != NULL)
	{
		slow = slow->next;
	}
/*compare reversed first half with second half*/
	while (slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);/*not a palindrome*/
		}
		prev = prev->next;
		slow = slow->next;
	}
	return (1);/*palindrome*/
}
