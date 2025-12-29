'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def kk(nums):
    k=[]
    s=""
    for num in nums:
        s+=str(num)
    i=int(s)+1
    z=str(i)
    for ch in z:
        k.append(int(ch))
    print(k)
nums=[9,9,9]
kk(nums)