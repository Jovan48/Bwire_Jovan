class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Test
animal = Animal()
animal.sound()  # Output: Some generic animal sound

dog = Dog()
dog.sound()     # Output: Bark (overridden)
