
# coding: utf-8

# Problem 1 :
# 
# Assume s is a string of lower case characters. Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5

# In[1]:

s='this is cincinnati'
count=0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': 
     count+=1
print('Number of vowels: '+str(count) )   


# Problem 2:
# 
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print Number of times bob occurs is: 2

# In[2]:

numberofbob=0
s='bobthkebobby'
for i in range(0,len(s)):
    a=s[i:(i+3)]
    if a =='bob':
        numberofbob +=1
print('Number of times bob occurs is: '+str(numberofbob) ) 


# Problem 3:
# 
# Assume s is a string of lower case characters. Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print Longest substring in alphabetical order is: abc

# In[3]:

mylist=[]
s = 'piipmbezplttfsu'
a=0
for a in range(0,len(s)-1):
    i=a
    while s[i]<=s[i+1]:
            i+=1 
            if i==len(s)-1:
                break
    mylist.append(str(s[a:i+1])  ) 
A=(sorted(mylist,key=len,reverse=True))
print('Longest substring in alphabetical order is: '+str(A[0]))

