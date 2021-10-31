
# একটি সংখ্যা ইনপুট নিয়ে সেটা পজিটিভ , নেগেটিভ না শুন্য তা নির্ণয়ের প্রোগ্রাম |

num = float(input('Enter a number: '))
if(num >= 0):
    if(num==0):
        print('It is Zero')
    else:
        print('It is positive number')
else:
    print('It is a negative number')