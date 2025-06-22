print("This a BMI Calculator Program")
print("")
age=int(input("Please enter your age: "))
def calculate():
    weight=int(input("Enter your weight in kg: "))
    height=int(input("Enter your heigth in cm: "))
    height=height/100
    if weight<=0 or height<=0:
        print("pls enter valid numbers")
        return False
    bmi=weight/(height**2)
    return bmi
bmi=calculate()
def results(bmi,age):
    if age<18:
        print("You need to visit a Doctor")
        return 
    else:
        if bmi<18.5:
            print( "You are Underweight")
        elif 18.5<=bmi<25:
            print ("Normal weigth")
        elif 25<=bmi<30:
            print("You are overweight")
        else:
            print("You are obese")
results(bmi,age)
        