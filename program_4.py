# Look at line 17 first.
# This program introduces a couple new concepts,
# we'll be covering those in the weeks ahead
def temp_conversion(celsius):
    # Write a program that converts Celsius temperatures to Fahrenheit temperatures. 
    # The formula is as follows: F = (9/5)C + 32
    # The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit.

    # Calculate the Fahrenheit equivalent.
    fahrenheit = 0.0
    #####################
    fahrenheit = (9/5)*(celsius) + 32
    ######################    


    # Return the variable to the calling function
    return fahrenheit

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    celsius = 0.0
    fahrenheit = 0.0
    # Get the Celsius temperature.
    celsius = float(input("Enter a Celsius temperature: "))
    fahrenheit = temp_conversion(celsius)
    # Display the Fahrenheit temperature.
    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")
