def main():
	milesToKm()
	FahToCel()
	GalToLit()
	PoundsToKg()
	InchesToCm()

def milesToKm():
	counter = 0
	miles = float(input("William, please tell me how many miles you'd like to convert to kilometers: "))

	while miles < 0 and counter <= 1:
		print("William, please do not enter a negative value!")
		miles = float(input("Please enter a valid number: "))
		counter = counter + 1

	if counter >= 1:
		print("ERROR: WILLIAM, YOU ARE ONLY ALLOWED THREE ATTEMPTS!")

	else:
		kilometers = format(miles * 1.6, '.2f')
		print("William,", miles, "is equal to", kilometers, "isn't that amazing!?")


def FahToCel():
	counter = 0 
	farenheit = float(input("William, please tell me what temperature in farenheit you'd like to convert to celcius: "))

	while farenheit >= 1000 and counter <= 1:
		print("William, let's cap it at 1000 degrees, okay?")
		farenheit = float(input("Please enter a valid number: "))
		counter = counter + 1

	if counter >= 1:
		print("ERROR: WILLIAM, YOU ARE ONLY ALLOWED THREE ATTEMPTS!")

	else:
		celcius = format((farenheit - 32) * 5/9, '.2f')
		print("William", farenheit, "farenheit is equal to", celcius, "isn't that amazing!?")


def GalToLit():
	counter = 0
	gallons = float(input("William, please tell me how many gallons you'd like to convert to liters: "))

	while gallons < 0 and counter <= 1:
		print("William, we can't calculate for negative values. Come on!")
		gallons = float(input("Please enter a valid number: "))
		counter = counter + 1 

	if counter >= 1:
		print("ERROR: WILLIAM, YOU ARE ONLY ALLOWED THREE ATTEMPTS!")

	else:
		liters = format(3.9 * gallons, '.2f')
		print("William,", gallons, "gallons is equal to", liters, "liters, isn't that amazing!?")


def PoundsToKg():
	counter = 0
	pounds = float(input("William, please tell me how many pounds you'd like to convert to kilograms: "))

	while pounds < 0 and counter <= 1:
		print("William, we can't calculate for negative pounds, either.")
		pounds = float(input("Please enter a valid number: "))
		counter = counter + 1

	if counter >= 1:
		print("ERROR: WILLIAM, YOU ARE ONLY ALLOWED THREE ATTEMPTS!")

	else:
		kilograms = format(0.45 * pounds, '.2f')
		print("William,", pounds, "pounds is equal to", kilograms,"kilograms, isn't that amazing!?")


def InchesToCm():
	counter = 0
	inches = float(input("William, please tell me how many inches you'd like to convert to centimeters: "))

	while inches < 0 and counter <= 1:
		print("William, we can't calculate for negative inches.")
		inches = float(input("Please enter a valid number: "))
		counter = counter + 1

	if counter >= 1:
		print("ERROR: WILLIAM, YOU ARE ONLY ALLOWED THREE ATTEMPTS!")

	else:
		centi = format(2.54 * inches, '.2f')
		print("William,", inches, "inches are equal to", centi,"centimeters, isn't that amazing!?")

main()
