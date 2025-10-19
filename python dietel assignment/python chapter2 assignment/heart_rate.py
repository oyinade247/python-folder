#prompt the user to enter their age
#To get the maximum heart rate, minus the user age  from 220 minute
#To get the target heart rate multipy the maximum heart rate wiith 85% or 50%



user_age = int(input("Enter your age : "))

maximum_heart_rate = (user_age - 220)

target_heart_rate = (maximum_heart_rate * 0.85)

print("Your maximum heart rate is", maximum_heart_rate)

print("Your target heart rate is", target_heart_rate)