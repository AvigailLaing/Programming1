def menu():
    print("\nDecoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
    option = int(input("\nPlease enter an option: "))
    return option
    #return this as the value when menu() is called
    #Use after the first time

def hex_char_decode(digit):
    #Include print statement Result:
    #Must be okay with Ox prefix or no 0x prefix
    #And hex typed in lowercase
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if digit in numbers:
        result = int(digit)
        #must turn digit into an integer otherwise it will stay a string and can't be multiplied in later functions
        return result
    else:
        digit = digit.upper()
        #turn all uppercase
        if digit == "A":
            result = 10
            return result
        elif digit == "B":
            result = 11
            return result
        elif digit == "C":
            result = 12
            return result
        elif digit == "D":
            result = 13
            return result
        elif digit == "E":
            result = 14
            return result
        elif digit == "F":
            result = 15
            return result
    #DONE YAYYYYY :)
def hex_string_decode(hex):
    #Use the above function to make it easier then
    #multiply each by power of 13
    #To iterate backwards, create for loop with
    #length of the string that moves backwards
    #4 character string fFfF should start at 4
    #use hex[i] to access a character at i position
    #in the string
    power = 0
    sum = 0
    for i in range(len(hex) - 1, -1, -1):
        digit = hex[i]
        sum += hex_char_decode(digit) * (16**power)
        power += 1
        #hex will be [f F f F]
        #so we want to snatch the last F
        #which is indexed at 3 since indexes start at 0
        #so range needs to start at len(hex) - 1
        #and the lower limit of range needs to be -1 since
        #range is exclusive of the last value
    return sum

def binary_string_decode(binary):
    #go backwards through this
    #create a power variable and go up
    #for each value, if 1, multiply by 2 by power and add to sum
    power = 0
    sum = 0
    for i in range (len(binary) - 1, -1, -1):
        digit = int(binary[i])
        if digit == 1:
            sum += digit * (2**power)
        power += 1
    return sum
    #done yayyyyyy

def binary_to_hex(binary):
    #first convert to decimal
    decimal = binary_string_decode(binary)
    remainders = []
    #now convert decimal to hex
    while decimal > 0:
        #FIRST append the remainder because otherwise if you change decimal first // 16, then the remainder = decimal % 16 won't use the right decimal
        remainder = decimal % 16
        decimal = decimal // 16
        remainders.append(remainder)
        #Add this remainder to a list
    #Now once decimal is 0, we convert any remainders that are
    #hex values above 9 to letters and print the list backwards
    result = []
    for i in range(len(remainders) - 1, -1, -1):
        remainder = str(remainders[i])
        #go backwards through list so we can just print it out
        #like this and it will be in the correct order
        # [12, 3]
        #it will start with 3
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if remainder in numbers:
            result.append(remainder)
        else:
            if remainder == "10":
                result.append("A")
            elif remainder == "11":
                result.append("B")
            elif remainder == "12":
                result.append("C")
            elif remainder == "13":
                result.append("D")
            elif remainder == "14":
                result.append("E")
            elif remainder == "15":
                result.append("F")
    #now we print the list without spaces in between
    result = (''.join(result))
    return result.zfill(4)
    #Because test case is being weird?

option = menu()
#This not only prints the menu, but also sets the option variable equal to the value returned by menu() (our input)
while option != 4:
    string = input("Please enter the numeric string to convert: ")
    if option == 1:
        #find a way to first check for 0x and yeet it out
        #so it doesn't mess with the length functions
        if string.startswith("0x") or string.startswith("0X"):
            string = string[2:]
            #THIS REMOVES THE FIRST 2 CHARACTERS
        if len(string) == 1:
            digit = string
            print(f"Result: {hex_char_decode(digit)}")
        else:
            hex = string
            print(f"Result: {hex_string_decode(hex)}")
        #print menu again
    elif option == 2:
        if string.startswith("0b") or string.startswith("0B"):
            string = string[2:]
        binary = string
        print(f"Result: {binary_string_decode(binary)}")
    elif option == 3:
        if string.startswith("0b") or string.startswith("0B"):
            string = string[2:]
        #have to add this to option 3 too lol
        binary = string
        print(f"Result: {binary_to_hex(binary)}")
    option = menu()
    #Once an operation has been done, we need a new option value, so run the menu again
    #Now if 4 is chosen, the while loop will break and we run the following line
print("Goodbye!")

