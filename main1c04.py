joke = input("*Knock knock*\n Whose there? ")
print(joke+" who?")
  
#message = "strings are immutable"
#message[0] = 'p'
#print(message) 

a = "this sentence should go second"
b = "this sentance should go first"

c=a
a=b
b=c

print(a)
print(b)