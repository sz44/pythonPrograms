n =int(input("add 2**0 to 2**n, enter n:"))
total = 0

"""
while n>=0:
    total += 2**n
    n -= 1
"""

for i in range(n,-1,-1):
    total += 2**i

print(total)
#1,2,4,8,16,32,64,128,256,512,1024
# 11 bits (1 byte + 3 bits)
# 2**0 + 2**1 + ... + 2**8 = ?


