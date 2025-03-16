product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.

class product:
    def __init__(self,code = 50,name = 'codetree'):
        self.code = code
        self.name = name

    def p(self,code = 50,name = 'codetree'):
        print(f'product {self.code} is {self.name}')

a = product()
b = product(product_code,product_name)

a.p()
b.p()
    