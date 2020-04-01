#listing variables
str_speed=int(input("What was your speed:\n "))
str_speedlimit=int(input("What was the allowed speed:\n "))
points=(str_speed - str_speedlimit)/5

#declaring statements
if str_speed <= str_speedlimit:
    print("OK, Keep it up, but not too up ;)")

if str_speed >= str_speedlimit:
    print("Slowdown Nigga, before your legs cramps")

if str_speed >= str_speedlimit :
    print("points:",points)

if points >= 12:
    print("Time to go to jail")
