class A:
    def show(self):
        print("Hello from class A")

class B(A):
    def display(self):
        print("Hello from class B")

class C(B):
    def greet(self):
        print("Hello from class C")

# Usage
obj = C()
obj.show()      # Inherited from A
obj.display()   # Inherited from B
obj.greet()     # Defined in C