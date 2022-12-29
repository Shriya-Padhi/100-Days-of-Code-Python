print("Welcome to the tip calculator!")
#Input values from user
tot_bill=input("What was the total bill? $")
tip=input("How much tip would you like to give? 10, 12, or 15?")
no_people=input("How many people to split the bill?")
#Type conversion
float_tot_bill = float(tot_bill)
int_tip = int(tip)
int_no_people= int(no_people)
#Calculate tips
if(tip=="10"):
  bill_after_tip=float_tot_bill*(10/100)
elif(tip=="12"):
  bill_after_tip=float_tot_bill*(12/100)
elif(tip=="15"):
  bill_after_tip=float_tot_bill*(15/100)
else:
  print("Error! Please enter correct tip %")
  exit()
#Create bill for per person
bill_including_tip = float_tot_bill + bill_after_tip
bill_per_person = bill_including_tip / int_no_people
final=round(bill_per_person,2)
print(f"Each person should pay: ${final}")