import matplotlib.pyplot as plt
from colorama import Fore
print(Fore.RED +"............................Welcome you to Compound Interest calculator......................................")
starting_bal = float(input(Fore.GREEN +"Starting Balance :- "))
number_of_trade=float( input(Fore.CYAN +"Total Number of Trade/day :- "))
percent=float( input(Fore.CYAN +"Percent of profitable Trade :- "))
intrest_rate_pos = float( input(Fore.CYAN +"Interest Rate positve :- "))
intrest_rate_neg = float( input(Fore.CYAN +"Interest Rate negative :- "))
duration = float(input(Fore.YELLOW +"Duration :- "))
principal_graph = []

def actual_rate():
  
    final_rate = number_of_trade*(((percent) * (intrest_rate_pos)) - ((100-percent)*intrest_rate_neg))
    final_rate = float(final_rate/100)
    return final_rate



def compounding(sb,ir,du):
    principal=0
    principal = sb 
    print(Fore.RED+" Compunding started ")
    print(Fore.LIGHTWHITE_EX+" Interest Rate :- ",ir)
       
    for i in range(du):
        interest=  (principal)*ir/100
        interest = round(interest,2)
        principal = principal + interest
        principal =round(principal, 2)
        principal_graph.append(principal)
        print(Fore.GREEN+"interest:- ",interest,Fore.CYAN+ "  principal:- ",principal)
        
    return principal

time_du = []
# actual_rate()
duration = int(duration)
for i in range(duration):
    time_du.append(i+1)
result = compounding(starting_bal,actual_rate(),duration)          
print(Fore.MAGENTA+"total :- ",result) 

plt.bar(time_du, principal_graph,color='green')

for a,b in zip(time_du, principal_graph): 
    plt.text(a, b, str(b))

plt.title("calculation Plot", fontsize=28)
plt.ylabel("principal", fontsize=18)

plt.xlabel("time", fontsize=18)
# plt.show()  
