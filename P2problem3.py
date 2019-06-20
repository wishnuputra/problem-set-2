# -*- coding: utf-8 -*-
"""
=========================================================
PSET2 Problem 3 - Paying Debt Off In A Year
(Bisection Search)

MITx 6.00.1x
=========================================================

This program calculates the minimum fixed monthly payment
needed in order pay off a credit card balance within
12 months. By a fixed monthly payment, a constant amount
that will be paid each month.

This program uses bisection search to find the smallest
monthly payment to the cent (no more multiples of $10)
such that we can pay off the debt within a year. This
program runs much faster than the problem 2 which uses
linear search.

Lower and upeer bound for bisection search:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)) / 12.0

Created on Thu Jun 20 09:26:31 2019

@author: Wishnuputra
=========================================================
"""

balance = 999999
annualInterestRate = 0.18

cents = -0.01
remBal = balance
low = balance/12
high = (balance * (1 + annualInterestRate)) / 12.0

while True:
    ans = (high + low) / 2.0

    # calculate remaining balance after one year
    for i in range(12):
        unpaidBal = remBal - ans
        remBal = unpaidBal + unpaidBal*annualInterestRate / 12.0

    # check if the remaining balance has met the cents accuracy
    if  remBal < 0 and remBal > cents:
        break
    else:
        if remBal > 0:
            low = ans
        elif remBal < 0:
            high = ans
        remBal = balance

print("Lowest Payment:", round(ans, 2))