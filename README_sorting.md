
# Sorting using Forward Chaining (Python & Prolog)

This README explains the implementation of sorting using forward chaining in both Python and Prolog. Forward chaining is a reasoning method that starts with known facts and applies rules to reach a goal.

## Python Implementation
- The script uses a bubble sort-like approach.
- It repeatedly checks adjacent elements and swaps them if out of order.
- Each swap is a rule application, and the process continues until the list is sorted.
- The code prints each step for clarity.

## Prolog Implementation
- Uses rules to swap adjacent elements if needed.
- Recursively applies the swap rule until the list is sorted.
- Example query: `?- forward_chaining_sort([5,2,9,1,5,6], Sorted).`

See `forward_chaining_sort.py` and `forward_chaining_sort.pl` for code and comments.