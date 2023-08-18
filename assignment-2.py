import requests

BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data(city):
    params = {
        "q": city,
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def get_temperature(weather_data, target_date):
    for entry in weather_data["list"]:
        if entry["dt_txt"] == target_date:
            return entry["main"]["temp"]
    return None

def get_wind_speed(weather_data, target_date):
    for entry in weather_data["list"]:
        if entry["dt_txt"] == target_date:
            return entry["wind"]["speed"]
    return None

def get_pressure(weather_data, target_date):
    for entry in weather_data["list"]:
        if entry["dt_txt"] == target_date:
            return entry["main"]["pressure"]
    return None

def main():
    city = "London,us"  # City for weather forecast
    
    weather_data = get_weather_data(city)
    
    while True:
        print("Select an option:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            target_date = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(weather_data, target_date)
            if temperature is not None:
                print(f"Temperature at {target_date}: {temperature} °C")
            else:
                print("Data not available for the given date and time.")
        elif choice == "2":
            target_date = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(weather_data, target_date)
            if wind_speed is not None:
                print(f"Wind Speed at {target_date}: {wind_speed} m/s")
            else:
                print("Data not available for the given date and time.")
        elif choice == "3":
            target_date = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(weather_data, target_date)
            if pressure is not None:
                print(f"Pressure at {target_date}: {pressure} hPa")
            else:
                print("Data not available for the given date and time.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
