# Write a program to calculate the best savings rate, as a function of your starting salary.
# You should use bisection search to help you do this efficiently. You should keep track of the number of
# steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote
# for part B in this problem.

semi_annual_raise=0.07
r=0.04
total_cost=1000000
cost_down_payment=total_cost*0.25
month_initial=36
epsilon=100
current_savings=0


annual_salary_static=float(input("Enter the starting salary: "))

step_search=0

low=0
high=1
guess=(low+high)/2


rate_month=((r+1)**(1/12))-1


annual_salary=annual_salary_static
monthly_savings=(annual_salary/12)
for month in range (month_initial):
    if month%6==0 and month!=0:
        annual_salary+=annual_salary*semi_annual_raise
        monthly_savings=(annual_salary/12)*(1+rate_month)
    current_savings+=current_savings*rate_month
    current_savings+=monthly_savings
if current_savings<cost_down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while(abs(cost_down_payment-current_savings)>epsilon):
        annual_salary=annual_salary_static
        current_savings=0
        guess=(low+high)/2
        monthly_savings=(annual_salary/12)*guess

        for month in range (month_initial):
            if month%6==0 and month!=0:
                annual_salary+=annual_salary*semi_annual_raise
                #monthly_savings=(annual_salary/12)*(1+rate_month)
                monthly_savings=(annual_salary/12)*guess
            current_savings+=current_savings*rate_month
            current_savings+=monthly_savings

        if cost_down_payment<current_savings:
            high=guess
        else:
            low=guess
        step_search+=1

    print("Best savings rate: " + str(round(guess, 4)))
    print("Steps in bisection search: " + str(step_search))
