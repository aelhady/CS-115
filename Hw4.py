'''
Created on Feb 19, 2016

@author: Christopher Landolfi
Pledge: I pledge my honor that I have abided by the Stevens Honor System 
'''
def pascal_add(lst):
    """Returns the list of sums by adding the adjacent terms of a row in pascal's triangle"""
    if lst==[]:
        return []
    if len(lst)==1:
        return [1]
    return [lst[0]+lst[1]]+pascal_add(lst[1:])

def pascal_row(num):
    """Returns the list of numbers as they would appear in num row of a pascal's triangle"""
    if num==0:
        return [1]
    if num==1:
        return [1,1]
    return [1]+pascal_add(pascal_row(num-1))
def pascal_triangle(num):
    """Returns a list a list of lists with each list being a row of pascal's triangle including row num"""
    if num==0:
        return [1]
    if num==1:
        return [[1],[1,1]]
    return pascal_triangle(num-1)+[pascal_row(num)]
