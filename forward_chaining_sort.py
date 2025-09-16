"""
Sorting using Forward Chaining

This script demonstrates sorting a list using forward chaining (rule-based reasoning).
"""

def forward_chaining_sort(arr):
    print(f"Initial list: {arr}")
    n = len(arr)
    changed = True
    step = 1
    while changed:
        changed = False
        for i in range(n - 1):
            # Rule: If arr[i] > arr[i+1], swap them
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
                print(f"Step {step}: Swapped {arr[i+1]} and {arr[i]} -> {arr}")
                step += 1
    print(f"Sorted list: {arr}")
    return arr

if __name__ == "__main__":
    # Example usage
    data = [5, 2, 9, 1, 5, 6]
    forward_chaining_sort(data)
