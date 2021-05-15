#! /usr/bin/env python

num = int(input("input a number to find sum upto that number : "))
sum = 0
while num>0:
  sum = sum+num
  num = num-1
print("Sum = " + str(sum))
