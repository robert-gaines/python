#!/usr/bin/env python3

def main():
    #
    print("Expressions = Values + Operators")
    #
    valOne = input("[+] Enter an integer value-> ")    
    #
    valTwo = input("[+] Enter an integer value-> ")
    #
    opr = input("[+] Enter an integer operator-> ")
    #
    print("[*] Expression: %s %s %s" % (valOne,opr,valTwo))    
    #
    print("Data type -> A category of values")

    print('''
            < Some Data Types >
            -------------------
            String - Text
            Numeric - Integer/Float
          ''')
    #
    print("[*] Variables contain values...")
    #
    print("[*] Variables established via assignment statements")
    #
    print("[*] Format: variable = value")
    #
    print("[*] Statement -> expression that does not evaluate ")
    #
    return

if(__name__ =='__main__'):
    #
    main()