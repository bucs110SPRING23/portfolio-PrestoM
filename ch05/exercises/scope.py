def mult(num1, num2):
    product = 0
    for i in range(num2):
        product += num1
    return product

def powa(num, expo):
    result = 1
    for i in range(expo):
        result *= num
    return result

def square(num):
    return powa(num, 2)

print(mult(5,4))
print(powa(2,3))
print(square(7))