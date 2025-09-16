
# Logical Reasoning for E-commerce Stores (Python & Prolog)

This README explains how forward and backward chaining can be used for logical reasoning in e-commerce scenarios, with both Python and Prolog examples.

## Forward Chaining (Python)
- Facts: User's purchase history, cart value, etc.
- Rules: If user is loyal and has high cart value, recommend 10% discount. If new, recommend 5% discount.
- Reasoning: Start from facts and apply rules to reach a recommendation.

## Backward Chaining (Python)
- Goal: Is user eligible for free shipping?
- Rules: If cart value > $200 or user is premium, eligible for free shipping.
- Reasoning: Start from goal and check if facts/rules support it.

## Prolog Examples
- Prolog rules for discount recommendation and free shipping eligibility.
- Example queries provided in comments.

See `ecommerce_reasoning.py` and `ecommerce_reasoning.pl` for code and comments.