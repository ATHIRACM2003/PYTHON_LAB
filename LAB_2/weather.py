#5.
import datetime

def weather_data():


  weather = [
      {'date': datetime.date(2024, 8, 1), 'max_temp': 28, 'min_temp': 22, 'humidity': 65},
       {'date': datetime.date(2024, 8, 2), 'max_temp': 29, 'min_temp': 20, 'humidity': 60},
       {'date': datetime.date(2024, 8, 3), 'max_temp': 25, 'min_temp': 22, 'humidity': 64},
       {'date': datetime.date(2024, 8, 4), 'max_temp': 25, 'min_temp': 22, 'humidity': 60},
       {'date': datetime.date(2024, 8, 5), 'max_temp': 29, 'min_temp': 24, 'humidity': 63},
       {'date': datetime.date(2024, 8, 6), 'max_temp': 30, 'min_temp': 20, 'humidity': 65},
       {'date': datetime.date(2024, 8, 7), 'max_temp': 28, 'min_temp': 19, 'humidity': 65},
       {'date': datetime.date(2024, 8, 8), 'max_temp': 27, 'min_temp': 20, 'humidity': 64},
       {'date': datetime.date(2024, 8, 9), 'max_temp': 31, 'min_temp': 21, 'humidity': 66},
       {'date': datetime.date(2024, 8, 10), 'max_temp': 36, 'min_temp': 22, 'humidity': 65},
  ]
  return weather

def min_max(weather_data):
     max_temp = float('-inf')
     min_temp = float('inf')
     for day in weather_data:
        max_temp = max(max_temp, day['max_temp'])
        min_temp = min(min_temp, day['min_temp'])
     return max_temp, min_temp

def count_days(weather_data, temp=30):
  hot_days = 0
  for day in weather_data:
    if day['max_temp'] > temp:
      hot_days += 1
  return hot_days

def average_humidity(weather_data):
  total_humidity = sum(day['humidity'] for day in weather_data)
  num_days = len(weather_data)
  return total_humidity / num_days

weather_data = weather_data()

highest_temp, lowest_temp = min_max(weather_data)
print("Highest temperature:", highest_temp)
print("Lowest temperature:", lowest_temp)

hot_days = count_days(weather_data)
print("Number of days with temperature above 30°C:", hot_days)

average_humidity = average_humidity(weather_data)
print("Average humidity:", average_humidity)
