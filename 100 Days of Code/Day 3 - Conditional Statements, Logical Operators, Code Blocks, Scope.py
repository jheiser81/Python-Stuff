# ======================================================== #
# ======== Conditional Statements (if, else, elif) ======= #
# ======================================================== #

# A basic if/else statement in python looks like this:
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue filling")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You are allowed to ride the rollercoaster.") 
else:
    print("Sorry, you are too short to ride.")
# Essentially, an if/else statement is a boolean true/false statement with certain conditions. If the condition is true, a particular thing will happen. If the condition is not true (false) then something else will happen
# In Python, if/else statements end with a colon to denote the end of the statement. The next line is indented, to show that it is part of the previous code block. This is different from other languages, which use curly braces to denote code blocks. Python instead uses indentation to denote code blocks, so it is important to use indentation properly, or the code will throw and error.

# ======================================================== #
# ================= Comparison Operators ================= #
# ======================================================== #

# The basic comparison operators in Python are the same as most other programming languages:
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

# It is important to remember than a single = is the assignment operator. It is used to "asign" a value to a variable, whereas two == is the equality operator, and is used to compare two values against each other.

# ======================================================== #
# ============= Coding Exercise: Odd or Even ============= #
# ======================================================== #

# Write a program that determines whether a given number is odd or even. Even numbers can be divided by 2 with no remainder.

# number = int(input("Enter a number to check: "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# ======================================================== #
# =============== Nested if/else Statements ============== #
# ======================================================== #

# Nested if/else statements are "nested", or place inside of, other if/else statements. This allows for multiple conditiong to be checked, and different actions to be taken based on the results of those checks. It is a way of incorporating more complex logic into a program.
# if condition1 == true:
#     if condition2 == true:
#         do this
#     else:
#         do this
# else:
#     do this
# In this simple example, the first if statement checks if the first condition is true. If it is, it then checks if the next condition is true. If it is, it does one thing. If it is not, it does something else. If the first condition is not true, the program moves to the final else statement, does something else, and then exits the if/else block.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int (input("What is your age? "))
if height >= 120:
    if age >= 18:
        print("You are an adult, your ticket will cost $12.")
    elif age < 18:
        print("You are not an adult, your ticket will cost $7.")
    print("You are allowed to ride the rollercoaster.") 
else:
    print("Sorry, you are too short to ride.")

# In this example, the program first checks if the height is greater than or equal to 120. If it is, it then checks if the age is greater than or equal to 18. If it is, it prints one statement. If it is not, it prints another statement. If the height is not greater than or equal to 120, the program prints a different statement.

if height >= 120:
    print("You are allowed to ride the rollercoaster.")
    age = int (input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you are too short to ride.")
    
# This code uses the "elif" statement, which is short for "else if". It allows you to check another conditiong if the first condition is not true. You can use as many elif statements as you want, but you can only use one else statement per if statement (although you can still use an else statement for each elif statement).
# The else statement is a terminal statement, and will execute if none of the other conditions are true.
# In this way, we can check multiple conditions at once, and execute different code based on the results of those checks.

# Another way to check multiple conditions is to use the "and" operator. This allows you to check if two conditions are true at the same time. If they are, the program will execute the code in the if statement. If they are not, the program will execute the code in the else statement. Using the same code as above, we can rewrite it using the "and" operator:

if height >= 120 and age >= 18:
    print("You are allowed to ride the rollercoaster.")
    print("You are an adult, please pay $12.")
elif height < 120 and age <= 18:
    print("You are not an adult, so must be accompanied by one. Your ticket will cost $7.")
elif height < 120 and age < 12:
    print("You are not an adult, so must be accompanied by one. Your ticket will cost $5.")
else:
    print("Sorry, you are too short to ride.")


# ======================================================== #
# =============== Successive If Statements =============== #
# ======================================================== #

# The difference between using successive if statements and elif statements is that successive if statements will check every condition, regardless of whether the previous condition was true or not. Elif statements will only check the next condition if the previous condition was false. This can be seen in the following example:

# if condition1 == true:
#     print("Condition 1 is true.")
# if condition2 == true:
#     print("Condition 2 is true.")
# if condition3 == true:
#     print("Condition 3 is true.")
# else:
#     print("None of the conditions are true.")

# In this example, the program will check if condition1 is true. If it is, it will print the first statement. It will then check if condition2 is true. If it is, it will print the second statement. It will then check if condition3 is true. If it is, it will print the third statement. If none of the conditions are true, it will print the else statement. This is because each if statement is independent of the others, and will execute regardless of the results of the other if statements.

bill = 0
if height >= 120:
    print("You are allowed to ride the rollercoaster.")
    age = int (input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Would you like a photo taken? Y or N: ").upper()
    if wants_photo == "Y":
        bill += 3 # Same as bill = bill + 3
    print(f"Your final bill is ${bill}.")
    # No need for else statement here, because the $3 is only added if user selects Y for the photo.
else:
    print("Sorry, you are too short to ride.")
    
# ======================================================== #
# =================== Logical Operators ================== #
# ======================================================== #

# Logical operators allow you to combine multiple condition checks into a single line of code. The three most common logical operators are "and", "or", and "not". These operators allow for more complex logic to be implemented in a program.

# and: Both conditions must be true for the code to execute. If either condition is false, the code will not execute.
# or: Only one condition needs to be true for the code to execute. If both conditions are false, the code will not execute.
# not: This operator reverses the boolean value of a condition. If the condition is true, it will be false. If the condition is false, it will be true.


