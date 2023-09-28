def reverse_array(arr):
    return arr[::-1]

input_str = input("Enter elements of the array separated by spaces: ")
user_array = [int(x) for x in input_str.split()]

reversed_array = reverse_array(user_array)

print("Reversed array:", reversed_array)
