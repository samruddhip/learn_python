class Person:
    __name = "anobjhbc"

    def __hello():
        print("Hello, I am", Person.__name)

p1 = Person()
print(p1.__name)  # AttributeError: 'Person' object has no attribute '__name'