def customer_eligibility():
    salary = float(input("Enter your salary: "))
    loan_amount = float(input("Enter loan amount: "))
    
        #check if the is eligible
    if salary >= 30000 and loan_amount <= salary * 10:
        print("Eligable to loan!")
        months = int(input("months "))

        #calculation
        loan_interest = loan_amount * 1.10
        monthly_payment = loan_interest / months
        
        print(f"Your loan interest with 10%: {loan_interest:.2f}")
        print(f"Your monthy payment is: {monthly_payment:.2f}")

        #if the customer is not eligible
    else:
         if salary < 30000:
            print("Not eligable to loan!")
         if loan_amount > salary *10 :
            print("Requested loan is too high!")




customer_eligibility()
