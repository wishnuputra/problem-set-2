# -*- coding: utf-8 -*-
"""
=========================================================
PSET2 Problem 2 - Paying Debt Off In A Year
MITx 6.00.1x
=========================================================

This program calculates the minimum fixed monthly payment
needed in order pay off a credit card balance within
12 months. By a fixed monthly payment, a constant amount
that will be paid each month.

In this problem, we will not be dealing with a minimum
monthly payment rate.

The following variables contain values as described
below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest
monthly payment that will pay off all debt in under
1 year, for example:
    
Lowest Payment: 180

Assume that the interest is compounded monthly according
to the balance at the end of the month (after the payment
for that month is made). The monthly payment must be a
multiple of $10 and is the same for all months. Notice
that it is possible for the balance to become negative
using this payment scheme, which is okay. A summary of
the required math is found below:

Monthly interest rate =
(Annual interest rate) / 12.0

Monthly unpaid balance =
(Previous balance) - (Minimum fixed monthly payment)

Updated balance each month =
(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)    

Created on Wed Jun 19 19:30:59 2019

@author: Wishnuputra
=========================================================
"""

balance = 320000
annualInterestRate = 0.2

remBal = balance
fixedPayment = 10

while remBal > 0:
    for i in range(12):
        unpaidBal = remBal - fixedPayment
        remBal = unpaidBal + unpaidBal*annualInterestRate / 12
    if remBal > 0:
        fixedPayment += 0.01
        remBal = balance

print("Lowest Payment:", fixedPayment)