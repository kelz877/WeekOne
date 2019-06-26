

#Ask the user for the two inputs

#Enter the total amount
total_bill = input("Please enter the total amount of your bill: ")


#Enter the tip percentage amount

tip_percentage = input("Please enter the percentage you would like to tip: ")


#After the user has entered both inputs, the application calculates 
#the tip amount and displays it to the user



def tip_amount(total, tip):
    tip_value = int(tip) * .01
    result = (tip_value) * int(total)
    return result



#non function
tip_amount = tip_amount(total_bill, tip_percentage)
print(tip_amount)



total_amount = float(input("Enter total amount: "))
tip = float(input("Enter tip"))

total = tip*.01 * total_amount
print(total)