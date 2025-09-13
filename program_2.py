
def average_age():
   # Get User Input
    age1 = float(input("What is your first friend's age? "))
    age2 = float(input("What is your second friend's age? "))
    age3 = float(input("What is your third friend's age? "))
    age4 = float(input("What is your fourth friend's age? "))
    age5 = float(input("What is your fifth friend's age? "))
    # Sum ages
    allAges = age1 + age2 + age3+ age4 + age5
    # Average the ages
    allAges = allAges / 5
    # Print the results
    print("The average age of your friends is", allAges)
# Line which calls the above function.
average_age()