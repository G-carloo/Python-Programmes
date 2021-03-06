#Defining hotel costs
def hotel_cost(nights):
    return 140 * nights

#defining  a plane ride cost
def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city =="JHB":
        return 2000
    else:
        return 1800


#defining rental_car_cost
#calculating the cost to rent a car depending on how long the use rents it for
def rental_car_cost(days):

    rental_cost= 40 # per day
    seven_days_discount = 50 # if you rent the car for 7 day or more
    three_days_discount = 20 # if you rent the car for 3 days or more

    rental_cost = rental_cost * days

    if days >= 7:
        rental_cost = 40 * days - seven_days_discount
    elif 3 <= days < 7:
        rental_cost = 40 * days - three_days_discount

    return rental_cost


#defining trip_cost
def trip_cost(days, nights, city, spending):
    return rental_car_cost(days) + hotel_cost(nights) + plane_ride_cost(city) + spending_money(spending)

num_of_days = int(input("How many days will you be staying at our hotel?: \n"))
city_travelling_to = input(
                              "Which city are you travellng to. The options are sensitive:"
                              " \nCape Town\nDurban\nJHB\nBFN\nPlease type in your destination city!\n "
                            )



spent_money = float(input("Your room service is?: \n" ))
spending_money = float(input("What is your budget?: "))

print(
        "The total costs for your vacation is: R ",
        trip_cost(city_travelling_to, num_of_days, spent_money, spending_money),
        "Thanks for being with us :)"
            )