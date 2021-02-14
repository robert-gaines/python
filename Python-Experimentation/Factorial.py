#!/usr/bin/env python3

def DeriveFactorial(password):
    PasswordLength = len(password)
    print("[*] Password Length: %i " % PasswordLength)
    product = 1
    for i in range(1,PasswordLength):
        product = i * product
    print("[*] Factorial: %i " % product)
    return product

DeriveFactorial('password')
