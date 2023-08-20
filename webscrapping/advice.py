'''advice.py
Personal Project
Eric Appiah Adjei'''

import requests
from bs4 import BeautifulSoup

def get_weight_advice(calorie_data):
    total_calories = sum(calorie_data.values())
    calorie_thresholds = get_calorie_thresholds()
    
    if total_calories < calorie_thresholds['low']:
        return "You might not be consuming enough calories. Consider increasing your intake."
    elif total_calories > calorie_thresholds['high']:
        return "You might be consuming too many calories. Consider reducing your intake."
    else:
        return "Your calorie intake seems balanced. Keep up the good work!"

def get_calorie_thresholds():
    # Web scraping logic using Requests and Beautiful Soup
    url = "https://example.com/calorie_thresholds"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        low_calories = float(soup.find("span", class_="low-calories").text)
        high_calories = float(soup.find("span", class_="high-calories").text)
        
        return {'low': low_calories, 'high': high_calories}
    
    # Default thresholds if data not found
    return {'low': 1500.0, 'high': 2500.0}

