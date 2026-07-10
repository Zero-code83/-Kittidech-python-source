print("4. BMI Calculator:")

#input
weight = float(input("Enter Weight(Kg) : "))
height = float(input("Enter Height(M) : "))

#process
BMI = weight / (height ** 2)

#output
print("Your BMI : ",BMI)