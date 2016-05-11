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

if __name__ == '__main__':
    print (convert_decimal_to_binary(233))
    print (convert_decimal_to_binary(42))
