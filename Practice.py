# creating a class
class Salaries:
    def __init__(self, net_mon_sal, gross_mon_sal, perc_tax):
        self.net_mon_sal = net_mon_sal
        self.gross_mon_sal = gross_mon_sal
        self.perc_tax = perc_tax

# defining funcitons
def n_m_s():
    answer = Emp_Ann_Sal * p_t
    return answer

def g_m_s():
     answer = Emp_Ann_Sal //12
     return answer

def p_t():
     answer = input(Emp_Work)
     return answer

#Listing variables
Emp_Ann_Sal = input("Please enter your Annual Salary.:\n")
Emp_Work = input("Do you work Full_time or Part_time?:\n")
Full_time = 0.295
Part_time = 0.25

#running
objn = (n_m_s())
objg = (g_m_s())
objp = (p_t())
print(objn, objg, objp)
