'''
Created on Feb 2, 2016

@author: Christopher
'''
from cs115 import map, reduce, range
def mult(x,y):
    """Returns the product of x and y"""
    return x*y
def add(x,y):
    """Returns the sum of x and y"""
    return x+y
def factorial(n):
    """Returns n!"""
    return reduce(mult, list(range(1,n+1)))
def mean(L):
    """Takes a list as input and returns the mean value in that list"""
    return reduce(add,L)/len(L)
def div(k):
    return 42%k==0
def divides(n):
    def div(k):
        return n%k==0
    return div
def prime(n):
    """Returns True if n is prime and False if n is not"""
    if map(divides(n), list(range(2,n)))==[False]*(n-2):
        return True
    return False

