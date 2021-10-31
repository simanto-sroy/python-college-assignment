
# তিনিটি সংখ্যার মধ্যে বৃহতম সংখ্যাটির নির্ণয়ের প্রোগ্রাম |

num_one = float(input("Enter first number: "))
num_two = float(input("Enter second number: "))
num_three = float(input("Enter third number: "))

if(num_one >= num_two) and (num_one >= num_three):
    largest = num_one
elif(num_two >= num_one) and (num_two >= num_three):
    largest = num_two
else:
    largest = num_three

print('The largest number among', num_one, num_two,'and',num_three, 'is = ',largest)
