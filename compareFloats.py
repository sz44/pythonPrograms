a = 12.001 - 12
b = 102.001 - 102
# check if a and b are equal.
diff = b - a
print("diff: ", diff)
if diff < 0:
    diff = -diff
if diff < 0.00000000001:
    print("same")
else:
    print("different")
