from stack import Stack


def convert_decimal_to_binary(dec_number):
    """
    Converts a decimal value (dec_number) to a binary number
    """
    # declare a stack to hold binary digits
    remstack = Stack()

    # while number greater than 0, push digit 1 onto stack if number is odd,
    # ,push 0 if even. Then divided by 2 to get the next number (w/ floor division)
    while dec_number > 0:
        rem = dec_number % 2
        remstack.push(rem)
        dec_number = dec_number // 2

    # now pop all values off the stack and append to empty string.
    # the values popped off equals the binary result
    binary_result = ""
    while not remstack.isEmpty():
        binary_result += str(remstack.pop())

    return binary_result


def base_converter(dec_number, base):
    """
    Converts a decimal number from base 10 to another base provided.
    Bases 2 and up.
    """
    digits = "0123456789ABCDEF"

    remstack = Stack()
    while dec_number > 0:
        rem = dec_number % base
        remstack.push(rem)
        dec_number = dec_number // base

    new_base_result = ""
    while not remstack.isEmpty():
        new_base_result += digits[remstack.pop()]

    return new_base_result

if __name__ == '__main__':
    print (convert_decimal_to_binary(233))
    print (convert_decimal_to_binary(42))
    print(base_converter(26,26))
    print(base_converter(233,16))
