def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...

    count=0

    for num in user_list:
        if num in winning_list:
            count+=1
    if count == 3:
        return "First"
    elif count == 2:
        return "Second"
    elif count == 1:
        return "Third"
    else:
        return "No"


    # Print the result


win_nums=[5, 14, 17]
usr_nums=[]

print("Enter your first number")
usernum1=int(input())
print("Enter your second number")
usernum2=int(input())
print("Enter your third number")
usernum3=int(input())

usr_nums.append(usernum1)
usr_nums.append(usernum2)
usr_nums.append(usernum3)

print(f"Congratulations, you won {winning_numbers(usr_nums, win_nums)} prize!")