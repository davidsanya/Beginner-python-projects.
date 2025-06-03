def BMI_Calculator(w,h,option):
    """Calculate Bmi Using Weight and height"""
    if option==1:
        BMI=w/(h**2)
        return BMI
    elif option==2:
        BMItwo=(w/(h**2))*703
        return BMItwo 
    try:    
        measurement_system=int(input("Please select measurement systems you use\n1.imperial system\n2.metric system\n:"))
        if measurement_system==1:
            weight=float(input("Please Enter weight in kg: "))
            height=float(input("please Enter height in meters: "))
        elif measurement_system==2: 
            weight=float(input("Please Enter weight in ibs: "))
            height=float(input("please Enter height in inches: "))
        else: 
            print("invaild options")
        

        results=BMI_Calculator(weight, height, measurement_system)
        if results is not None: 
            print("your Bmi is:",round(results,2))
            if results<18.5:
                print("your Bmi Shows you are in the underweight range")
            elif 18.5<=results<=24.9:
                        print("your Bmi shows you are in the healthyweigh range")
            elif 25<=results<=29.9:
                        print("your Bmi shows you are in the overweight range")
            elif 30<=results<=39.9:
                        print("your Bmi shows you are in the obese range")
            elif 40<=results:
                        print("your Bmi shows you are in the severely obese range")
        else:
            print("could not calculate due to invalid options")
                    
    except ValueError:
            print("invaild inputs provide only interger or float") 
            exit()

print(BMI_Calculator.__doc__)