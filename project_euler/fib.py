__author__ = 'Gawaine_OGilvie'


class Fibonacci:

    def __init__(self):
        pass

    def fib(self, n):
        """Returns the Nth number in the fibonacci sequence"""

        if n <= 0:
            return None
        if n == 1:
            return 0
        if n == 2:
            return 1

        a, b = 0, 1
        count = 2
        next_num = 0
        while count != n:
            print(a,b)
            count += 1
            next_num = a + b
            a, b = b, next_num
        return next_num


if __name__ == '__main__':
    f = Fibonacci()
    print("Nth number is :", f.fib(5))
