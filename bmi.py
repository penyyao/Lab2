def calculate_bmi(height, weight):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight / (height * height)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value according to WHO guidelines.
    """
    if bmi < 18.5:
        return "Underweight", -1
    elif bmi < 25:
        return "Normal weight" , 0
    elif bmi < 30:
        return "Overweight", 1
    else:
        return "Obese"

def main():
    # Input weight in kilograms
    weight = float(input("Enter your weight in kilograms: "))
    # Input height in meters
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(height, weight)
    
    # Interpret BMI
    interpretation = interpret_bmi(bmi)

    print("Your BMI is:", round(bmi, 2))
    print("Interpretation:", interpretation)

if __name__ == "__main__":
    main()
