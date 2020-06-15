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
