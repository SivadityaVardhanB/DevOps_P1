import random

a = random.randint(1, 10000)
b = random.randint(1, 10000)
c = a+b

with open('.\Pyhton_app\Result.txt', 'w') as result:
    result.write("Sum of {A} + {B} is = {C}".format(A=a, B=b, C=c))

print("Sum of {A} + {B} is = {C}".format(A=a, B=b, C=c))