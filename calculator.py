def calculator(num1, num2, operator):
    """
    This function performs basic arithmetic and comparison operations on two numbers.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    operator (str): A string representing the operation to perform. The valid operators are:
        - "+" for addition
        - "-" for subtraction
        - "*" for multiplication
        - "/" for division
        - "%" for modulus
        - ">" for greater than comparison
        - ">=" for greater than or equal to comparison
        - "<" for less than comparison
        - "<=" for less than or equal to comparison

    Returns:
    result: The result of the arithmetic operation or comparison. The type of the result depends on the operator:
        - int or float for arithmetic operations
        - bool for comparison operations

    Example Usage:
    --------------
    calculate(4, 5, "*")  # Output: The result is: 20
    calculate(10, 2, "/")  # Output: The result is: 5.0
    calculate(7, 7, ">=")  # Output: The comparison result is: True

    Note:
    -----
    - If division by zero is attempted, the function prints an error message and does not return a result.
    - If an invalid operator is provided, the function prints an error message and does not return a result.
    """
    if operator == "+":
        return "The result is:", num1 + num2
    elif operator == "-":
        return "The result is:", num1 - num2

    # Function implementation here ...
        
    elif operator=="*":
        return "The result is:", num1*num2
    elif operator=="/":
        if num2==0:
            return "Unable to divide by zero"
        else:
            return "The result is:", num1/num2
    elif operator=="%":
        return "The result is:", num1%num2
    elif operator==">":
        return "The result is:", num1>num2
    elif operator==">=":
        return "The result is:", num1>=num2
    elif operator=="<":
        return "The result is:", num1<num2
    elif operator=="<=":
        return "The result is:", num1<=num2

    else:
        return "Invalid operator"

## Run the example
# calculator(4, 5, "*")  # Output: The result is: 20
# calculator(10, 2, "/")  # Output: The result is: 5.0
# calculator(7, 7, ">=")  # Output: The comparison result is: True


#use this later at the end of the function's completion


# Following "comment" lines are used for testing, not to be assessed

'''
print("Enter your first number:")
usernum1=int(input())
print("\nEnter the operator:")
userop=str(input())
print("\nEnter your second number:")
usernum2=int(input())
print(calculator(usernum1, usernum2, userop))
'''

print(calculator(4, 5, "*"))
print(calculator(10, 2, "/"))
print(calculator(7, 7, ">="))