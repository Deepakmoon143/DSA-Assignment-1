def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs


try:
    input_array = input("Enter an integer array (comma-separated): ")
    target_sum = int(input("Enter the target sum: "))
    
    input_array = input_array.split(',')
    input_array = [int(x.strip()) for x in input_array]

    pairs = find_pairs_with_sum(input_array, target_sum)

    if len(pairs) > 0:
        print("Pairs with the sum {} are:".format(target_sum))
        for pair in pairs:
            print(pair)
    else:
        print("No pairs found with the sum {}.".format(target_sum))

except ValueError:
    print("Invalid input. Please enter a valid integer array and target sum.")
