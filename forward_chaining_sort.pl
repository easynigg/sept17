% Sorting using Forward Chaining in Prolog
% This example uses a simple bubble sort logic with forward chaining rules.

% swap_adjacent(List, SwappedList) succeeds if two adjacent elements are out of order and swaps them.
swap_adjacent([X,Y|Rest], [Y,X|Rest]) :- X > Y.
swap_adjacent([Z|Rest], [Z|Rest1]) :- swap_adjacent(Rest, Rest1).

% forward_chaining_sort(List, SortedList) applies swap_adjacent until no more swaps are possible.
forward_chaining_sort(List, SortedList) :-
    swap_adjacent(List, List1), !,
    forward_chaining_sort(List1, SortedList).
forward_chaining_sort(List, List).

% Example query:
% ?- forward_chaining_sort([5,2,9,1,5,6], Sorted).
% Sorted = [1,2,5,5,6,9].
