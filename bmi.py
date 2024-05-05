def calculate_and_interpret_bmi(height, weight):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters,
    and interpret the BMI value according to WHO guidelines.
    """
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        interpretation = -1
    elif bmi < 25:
        interpretation = 0
    else:
        interpretation = 1
    
    return bmi, interpretation

def main():
    # Input weight in kilograms
    weight = float(input("Enter your weight in kilograms: "))
    # Input height in meters
    height = float(input("Enter your height in meters: "))

    # Calculate BMI and interpret
    bmi, interpretation = calculate_and_interpret_bmi(height, weight)
    
    print("Your BMI is:", round(bmi, 2))
    print("Interpretation:", interpretation)

if __name__ == "__main__":
    main()
