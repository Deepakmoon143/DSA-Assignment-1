def are_rotations(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    
    concat_str = str1 + str1

    
    if str2 in concat_str:
        return True
    else:
        return False


try:
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    if are_rotations(str1, str2):
        print("The two strings are rotations of each other.")
    else:
        print("The two strings are not rotations of each other.")

except ValueError:
    print("Invalid input. Please enter valid strings.")
