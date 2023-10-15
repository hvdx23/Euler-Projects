# euler 56
# largest sum for a^b where a,b <100
import math
import sys



def sumofdig(number):
    digit_sum=0
    for digit in str(number):
        digit_sum += int(digit)
    return digit_sum
def primal():
    maxdig=0
    for a in range(1, 100):
        for b in range(1, 100):
            product = a ** b
            digit_sum = sumofdig(product)
            if digit_sum>maxdig:
                maxdig=digit_sum
    return maxdig

large=primal()
print(large)