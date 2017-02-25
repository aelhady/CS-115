'''
Created on Mar 27, 2016

@author: Christopher Landolfi

Pledge: I pledge my honor that I have abided by the Stevens Honor System

'''
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
    
def numToBase(N, B):
    """Converts N to a base B number"""
    if N == 0: 
        return ''
    else:
        return numToBase(N // B, B) + str(N % B)
    
def baseBToNum(S, B):
    """Returns S in base B"""
    if S == '':
        return 0
    else:
        return baseBToNum(S[0:-1], B) *B + int(S[-1])
    
def binaryPadder(s):
    """Will return a binary number that is the correct bit length"""
    if len(s) >= 8:
        return s
    else:
        return binaryPadder('0'+s)
    
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return binaryToNum(s[0:-1]) *2 + int(s[-1])
    
def flip(S): #Used to help convert an 8 bit number to a TC number
    """Returns S with all of the bits flipped"""
    if S == '':
        return ''
    if S[0] == '0':
        return '1' + flip(S[1:])
    else:
        return '0' + flip(S[1:])
    
def add(S, T):
    """Returns the addition of two binary strings in binary"""
    return numToBase(int(baseBToNum(S, 2) + baseBToNum(T, 2)), 2) 
    
def TcToNum(TcNum):
    """Converts an 8 bit number in two's-compliment and converts it to decimal"""
    if TcNum[0] == '1':
        return -1 * binaryToNum(flip(add(TcNum, '11111111'))[1:])
    else:
        return binaryToNum(TcNum)

def NumToTc(N):
    """Converts a base 10 number to a Two's-compliment number"""
    if N < 0:
        return add(flip(binaryPadder(numToBinary(N * -1))), '1')
    elif N > 127:
        return 'Error'
    else:
        return binaryPadder(numToBinary(N))

    

