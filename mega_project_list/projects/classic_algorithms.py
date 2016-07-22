import sys


def collatz_conjecture(n):
    ""
    steps = 0
    result = n
    while result != 1:
        if n % 2 == 0:
            result /= 2
            steps += 1
        else:
            result = (result * 3) + 1
            steps += 1

    return steps

if __name__ == '__main__':
    print(collatz_conjecture(4))
