print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=float(input("How much tip would you like to give ? 10%, 12%, or 15%? "))
people=float(input("How many people to split the bill? "))
if(tip==12):
    print(f"Each person should pay: {round(bill*1.12/people,2)}")
elif(tip==10):
    print(f"Each person should pay: {round(bill*1.10/people,2)}")
elif(tip==15):
    print(f"Each person should pay: {round(bill*1.15/people,2)}")
