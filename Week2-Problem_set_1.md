
Problem 1:

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41



```python
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

count=1
while count<13:
    A=balance-(balance*monthlyPaymentRate)
    RB=(A+A*(annualInterestRate/12))
    
    balance=RB
    count+=1
final=round(RB,2)    
print('Remaining balance: '+str(final))
```

    Remaining balance: 31.38
    

Problem 2:

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


```python
balance = 3926
annualInterestRate = 0.2
i=0
while balance>0:
    payment=balance
    
    count=1
    while count<13:
            A=payment-(i)
            RB=(A+A*(annualInterestRate/12))
            payment=RB
            count+=1
       
    if payment<=0:
        break
    else:
        i+=0.01
print(round(i,2))
```

    357.73
    

Problem 3

Monthly interest rate = (Annual interest rate) / 12.0

Monthly payment lower bound = Balance / 12

Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year



```python
balance = 461092
annualInterestRate = 0.18
low=(balance/12)

high=(balance*(1+(annualInterestRate/12))**12)

payment=balance

while annualInterestRate>0:
    
    if payment in (-0.01,0.01):
        
        break
        
    payment=balance
    
    count=1
    
    i=(high+low)/2
    
    while count<13:
        
            A=payment-(i)
            
            RB=(A+A*(annualInterestRate/12))
            
            payment=round(RB,2)
            
            count+=1 
            
    if payment in (-0.01,0.01):
        
        print(round(i,2))
        
    elif payment>0.01:
        
        low=i   
        
    else:
        
        high=i
        
    i=(high+low)/2
    
```

    41648.19
    

Recursive Approach


```python
balance = 461092
annualInterestRate = 0.18
low=(balance/12)

high=(balance*(1+(annualInterestRate/12))**12)

i=(high+low)/2

def emi(balance,annualInterestRate,high,low):
    
        count=1
        
        i=(high+low)/2
        
        payment=balance
        
        while count<13:
            
            A=payment-i
            
            RB=(A+A*(annualInterestRate/12))
            
            payment=round(RB,3)
            
            count+=1
            
        if payment in (-0.01,0.01):
            
            return round(i,2)
        
        elif payment<-0.01:
            
            high=i
            
            return emi(balance,annualInterestRate,i,low)
        
        else:
            
            low=i
            
            return emi(balance,annualInterestRate,high,i)
        
emi(balance,annualInterestRate,high,low)
    

```




    41648.19




```python

```
