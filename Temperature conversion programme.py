# Temperature conversion programme
temp= float(input("Enter the temperature: "))
unit = input("Is the temperature in celcius or fahrenheit (c or f): ")

if unit == "c":
    temp = round((temp * 9/5) + 32 )
    print(f"Temperature in fahrenheit is {temp}°F")
elif unit == "f": 
    temp = round((temp - 32) * 5/9 )
    print(f"Temperature in celcius is {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurment")
    
    

