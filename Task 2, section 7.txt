from datetime import datetime, timedelta

str_fname= input("Enter your first name:\n")
str_lname= input("Enter your last name:\n")
str_mark1= int(input("Enter first mark:\n"))
str_mark2= int(input("Enter second mark:\n"))
str_mark3= int(input("Enter third mark:\n"))
Average= (str_mark1 + str_mark2 + str_mark3) /3

def ten_dates(t):

    import datetime

dt = datetime(2020, 0o3, 20, 12, 00, 00)
add_dt = dt + timedelta(days=14)
print(add_dt.strftime("%d-%m_%Y %H:%M:%S"))

if Average >= 50:
    print("You have made it through to the next round.")

if Average <= 50:
    print("You have, unfortunately not made it through.")

