#include "lists.h"
/**
 * check_cycle - function that checks for a circle
 * @list: pointer
*/
int check_cycle(listint_t *list)
{
  listint_t *slw = list;
  listint_t *fst = list;

  if(!list)
  return (0);
  while (slw && fst && fst->next)
  {
    slw = slw->next;
    fst = fst->next;
    if(slw == fst)
    return (1);
  }
  return (0);
}
