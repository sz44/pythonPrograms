# convert integer to binery
n = int(input("enter an interger 0 - 1023:"))
b = ""

if n > 1023:
    print("too large")
# 2**9 = 512
if n >= 511:
    b += "1"
    n -= 512
else:
    b += "0"
# 2**8 = 256
if n >= 256:
    b += "1"
    n -= 256
else:
    b += "0"
# 2**7 = 128
if n >= 128:
    b += "1"
    n -= 128
else:
    b += "0"

if n >= 64:
    b += "1"
    n -= 64
else:
    b += "0"

if n >= 32:
    b += "1"
    n -= 32
else:
    b += "0"

if n >= 16:
    b += "1"
    n -= 16
else:
    b += "0"
if n >= 8:
    b += "1"
    n -= 8
else:
    b += "0"

if n >= 4:
    b += "1"
    n -= 4
else:
    b += "0"

if n >= 2:
    b += "1"
    n -= 2
else:
    b += "0"

if n >= 1:
    b += "1"
    n -= 1
else:
    b += "0"

print (b)
