import matplotlib.pyplot as plt
from colorama import Fore
import math
print(Fore.RED +"............................Welcome you to RSM's calculator......................................")


var1 = int(input(Fore.CYAN +"Press" +Fore.GREEN +" 0 "+ Fore.CYAN +"for duration"+Fore.GREEN + " 1 " + Fore.CYAN +"for Interest rate "+Fore.GREEN + " 2 " + Fore.CYAN+" for Starting Balance :- " +Fore.GREEN))


if(var1 == 0):
    starting_bal = int(input(Fore.GREEN +"Starting Balance :- "))
    expected_intrest_rate=float( input(Fore.CYAN +"Expected Interest Rate :- "))
    target  = int(input(Fore.LIGHTGREEN_EX +"Target :- " ))
    var2 = int(input(Fore.CYAN +"Press" +Fore.GREEN +" 0 "+ Fore.CYAN +"for simple"+Fore.GREEN + " 1 " + Fore.CYAN +"for Compound :- "+Fore.GREEN))
    if(var2==0):
        time = target * 100/(expected_intrest_rate * starting_bal )
        print(Fore.LIGHTBLACK_EX+"time Period :- ",time)
    if(var2==1):
        # time = target * 100/(expected_intrest_rate * starting_bal )
        t = (math.log(target/starting_bal,10)) / (math.log((1 + (expected_intrest_rate/100)),10))
        t = round(t,2)
        print(Fore.LIGHTMAGENTA_EX+"time Period :- ",t)
        
elif(var1 == 1):
    starting_bal = int(input(Fore.GREEN +"Starting Balance :- "))
    target  = int(input(Fore.LIGHTGREEN_EX +"Target :- " ))
    duration = int(input(Fore.YELLOW +"Duration :- "))
    var2 = int(input(Fore.CYAN +"Press" +Fore.GREEN +" 0 "+ Fore.CYAN +"for simple"+Fore.GREEN + " 1 " + Fore.CYAN +"for Compound :- "+Fore.GREEN))
    if(var2==0):
        inter = target * 100/(duration * starting_bal )
        print(Fore.LIGHTBLACK_EX+"Interest :- ",inter)
    if(var2==1):
        # time = target * 100/(expected_intrest_rate * starting_bal )
        inter = (pow(target/starting_bal,1/duration)) - 1
        inter = round(inter*100,2)
        print(Fore.LIGHTMAGENTA_EX+"Interest :- ",inter)
elif(var1 == 2):
    duration = int(input(Fore.YELLOW +"Duration :- "))
    expected_intrest_rate=int( input(Fore.CYAN +"Expected Interest Rate :- "))
    target  = int(input(Fore.LIGHTGREEN_EX +"Target :- " ))
    var2 = int(input(Fore.CYAN +"Press" +Fore.GREEN +" 0 "+ Fore.CYAN +"for simple"+Fore.GREEN + " 1 " + Fore.CYAN +"for Compound :- "+Fore.GREEN))
    if(var2==0):
        bal = target * 100/(duration * duration )
        print(Fore.LIGHTBLACK_EX+"Starting Balance :- ",bal)
    if(var2==1):
        # time = target * 100/(expected_intrest_rate * starting_bal )
        bal = target/(pow(1+expected_intrest_rate/100,duration))
        bal = round(bal,2)
        print(Fore.LIGHTMAGENTA_EX+"Starting Balance :- ",bal)
else:
    raise Exception("write correct input")
    
principal_graph = []

# def compounding(sb,ir,du):
#     principal=0
#     principal = sb 
#     for i in range(du):
#         interest=  (principal)*ir/100
#         interest = round(interest,2)
#         principal = principal + interest
#         principal =round(principal, 2)
#         principal_graph.append(principal)
#         print(Fore.GREEN+"interest:- ",interest,Fore.CYAN+ "  principal:- ",principal)
        
#     return principal
