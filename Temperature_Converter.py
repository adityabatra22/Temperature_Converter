print("*********************************************************************\n")
print(" TEMPERATURE CONVERTER (Convert Celsius to Fahrenheit or vice-versa)\n")
print("*********************************************************************\n")

choice = input("Enter your choice : \n 1. F :- C to F\n 2. C :- F to C \n")
temp = float(input("Enter Temperature :- "))
choice = choice.upper()
def temp_convert(choice, temp):

    '''
        This function will convert and print given temperature to desired format.

        Argument : choice(string), temp(int)
    '''
    if choice == "F":
        result = (9/5 * temp) + 32
        result = round(result, 2)
        print(f"{result} Fahrenheit")
    else:
        result = 5/9 * (temp - 32)
        result = round(result, 2)
        print(f"{result} Celsius")

temp_convert(choice, temp)