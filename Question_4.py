def find_first_non_repeated_char(input_str):
    count = {}

    
    for i in input_str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    
    for i in input_str:
        if count[i] == 1:
            return i

    
    return None


try:
    input_str = input("Enter a string: ")

    first_non_repeated = find_first_non_repeated_char(input_str)

    if first_non_repeated is not None:
        print("The first non-repeated character is:", first_non_repeated)
    else:
        print("There are no non-repeated characters in the string.")

except ValueError:
    print("Invalid input. Please enter a valid string.")
