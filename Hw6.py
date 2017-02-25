'''
Created on 3/7/16
@author:   Chris Landolfi and Jordan Handwerger
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 6
'''
from cs115 import map, reduce
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def compressHelp1(S):
    """Returns the count for the how many times the first integer is consecutive"""
    if S == '':
        return 0
    elif len(S) == 1:
        return 1
    elif S[0] == S[1]:
        return 1 + compressHelp1(S[1:])
    else:
        return 1
    
def compressHelp2(S):
    """Returns a list of the values of the consecutive integers in succession"""
    if S == '':
        return []
    return [compressHelp1(S)] + compressHelp2(S[compressHelp1(S):])

def compressHelp3(L):
    """Breaks the numbers up so they are not larger than the maximum run length"""
    if L == []:
        return []
    if L[0] > MAX_RUN_LENGTH:
        L[0] = L[0] - MAX_RUN_LENGTH
        return [MAX_RUN_LENGTH, 0] + compressHelp3(L)
    return [L[0]] + compressHelp3(L[1:]) 

def add(x, y):
    """Returns x + y"""
    return x + y
    
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n == 0:
        return False
    elif n % 2 == 1:
        return True
    else:
        return False
    
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0: 
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + '1'
    else:
        return numToBinary(n // 2) + '0'

def binaryPadder(s):
    """Will return a binary number that is the correct bit length"""
    if len(s) >= COMPRESSED_BLOCK_SIZE:
        return s
    else:
        return binaryPadder('0'+s)
    
def compress(S):
    """Takes a binary string and returns a new binary string that is the input's run-to-length encoding"""
    if S == '':
        return ''
    elif S[0] == '1':
        return '0' * COMPRESSED_BLOCK_SIZE + reduce(add, map(binaryPadder, map(numToBinary, compressHelp3(compressHelp2(S)))))
    else:
        return reduce(add, map(binaryPadder, map(numToBinary, compressHelp3(compressHelp2(S)))))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return binaryToNum(s[0:-1]) *2 + int(s[-1])
    
def uncompressHelp(n, s):
    if s == '':
        return ''
    elif n == 1:
        return binaryToNum(s[:5]) * '1' + uncompressHelp(0, s[5:])
    elif n == 0:
        return binaryToNum(s[:5]) * '0' + uncompressHelp(1, s[5:])
def uncompress(S):
    """Returns S as the uncompressed version of itself""" 
    if S == '':
        return 0
    return uncompressHelp(0, S)

def compression(s):
    """Calculates the ratio of a compressed string vs a regular string"""
    return len(compress(s))/len(s)
