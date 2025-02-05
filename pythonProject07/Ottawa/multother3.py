def multiply_all(lst):
    if len(lst) != 4:
        return "List must have exactly 4 elements"

    result = []
    total_product = 1

    # Calculate the total product of all elements
    for num in lst:
        total_product *= num

    # For each element, append total_product divided by that element
    for num in lst:
        result.append(total_product // num)

    return result


# Example usage
my_list = [2, 3, 4, 5]
result = multiply_all(my_list)
print(result)  # Output: [60, 40, 30, 24]
