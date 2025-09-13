def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    #Get user input
    price1 = float(input("What is the price of your first item? "))
    price2 = float(input("What is the price of your second item? "))
    price3 = float(input("What is the price of your third item? "))
    price4 = float(input("What is the price of your fourth item? "))
    price5 = float(input("What is the price of your fifth item? "))
    #Calculate subtotal
    subtotal = price1 + price2 + price3 + price4 + price5
    #Calculate sales tax
    salesTax = subtotal * .07
    #Calculate total
    total = subtotal + salesTax
    #Print subtotal, sales tax, and total
    print("Your subtotal is $", subtotal)
    print("Your sales tax is $", salesTax)
    print("Your total is $", total)
calculate_total_purchase()