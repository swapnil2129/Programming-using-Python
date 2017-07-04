
# coding: utf-8

# # 1
# Write a function is_triangular that meets the specification below. A triangular number is a number obtained by the continued summation of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

# In[32]:

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    return (-1+abs((1+8*k)**0.5))%2==0
        


# In[47]:

is_triangular(6)


# # 2
# Write a Python function that takes in a string and prints out a version of this string that does not contain any vowels, according to the specification below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.
# 
# For example, if s = "This is great!" then print_without_vowels will print Ths s grt!. If s = "a" then print_without_vowels will print the empty string .

# In[49]:

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    a=""
    for i in s:
        if i not in ["a",'e','i','o','u',"A",'E','I','O','U']:
            a+=i
    print(a)        
        


# In[50]:

s="This is kuldip"
print_without_vowels(s)


# # 3
# Write a function that satisfies the following docstring:
# 
# def largest_odd_times(L):
# 
#       """
#         Assumes L is a non-empty list of ints
#     
#         Returns the largest element of L that occurs an odd number 
#         
#         of times in L. If no such element exists, returns None
#         """
#         
#     
# For example, if
# 
# largest_odd_times([2,2,4,4]) returns None
# 
# largest_odd_times([3,9,5,3,5,3]) returns 9

# In[150]:

def largest_odd_times(L):
    A=[]
    for i in L:
        count=L.count(i)
        if count%2 !=0:           
            A.append(i)
    if not A:
        return (None)
    else:
        return (max(A))
L=([2,2,4,4,10,11,11,11,11,11])
largest_odd_times(L)              


# # 4
# 
# Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary.
# 
# The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list (increasing order) of all keys in d that have the same value in d.
# 
# Here are two examples:
# 
# If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
# 
# If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
# 
# If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}

# In[151]:

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''

    revdict = {}
    for k, v in d.items():
        revdict.setdefault(v, []).append(k)
    return revdict
d = {4:True, 2:True, 0:True}
dict_invert(d)


# # 5
# Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗10 ^3+2∗10^2+3∗10^1+4∗10^0.

# In[183]:

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def result(x):
        reverse=L[::-1]
        sum=0
        for i in reverse:
            sum+=i*(x)**(reverse.index(i))
        return(sum)
    return (result(x))  
L=[1,2,3,4]
x=10
general_poly (L)


# # 6
# 
# Write a Python function that takes in two lists and calculates whether they are permutations of each other. The lists can contain both integers and strings. We define a permutation as follows:
# 
# the lists have the same number of elements
# 
# list elements appear the same number of times in both lists
# 
# If the lists are not permutations of each other, the function returns False. 
# 
# If they are permutations of each other, the function returns a tuple consisting of the following elements:
# 
# the element occuring the most times
# 
# how many times that element occurs
# 
# the type of the element that occurs the most times
# 
# If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times, you can return any of them.

# In[220]:

L1=[1, 'b', 1, 'c', 'c', 1]
L2=['c', 1, 'b', 1, 1, 'c']
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    a=[str(s) for s in L1] 
    b=[str(i) for i in L2] 
    a.sort()
    b.sort()
    if a!=b:
        return (False)
    else:
        tup=max(set(L1), key=L1.count)
        times=L1.count(tup)
        answer=(tup,times,type(tup))
        return answer

is_list_permutation(L1, L2)  

