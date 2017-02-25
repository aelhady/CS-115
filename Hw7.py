'''
Created on Mar 13, 2016

@author: Christopher Landolfi

Pledge: I pledge my honor that I have abided by the Stevens Honor System.
'''
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
    


def baseToBase(B1, B2, SinB1):
    """SinB1 is a string of integers in B1 and the function returns a string representing a number in B2"""
    return numToBase(int(baseBToNum(SinB1, B1)), B2) 


def add(S, T):
    """Returns the addition of two binary strings in binary"""
    return numToBase(int(baseBToNum(S, 2) + baseBToNum(T, 2)), 2) 



FullAdder = { ('0','0','0') : ('0','0'), ('0','0','1') : ('1','0'), ('0','1','0') : ('1','0'),('0','1','1') : ('0','1'), ('1','0','0') : ('1','0'), ('1','0','1') : ('0','1'), ('1','1','0') : ('0','1'), ('1','1','1') : ('1','1') }

def carry(s, t): #Calculates the carry of the addition of two binary numbers to be used in the dictionary search
    """Returns the carry of the addition of s and t in binary"""
    if s =='' or t == '':
        return '0'
    elif s == '0' or t == '0':
        return '0'
    else: 
        return '1'

def addB(S, T):
    """Returns the addition of two binary strings in binary"""
    if S == '':
        return T
    if T == '':
        return S
    else:
        return addB(S[:-1], T[:-1]) + FullAdder[S[-1], T[-1], carry(S[-1], T[-1])][0]

    
    