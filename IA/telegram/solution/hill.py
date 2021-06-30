#!/usr/bin/python3
import string
from itertools import islice, cycle
import itertools
import numpy

def repeat(lst, times):
    return islice(cycle(lst), len(lst)*times)

def main():
    str_text="general aes-256-cbc key E5F040D82361F609C70A0E6D78294A13BE222EE389C1FEE4E41CAC28C4696EB5 iv 04ABC222D213CFA8AE548C866FA366D1 stop"
    str_cipher = ""
    i = 0
    dict_alpha = {}
    lst_clear = []
    lst_var = []
    for alpha in itertools.product(string.ascii_lowercase+string.digits+" "):
        dict_alpha.update({i:''.join(alpha)})
        i += 1
    print("Len:" + str(i) )
    i = 0
    print("The clear is: " +str_text)
    for char in str_text:
        for key,value in dict_alpha.items():
            if char == value:
                lst_var.append(key)
                i += 1
                if i != 0 and i%2 == 0:
                    lst_clear.append(lst_var) 
                    lst_var=[]
    if i%2 == 1:
        lst_var.append(0)
        lst_clear.append(lst_var)
        i += 1
    #if i%3 == 2:
    #    lst_var.append(0)
    #    lst_clear.append(lst_var)
    #    i = 0
    else:
        i = 0
    print(lst_clear)
    int_var = 0
    lst_mat = ((1,2),(0,3))
    #lst_mat = ((1,2),(0,3), (2,0))
    matrix_key = numpy.matrix(lst_mat)
    matrix_text = numpy.matrix(lst_clear)
    matrix_clear = numpy.transpose(matrix_text)
    matrix_cipher = numpy.dot(matrix_key, matrix_clear)
    matrix_cipher %= 37
    print(matrix_key)
    print(matrix_clear)
    print(matrix_cipher)
    for line in matrix_cipher.tolist():
        for i in line:
            for key,value in dict_alpha.items():
                if key == i:
                    str_cipher += value
    print("The cipher is: " + str_cipher)

if __name__=="__main__":
    main()
