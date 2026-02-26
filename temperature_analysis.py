# Name: Ishwar Vishwakarma
# Roll Number: iitp_aimlh_2602411
# Assignment: Python Loops & Automation - Subjective Question

def MaxMinTemp():
    print("\n===== Task 1: Find Maximum and Minimum =====\n")
    
    temperatures = [28, 32, 35, 29, 31, 27, 30]
    
    min_temp = temperatures[0]
    max_temp = temperatures[0]

    for temp in temperatures:
        if(temp < min_temp):
            min_temp = temp
        if(temp > max_temp):
            max_temp = temp
    
    print(f"Maximum Temperature : {max_temp}°C")
    print(f"Minimum Temperature : {min_temp}°C")

#MaxMinTemp()

def CountHotDays():
    print("\n===== Task 2: Count Hot Days =====\n")
    
    temperatures = [28, 32, 35, 29, 31, 27, 30]
    
    hot_days = 0
    
    for temp in temperatures:
        if(temp <= 30):
            continue
        if(temp > 30):
            hot_days += 1
    
    print(f"Hot Days (>30°C) : {hot_days}")
    
CountHotDays()

"""
print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
# Write your code here
"""
