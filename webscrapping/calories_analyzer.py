'''calories_analyzer.py
Personal Project
Eric Appiah Adjei'''

import requests
from bs4 import BeautifulSoup

def analyze_calories(user_data):
    food_items = ['breakfast', 'lunch', 'dinner', 'snacks']
    calorie_data = {}
    
    for item in food_items:
        calorie_data[item] = user_data[item]
        
        # Web scraping to fetch accurate calorie data
        
        food_name = input(f"Enter the name of {item}: ")
        calorie_data[item] = get_calories_from_website(food_name)
    return calorie_data
    
    return calorie_data

def get_calories_from_website(food_name):
    # Web scraping using Requests and Beautiful Soup
    url = f"https://example.com/calorie/{food_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        calorie_element = soup.find("span", class_="calories")
        
        if calorie_element:
            return float(calorie_element.text)
    return 0.0  # Default if data not found
