#!/usr/bin/env python3

def print_fibonacci(length):
    my_list=[0,1]
    pass
    if(length==0):
        my_list=[]
    elif(length==1):
        my_list=[0]
    else:
        for i in range(length-2):
           my_list.append(my_list[i+1]+my_list[i]) 
    
    print(my_list)
        
            