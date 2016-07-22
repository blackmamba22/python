#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the
multiples of five print “Buzz”. For numbers which are multiples of both three
and five print “FizzBuzz”."""


def fizz_buzz():
    """FizzBuzz function"""
    output = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", i)
            output.append("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz", i)
            output.append("Fizz")
        elif i % 5 == 0:
            print("Buzz", i)
            output.append("Buzz")
        else:
            print(i)
            output.append(i)


if __name__ == '__main__':
    fizz_buzz()
