class A:

    def one(self):

        return self.two()  

    def two(self):

        return '‘A’ ' 

class B(A):

    def two(self):

        return '‘B’'

obj2=B()

print(obj2.two())