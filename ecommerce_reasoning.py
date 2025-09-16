"""
Logical Reasoning for E-commerce Stores using Forward and Backward Chaining
"""

# Forward Chaining Example: Discount Recommendation
def forward_chaining_discount(user):
    facts = []
    if user['purchases'] > 5:
        facts.append('loyal_customer')
    if user['cart_value'] > 100:
        facts.append('high_cart')
    # Rules
    if 'loyal_customer' in facts and 'high_cart' in facts:
        return 'Recommend 10% discount'
    elif user['is_new']:
        return 'Recommend 5% discount'
    else:
        return 'No discount'

# Backward Chaining Example: Free Shipping Eligibility
def backward_chaining_free_shipping(user):
    # Goal: eligible for free shipping
    if user['cart_value'] > 200:
        return True
    elif user['is_premium']:
        return True
    else:
        return False

if __name__ == "__main__":
    user1 = {'purchases': 8, 'cart_value': 120, 'is_new': False, 'is_premium': False}
    user2 = {'purchases': 1, 'cart_value': 250, 'is_new': True, 'is_premium': True}
    print("Forward Chaining Discount for user1:", forward_chaining_discount(user1))
    print("Backward Chaining Free Shipping for user1:", backward_chaining_free_shipping(user1))
    print("Forward Chaining Discount for user2:", forward_chaining_discount(user2))
    print("Backward Chaining Free Shipping for user2:", backward_chaining_free_shipping(user2))
