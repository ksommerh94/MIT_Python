# Write a program to calculate the best savings rate, as a function of your starting salary.
# You should use bisection search to help you do this efficiently. You should keep track of the number of
# steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote
# for part B in this problem.
import numpy

semi_annual_raise=0.07
r=0.04
total_cost=1000000
cost_down_payment=total_cost*0.25
month=36
epsilon=100

annual_salary=float(input("Enter the starting salary: "))

step_search=0

low=0
high=1
guess=(low+high)/2

costDownPayment=total_cost*portion_down_payment
#monthly
while(abs(cost_down_payment-current_savings)<epsilon):
    current_savings=0
    monthly_savings=(annual_salary/12)*guess
    for i in range (36):
        if month%6==0 and month!=0:
            annual_salary+=annual_salary*semi_annual_raise
            monthly_savings=(annual_salary/12)*guess
        current_savings+=current_savings*r/12
        current_savings+=monthly_savings






    #print (current_savings)
print("Number of months: " + str(month))
