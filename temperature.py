# def fahrenheit function here
def to_celcius(fahrenheit):
	celcius_number = (9/5)*fahrenheit+32
	return celcius_number
#def Celsius function here
def to_fahrenheit(celcius):
	fahrenheit_number = (5/9)*(celcius-32)
	return fahrenheit_number
#get input
temperature_number = int(raw_input("Enter a temperature:"))
temperature_unit = raw_input("Convert to (F)ahrenheit or (C)elsius:")                                                                                                                 

#based on input call function

if temperature_unit == "C": 
	celcius = to_celcius(temperature_number) #to_celcius is returning an int
	print ("celcius_number: " +str(celcius))
elif temperature_unit == "F":
	fahrenheit = to_fahrenheit(temperature_number)
	print ("fahrenheit_number: " +str(fahrenheit))

