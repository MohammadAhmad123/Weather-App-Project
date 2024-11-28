# Hardcoded weather data
weather_data = {
    "London": {"temperature": "03°C", "conditions": "Partly Cloudy", "wind_speed": "5 mph", "humidity": "93%"},
    "New York": {"temperature": "10°C", "conditions": "Cloudy", "wind_speed": "13 mph", "humidity": "83%"},
    "Tokyo": {"temperature": "8°C", "conditions": "Clear", "wind_speed": "4 mph", "humidity": "57%"},
    "Sydney": {"temperature": "21°C", "conditions": "Cloudy", "wind_speed": "7 mph", "humidity": "95%"},
    "Paris": {"temperature": "4°C", "conditions": "Clear", "wind_speed": "5mph", "humidity": "89%"}
}

# Welcome message
def display_welcome():
    print("Welcome to the Python Weather Forecast App!\n")

# Function to get city name input from the user
def get_city():
    while True:
        city = input("Please enter the city name for the weather forecast: ").strip().title()
        if city in weather_data:
            return city
        else:
            print("Invalid city name. Please try again.\n")

# Function to display weather information
def display_weather(city):
    data = weather_data[city]
    print(f"\nWeather Forecast for {city}:")
    print(f"Temperature: {data['temperature']}")
    print(f"Conditions: {data['conditions']}")
    print(f"Wind Speed: {data['wind_speed']}")
    print(f"Humidity: {data['humidity']}\n")

# Thank you message
def display_thank_you():
    print("Thank you for using the Python Weather Forecast App!\n")

# Main function to run the program
def main():
    display_welcome()
    city = get_city()
    display_weather(city)
    display_thank_you()

# Run the program
if __name__ == "__main__":
    main()