#Program to calculate the total cost of tickets depending on the choice of ticktes
class Tickets:
#defining a special method
        def __init__(self, Cell_Number, Ticket_Price, Number_of_tickets,):
            self.Cell_Number  = Cell_Number
            self.Ticket_Price = Ticket_Price
            self.Number_of_tickets = Number_of_tickets

#defining another special method
        def   calPreoayments(self):
             VAT = 15/100
             answer =  self.Ticket_Price * self.Number_of_tickets * VAT

#declaring statements
             if self.Ticket_Price == 40:
                 print("R", self.Ticket_Price)
                 print(self.Number_of_tickets,"tickets for Soccer  are booked")
                 print("For", self.Cell_Number)

             if self.Ticket_Price == 75:
                 print("R", self.Ticket_Price)
                 print(self.Number_of_tickets,"tickets for Movies are booked")
                 print("For", self.Cell_Number)

             if self.Ticket_Price == 100:
                 print("R", self.Ticket_Price)
                 print(self.Number_of_tickets,"tickets for the Theatre are booked")
                 print("For", self.Cell_Number)

objTicket =  Tickets(input("Enter your Cell_Number:\n")),  (input("What's the Ticket_price:\n")), (input("What's the Number_of_tickets:\n"))
objTicket.Tickets
