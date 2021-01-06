#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:38:32 2021

@author: Maks Fraszka

A simple function calculating monthly mortgage payment based on principal,
interest rate, and years.

"""

def calc_mortg():
    print('Hello, welcome to your Mortgage Calculator!\n')
    p = int(input('Enter the principal loan amount: '))
    r = int(input('Enter your annual interest rate: '))
    f = int(input('Enter the number of years of fixed mortgage: '))
    n = int(f)*12
    M = p*(((r/100)/12)*((1+((r/100)/12))**n))/(((1+((r/100)/12))**n)-1)
    print('\nYour total monthly mortgage payment is $',round(M,2))