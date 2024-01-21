#!/usr/bin/python3
"""
Module to show calender
"""
import calendar



def print_cal(year):    
    for month in range(1,13):
        print(calendar.month(year,month))
        
def show_month(year,month):
    print(calendar.month(year,month))


if __name__ == "__main__":
    which = input("Print Calender or Month \n")
    if which == 'calender':  
        year = int(input("Enter year \n"))
        print_cal(year)
    if which == 'month':  
        year = int(input("Enter year \n"))
        month = int(input("Enter Month \n"))
        show_month(year, month)
