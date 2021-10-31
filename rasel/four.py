
# দিনকে মাস ও দিনে পরিবর্তনের প্রোগ্রাম |

Days = int(input('Please enter the number of days: '))
Month = Days//30
Day = Days%30
print("Conversion of {0} Days = {1} Month and {2} Days".format(Days, Month, Day))