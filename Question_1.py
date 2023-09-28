def find_pairs_with_sum(arr, target_sum):
    pairs = []
    num = set() 

    for i in arr:
        difference = target_sum - i
        if difference in num:
            pairs.append((i, difference))
        num.add(i)

    return pairs


arr_str = input("Enter the array elements separated by spaces: ")
target_sum = int(input("Enter the target sum: "))


arr = list(map(int, arr_str.split()))


result = find_pairs_with_sum(arr, target_sum)

if result:
    print("Pairs with sum", target_sum, "are:", result)
else:
    print("No pairs with sum", target_sum, "found in the array.")

