#!/usr/bin/env python3 

def main():
    #
    print("[*] Flow control statements govern the exeuction pattern of a program")
    #
    print('''
            -> Boolean Data Types : evalue to True/False
            -> Comparison Operators:
                == - Equal
                != - Not Equal
                <  - Less
                >  - Greater
                <= - Less or Equal To
                >= - Greater or Equal To

            -> Logical Operators
               and
               or
               not
          ''')
    #
    valOne = int(input("[+] Enter an integer value-> "))
    #
    valTwo = int(input("[+] Enter an integer value-> "))
    #
    if(valOne == valTwo):
        #
        print("Values are Equal")
        #
    if(valOne != valTwo):
        #
        print("Values are not equivalent")
        #
        if(valOne < valTwo):
            #
            print("First value is less than second")
            #
        if(valOne > valTwo):
            #
            print("First value is greater than the second")
            #
        elif(valOne >= valTwo):
            #
            print("Value one is greater or equal to value two")
            #
        elif(valOne <= valTwo):
            #
            print("Value one is less than or equal to value two")
            #
    else:
        print("Comparisons of these values are not possible")

if(__name__ == '__main__'):
    #
    main()