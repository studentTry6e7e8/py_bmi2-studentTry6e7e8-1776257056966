def calculate_bmi():
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))

        if height <= 0:
            print("Error: Height must be greater than zero.")
            return

        bmi = weight / (height ** 2)
        
        if bmi < 25:
            status = "Other"
        elif 25 <= bmi < 30:
            status = "Overweight"
        else:
            status = "Obesity"

        print(f"BMI: {bmi:.2f} | Status: {status}")

    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_bmi()