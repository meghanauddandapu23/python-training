'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i==n-1 or j==0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()