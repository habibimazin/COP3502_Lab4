
def hex_string_decode(hex):
    #get rid of 0x prefix
    if hex[0:2] == '0x':
        hex = hex[2:]


    bit_index = len(hex) - 1
    total = 0

    for digit in hex:
        total += hex_char_decode(digit) * pow(16, bit_index)
        bit_index -= 1
    return total

def hex_char_decode(digit):
   val = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
   return val.index(digit.upper())


def binary_string_decode(binary):
    if binary[0:2] == '0b':
        binary = binary[2:]

    bit_index = len(binary) - 1
    total = 0

    for digit in binary:
        total += int(digit) * pow(2, bit_index)
        bit_index -= 1
    return total


def binary_to_hex(binary):
    b_value = binary_string_decode(binary)
    numbers = []
    string = ""
    if b_value // 16 == 0:
        numbers.append(b_value)
    else:
        while True:
            quot = b_value // 16
            rem = b_value % 16
            numbers.insert(0, rem)
            b_value = quot
            if rem == 0 or quot == 0:
                numbers.insert(0,quot)
                break
    if 0 in numbers:
        numbers.remove(0)
    for number in numbers:
        if number == 10:
            let = "A"
        elif number == 11:
            let = "B"
        elif number == 12:
            let = "C"
        elif number == 13:
            let = "D"
        elif number == 14:
            let = "E"
        elif number == 15:
            let = "F"
        else:
            let = str(number)
        string += str(let)
    return string






if __name__ == "__main__":
    while True:

        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")
        print("")

        operation = int(input(("Please enter an option: ")))

        if operation == 1:
            hex = input("Please enter the numeric string to convert: ")
            hex_num = hex_string_decode(hex)
            print("Result:", hex_num)
            print("")
            continue

        elif operation == 2:
            convert_binary = input("Please enter the numeric string to convert: ")
            binary_num = binary_string_decode(convert_binary)
            print("Result:", binary_num)
            print('')
            continue

        elif operation == 3:
            convert_b_to_h = input("Please enter the numeric string to convert: ")
            binary = binary_to_hex(convert_b_to_h)
            print("Result: ", binary)
            continue

        elif operation == 4:
            print("Goodbye!")
            break
