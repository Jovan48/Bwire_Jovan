class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):  # Multiple inheritance
    pass

# Test
d = D()
d.greet()  # Will follow MRO: D -> B -> C -> A

# Print MRO
print(D.__mro__)
