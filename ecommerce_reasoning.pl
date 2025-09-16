% Logical Reasoning for E-commerce Stores using Forward and Backward Chaining

% Facts: user(purchases, cart_value, is_new, is_premium)
user(user1, 8, 120, false, false).
user(user2, 1, 250, true, true).

% Forward Chaining Rules: Discount Recommendation
recommend_discount(User, '10%') :-
    user(User, Purchases, CartValue, _, _),
    Purchases > 5, CartValue > 100.
recommend_discount(User, '5%') :-
    user(User, _, _, true, _).
recommend_discount(User, 'No discount') :-
    user(User, _, _, _, _),
    \+ recommend_discount(User, _).

% Backward Chaining Rules: Free Shipping Eligibility
eligible_free_shipping(User) :-
    user(User, _, CartValue, _, _), CartValue > 200.
eligible_free_shipping(User) :-
    user(User, _, _, _, true).

% Example queries:
% ?- recommend_discount(user1, Discount).
% ?- eligible_free_shipping(user2).
