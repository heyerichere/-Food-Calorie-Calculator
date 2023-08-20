'''user_input.py
Personal Project
Eric Appiah Adjei'''

def get_user_input():
    #Takes calories consumed, converts them into float and adds them to a hashmap 

    user_data = {}
    
    user_data['breakfast'] = float(input("Enter calories consumed during breakfast: "))
    user_data['lunch'] = float(input("Enter calories consumed during lunch: "))
    user_data['dinner'] = float(input("Enter calories consumed during dinner: "))
    user_data['snacks'] = float(input("Enter calories consumed during snacks: "))
    
    return user_data

