# -*- coding: utf-8 -*-
"""
=========================================================
PSET2: Problem 1
MITx 6.00.1x
=========================================================

This is a program for problem set 2, problem 1 of
MITx 6.00.1x

This program calculates the credit card balance
after one year if a person only pays the minimum monthly
payment required by the credit card company each month.

The following variables contain values as described
below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

At the end of 12 months, it will print out the remaining
balance with two decimal digits of accuracy.

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = 
(Minimum monthly payment rate) x (Previous balance)

Monthly unpaid balance =
(Previous balance) - (Minimum monthly payment)

Updated balance each month = 
(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Created on Wed Jun 19 18:26:22 2019

@author: Wishnuputra
=========================================================
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    unpaidBal = balance - balance*monthlyPaymentRate
    balance = unpaidBal + unpaidBal*annualInterestRate / 12
    
balance = round(balance, 2)
print("Remaining balance:", balance)