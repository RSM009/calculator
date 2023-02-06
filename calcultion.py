import matplotlib.pyplot as plt
import colorama
from colorama import Fore
print(Fore.RED +"............................Welcome you to Compound Interest calculator......................................")
starting_bal = float(input(Fore.GREEN +"Starting Balance :- "))
#monthly_contri =float(input   ("Monthly Contribution(optional):- "))
intrest_rate=float( input(Fore.CYAN +"Interest Rate :- "))
duration = int(input(Fore.YELLOW +"Duration :- "))
principal_graph = []

def compounding(sb,ir,du):
    principal=0
    principal = sb 
    for i in range(du):
        interest=  (principal)*ir/100
        interest = round(interest,2)
        principal = principal + interest
        principal =round(principal, 2)
        principal_graph.append(principal)
        print(Fore.GREEN+"interest:- ",interest,Fore.CYAN+ "  principal:- ",principal)
        
    return principal
time_du = []
for i in range(duration):
    time_du.append(i+1)
result = compounding(starting_bal,intrest_rate,duration)          
print(Fore.MAGENTA+"total :- ",result) 

plt.bar(time_du, principal_graph,color='green')

for a,b in zip(time_du, principal_graph): 
    plt.text(a, b, str(b))

plt.title("calculation Plot", fontsize=28)
plt.ylabel("principal", fontsize=18)

plt.xlabel("time", fontsize=18)
#plt.show()  
