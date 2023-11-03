#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a sorted singly linked list.
 *
 * @head: pointer to the first node
 * @number: the data of the inserted node
 *
 * Return: the address of the new node, or NULL if it failed
**/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *tempNode;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL || (*head)->n >= number)
    {
        new->next = *head;
        *head = new;
    }
    else
    {
        tempNode = *head;
        while (tempNode->next != NULL && tempNode->next->n < number)
        {
            tempNode = tempNode->next;
        }
        new->next = tempNode->next;
        tempNode->next = new;
    }

    return (new);
}
