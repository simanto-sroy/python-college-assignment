
# কেনো একটি পূর্ণসংখ্যা ইনপুট নিয়ে এটি মোলিক সংখ্যা কি না তা নির্ণয়ের প্রোগ্রাম |

number = int(input('Enter a number: '))

if(number > 1):
    for i in range(2, number):
        if(number % i) == 0:
            print(number, 'is not a prime number')
            break
        else:
            print(number, 'is a prime number')
else:
    print(number, 'is not a prime number')