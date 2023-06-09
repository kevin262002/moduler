import datetime

print("Date & Time : ",datetime.datetime.now())
print("Year : ", datetime.date.today().strftime("%Y"))
print("Month of Year : ", datetime.date.today().strftime("%B"))
print("Week Number of the Year : ", datetime.date.today().strftime("%U"))
print("Weekday of the Week : ", datetime.date.today().strftime("%u"))
print("Day of Year : ", datetime.date.today().strftime("%j"))
print("day of the Month : ", datetime.date.today().strftime("%d"))
print("Day of Week : ", datetime.date.today().strftime("%A"))
