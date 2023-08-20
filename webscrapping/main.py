'''main.py
Personal Project
Eric Appiah Adjei'''

import user_input
import calories_analyzer
import advice

def main():
    print("Welcome to the Calorie Calculator!")
    user_data = user_input.get_user_input()
    calorie_data = calories_analyzer.analyze_calories(user_data)
    weight_advice = advice.get_weight_advice(calorie_data)
    
    print("\nCalorie Analysis:")
    for item, calories in calorie_data.items():
        print(f"{item}: {calories} calories")
    
    print("\nWeight Management Advice:")
    print(weight_advice)

if __name__ == "__main__":
    main()
