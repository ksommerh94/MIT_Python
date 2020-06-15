import numpy
import pylab

from matplotlib import pylab
from pylab import *

# initial variables
annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semi­annual raise, as a decimal: "))

#for testing
# annual_salary=80000
# portion_saved=.1
# total_cost=800000
# semi_annual_raise=.03


monthly_savings=(annual_salary/12)*portion_saved
#print(monthly_savings)
portion_down_payment=0.25
r=0.04


costDownPayment=total_cost*portion_down_payment
month=0
current_savings=0
#monthly
while(current_savings<costDownPayment):
    if month%6==0 and month!=0:
        annual_salary+=annual_salary*semi_annual_raise
        monthly_savings=(annual_salary/12)*portion_saved
    current_savings+=current_savings*r/12
    current_savings+=monthly_savings
    month+=1
    #print (current_savings)
print("Number of months: " + str(month))
