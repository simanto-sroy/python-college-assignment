
# n সংখ্যার যোগফল নির্ণয়ের প্রোগ্রাম |

n = int(input('Enter a number: '))
if(n < 0):
    print('Enter a positive Number')
else:
    sum = 0
    while(n > 0):
        sum += n
        n -= 1
        print('The sum is =' ,sum)