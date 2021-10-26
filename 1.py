#gives caution
print("⚠️⚠️⚠️Please read the below text⚠️⚠️⚠️")

#asks user which password he wants to use
print("what passwords do you want to use? [please reply with low, mid or high for social media, personal or buisness respectively]")

#asks for the input
userinput = input('please enter -> ')

#low password
if userinput == "low":                                        #"low" user input
   import random                                              #imports of random(to randomise) and string(to group the letters)
   import string
   total = string.ascii_letters + string.digits               #total
   length = 8                                                 #determines the length
   password = "".join(random.sample(total, length))           #brings it all together
   print("Low level password. Commonly used for social media")#prints class
   print(password)                                            #prints password

#mid use input
elif userinput == "mid":                                       #"mid" user input
   import random
   import string
   total = string.ascii_letters + string.digits
   length = 10
   password = "".join(random.sample(total, length))
   print("Medium level password. Used for personal use")
   print(password)


#high input
elif userinput == "high":                                       #"high" user input
   import random
   import string
   total = string.ascii_letters + string.digits + string.punctuation
   length = 12
   password = "".join(random.sample(total, length))
   print("high level password used for buisness")
   print(password)

else:
   print('INVALID')

print("made by Magenta")                            #says creators name
