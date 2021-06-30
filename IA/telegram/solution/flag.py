#!/usr/bin/python2.7
flag="067089066069082084070123073095076048086095073052095067089066051082125"
parsed_flag = ''.join([chr(int(flag[i:(i + 3)])) for i in range(0, len(flag), 3)])
print parsed_flag
