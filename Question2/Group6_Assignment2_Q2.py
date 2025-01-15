import os
import csv
from collections import defaultdict

temperatures_dir = "D:\ABC_company\ivan"

# Define seasons: each season contains months (1-indexed)
seasons = {
    'Summer': [16, 5, 6],  # December, January, February
    'Autumn': [7, 8, 9],   # March, April, May
    'Winter': [10, 11, 12],   # June, July, August
    'Spring': [13, 14, 15]  # September, October, November
}

# Dictionary to store temperature data for each station across years
station_data = defaultdict(lambda: defaultdict(list))  # station_data[station_name][month] = [temperature]

# Read data from CSV files and store it in station_data
def collete_the_station_data():
    for year in range(1986, 2005):
        file_path = os.path.join(temperatures_dir, f'stations_group_{year}.csv')
        if not os.path.exists(file_path):
            break
        
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            
            for row in reader:
                station_name = row[0]
                station_id = row[1]
                latitude = row[2]
                longitude = row[3]
                temperatures = list(map(float, row[4:]))

                # Store the data for each month in station_data
                for month, temp in enumerate(temperatures, start=1):
                    station_data[station_name][month].append(temp)
    

# Function to calculate the average temperature for each season
def calculate_seasonal_averages():
    seasonal_averages = defaultdict(lambda: defaultdict(float))
    
    for station_name, months_data in station_data.items():
        for season_name, months in seasons.items():
            season_temps = []
            for month in months:
                season_temps.extend(months_data[month])  # Add temperatures for the season
            if season_temps:
                seasonal_averages[station_name][season_name] = sum(season_temps) / len(season_temps) 

    return seasonal_averages

# Function to find the station with the largest temperature range
def find_largest_temp_range():
    largest_range = -float('inf')
    largest_range_stations = []
    
    for station_name, months_data in station_data.items():
        min_temp = float('inf')
        max_temp = -float('inf')
        for month, temps in months_data.items():
            min_temp = min(min_temp, min(temps))
            max_temp = max(max_temp, max(temps))
            if month == 12:
                break
        temp_range = max_temp - min_temp
        if temp_range > largest_range:
            largest_range = temp_range
            largest_range_stations = [station_name]
        elif temp_range == largest_range:
            largest_range_stations.append(station_name)
    
    return largest_range_stations, largest_range

# Function to find the warmest and coolest stations
def find_warmest_and_coolest_stations():
    station_avg_temps = {}
    
    for station_name, months_data in station_data.items():
        all_temps = []
        for month, temps in months_data.items():
            all_temps.extend(temps)
            if month == 12:
                break
        avg_temp = sum(all_temps) / len(all_temps)
        station_avg_temps[station_name] = avg_temp
            
    warmest_station = min(station_avg_temps, key=station_avg_temps.get)
    coolest_station = max(station_avg_temps, key=station_avg_temps.get)
    
    return warmest_station, station_avg_temps[warmest_station], coolest_station, station_avg_temps[coolest_station]

# Write seasonal averages to file
def write_seasonal_averages(seasonal_averages):
    with open('average_temp.txt', 'w') as file:
        for station_name, season_temps in seasonal_averages.items():
            file.write(f"Station: {station_name}\n")
            for season, avg_temp in season_temps.items():
                file.write(f"  {season}: {avg_temp:.2f}\n")
            file.write("\n")

# Write largest temperature range to file
def write_largest_temp_range(largest_range_stations, largest_range):
    with open('largest_temp_range_station.txt', 'w') as file:
        file.write(f"Stations with the largest temperature range ({largest_range:.2f}°C):\n")
        for station in largest_range_stations:
            file.write(f"  {station}\n")

# Write warmest and coolest stations to file
def write_warmest_and_coolest(warmest_station, warmest_temp, coolest_station, coolest_temp):
    with open('warmest_and_coolest_station.txt', 'w') as file:
        file.write(f"Warmest Station: {warmest_station} with an average temperature of {warmest_temp:.2f}°C\n")
        file.write(f"Coolest Station: {coolest_station} with an average temperature of {coolest_temp:.2f}°C\n")

# Main function to run the program
def main():
   
    collete_the_station_data()
    seasonal_averages = calculate_seasonal_averages()
    write_seasonal_averages(seasonal_averages)
    
    largest_range_stations, largest_range = find_largest_temp_range()
    write_largest_temp_range(largest_range_stations, largest_range)
    
    warmest_station, warmest_temp, coolest_station, coolest_temp = find_warmest_and_coolest_stations()
    write_warmest_and_coolest(warmest_station, warmest_temp, coolest_station, coolest_temp) 
    print(warmest_station)
    print(warmest_temp)
    print(coolest_station)
    print(coolest_temp)
   


main()
   