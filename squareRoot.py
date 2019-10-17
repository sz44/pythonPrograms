val = input('enter a number:')
val = int(val)
#compute approximate square root of input number
x, a = 0, 1

while x*x != val:
    print(x)
    oldX = x
    if x*x < val:
         x += a
    if oldX == x:
        break
    if x*x > val:
         x -= a
         a /= 10
    print(x)
#
#
# 1. check if the current x when squared is under the input value
# 2. if it is add to it (starting with a=1)
# 3. check if we are stuck, reached the limited of the number of float digits python can show
# 4. if we did than we cannot do more accurate so end the program
# 5. check if the current x when squared is over the input value
# 6. if it is, remove the prevous a that made us go over, and divide a by 10
#    so that now we are adding decimals to the number

# another way to stop: decide the accurace the number of digits to show,
# the smallest a value, and just break when we come to it.

