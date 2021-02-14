#!/usr/bin/env python3

import os

def DeriveFactorial(password):
    PasswordLength = len(password)
    print("[*] Password Length: %i " % PasswordLength)
    product = 1
    for i in range(1,PasswordLength):
        product = i * product
    print("[*] Factorial: %i " % product)
    return product

def GenerateGuesses(password):
    password_dictionary = {}
    result = {}
    i = 0
    for p in password:
        password_dictionary[i] = p
        i += 1
    characters = [
                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    '0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=','|','/',
                    '\\','?','<','>',',',"'",':',';','{','}','[',']','"'
                 ]
    password_factorial = DeriveFactorial(password)
    password_guesses = 0
    while(password_guesses <= password_factorial):
        resolution_index = 0
        for p in password_dictionary.values():
            if(p.isupper() and p.isalpha()):
                for c in characters:
                    print("[*] Comparing: %s:%s" % (p,c))
                    os.system('cls')
                    password_guesses += 1
                    if(p == c.upper()):
                        result[resolution_index] = c.upper()
                        resolution_index += 1
            else:
                for c in characters:
                    print("[*] Comparing: %s:%s" % (p,c))
                    os.system('cls')
                    password_guesses += 1
                    if(p == c):
                        result[resolution_index] = c
                        resolution_index += 1

        if(len(result.values()) == len(password)): break
    result_plaintext = ''
    for r in result.values():
        result_plaintext += r
    print("[*] Total Guesses: %i " % password_guesses)
    print("[*] Password value: %s " % result_plaintext)

def main():
    print("[*] Simple Password Cracker")
    print("---------------------------")
    print()
    password = input("[*] Enter the password-> ")
    GenerateGuesses(password)

if(__name__ == '__main__'):
    main()
