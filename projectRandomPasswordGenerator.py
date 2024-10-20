import random
import string

passwordLength = 8
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension
value = "".join([random.choice(charValues) for i in range(passwordLength)])
print("Random password is: ", value)

# password = ""
# for i in range(passwordLength):
#     password += random.choice(charValues)

# print("Random password is: ", password)