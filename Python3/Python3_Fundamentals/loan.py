# Get details of loan
money_owed = float(input("How much money do you owe, in dollars?\n")) # $50,000

apr = float(input("What is your annual percentage rate of the loan?\n")) # 3%

payment = float(input("How much will you pay off each month in dollars?\n")) # $1,000

months = int(input("How many months do you want to see the results for?\n")) # 24


monthly_interest_rate = apr/100/12
total_amount_of_interest = 0

for i in range(months):
    # Calculate interest to pay 
    interest_paid = money_owed*monthly_interest_rate

    # Add in interest
    money_owed = money_owed + interest_paid
    total_amount_of_interest = total_amount_of_interest + interest_paid

    if (money_owed - payment < 0):
        print(f"The last payment is {money_owed}")
        print(f"You paid the loan off in {i + 1} months.")
        print(f"The total amount of interest you paid was {total_amount_of_interest}")
        break
    # Make payment 
    money_owed = money_owed - payment

    print(f"Paid {payment}, of which {interest_paid} was interest. Now, I only owe {money_owed}")