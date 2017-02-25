'''
Created on Feb 17, 2016

@author: Christopher Landolfi
Pledge: I pledge my honor that I have abided by the Stevens Honor System
Chris J Landolfi
'''
def giveChange(amount, coins):
    """"Return the smallest amount of coins needed to reach amount with given coins"""
    if amount==0:
        return [0,[]]
    if coins==[]:
        return [float('inf'),[]]
    if coins[0]>amount:
        return giveChange(amount,coins[1:])
    use_it=giveChange(amount-coins[0],coins)
    use_it=[use_it[0]+1,use_it[1]+[coins[0]]]
    lose_it=giveChange(amount,coins[1:])
    if use_it[0]<lose_it[0]:
        return use_it
    return lose_it
scrabbleScores=[ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],      ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],      ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],      ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary=['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',               'spam', 'spammy', 'zzyzva']
def letterScore(letter, scorelist):
    '''Returns the score of a single given letter based on its value in scoreList'''
    if letter == scorelist[0][0]: #Checks if the letter is in the first pair
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:]) #When letter is not in the first pair it recursively calls the next pair

def combine(wordList,scoreList): 
    '''Returns a list of lists of each word and its associated score'''
    if wordList == [] or scoreList==[]: #Base case: list is empty is has associated all words with their score
        return []
    return [[wordList[0],scoreList[0]]]+combine(wordList[1:],scoreList[1:]) #recursive call

def wws_helper(scores):
    def wws_helper2(word):
        if word=='':
            return 0
        return letterScore(word[0], scores)+wws_helper2(word[1:])
    return wws_helper2
         
def wordsWithScore(dct, scores):
    """List of words in dct, with their Scrabble score"""
    return combine(dct, list(map(wws_helper(scores), dct)))

def take(n,L):
    """Return the list L[0:n]"""
    if n==0:
        return [L[0]]
    if L==[]:
        return []
    return [L[0]]+take(n-1,L[1:])

def drop(n,L):
    """Returns the list L[n:]"""
    if n==0:
        return L
    if L==[]:
        return []
    return drop(n-1,L[1:])
