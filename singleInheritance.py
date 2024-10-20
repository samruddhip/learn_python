class A:
    varA = "I am A"

class B:
    varB = "I am B"

class C(A, B):
    varC = "I am C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)