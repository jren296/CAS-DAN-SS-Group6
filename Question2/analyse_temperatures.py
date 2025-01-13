import os
import pandas as pd
data_folder = "temperatures"  # Folder where CSV files are stored

# Store data for calculations
monthly_temps = {month: [] for month in range(1, 13)}  # For monthly averages
station_data = {}  # For each station's data

month_map = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

for filename in os.listdir(data_folder):  # Loop through each file in the folder
    if filename.endswith(".csv"):  # Only process CSV files
        filepath = os.path.join(data_folder, filename)
        df = pd.read_csv(filepath)  # Read the CSV file

        # Ensure columns exist in csv file
        if {'STATION_NAME', 'STN_ID'}.issubset(df.columns) and all(month in df.columns for month in month_map.values()):
            for _, row in df.iterrows():
                station_id = row['STN_ID']
                station_name = row['STATION_NAME']

                # Add station data if not already present
                if station_id not in station_data:
                    station_data[station_id] = {
                        'name': station_name,
                        'temps': []
                    }

                # Temp stored under each month of the year
                for month_num, month_name in month_map.items():
                    temp = row[month_name]
                    if pd.notna(temp):  # Ensure temperature is not NaN
                        monthly_temps[month_num].append(temp)
                        station_data[station_id]['temps'].append(temp)

 # Calculating average temperatures for each month
average_monthly_temps = {
    month: (sum(temps) / len(temps)) if len(temps) > 0 else None for month, temps in monthly_temps.items()
}


# Saving averages to a file
with open("average_temp.txt", "w") as avg_file:
    avg_file.write("Average Monthly Temperatures:\n")
    for month, avg_temp in average_monthly_temps.items():
       if avg_temp is not None:  # If there's data, write the average
        avg_file.write(f"Month {month}: {avg_temp:.2f}\n")
       else:  # If there's no data, indicate so
        avg_file.write(f"Month {month}: No data available\n")

# Finding the stations with the largest temperature range
largest_range = 0
largest_range_stations = []

for station_id, data in station_data.items():
    temp_range = max(data['temps']) - min(data['temps'])
    if temp_range > largest_range:
        largest_range = temp_range
        largest_range_stations = [data['name']]
    elif temp_range == largest_range:
        largest_range_stations.append(data['name'])

# Saving results
with open("largest_temp_range_station.txt", "w") as range_file:
    range_file.write("Station(s) with the Largest Temperature Range:\n")
    range_file.write(f"Range: {largest_range:.2f}\n")
    range_file.write("\n".join(largest_range_stations))

# Calculating the average temperature for each station
average_station_temps = {
    data['name']: sum(data['temps']) / len(data['temps']) for data in station_data.values()
}
warmest_temp = max(average_station_temps.values())
coolest_temp = min(average_station_temps.values())

warmest_stations = [
    name for name, avg_temp in average_station_temps.items() if avg_temp == warmest_temp
]
coolest_stations = [
    name for name, avg_temp in average_station_temps.items() if avg_temp == coolest_temp
]

# Saving results
with open("warmest_and_coolest_station.txt", "w") as temp_file:
    temp_file.write("Warmest Station(s):\n")
    temp_file.write(f"Temperature: {warmest_temp:.2f}\n")
    temp_file.write("\n".join(warmest_stations))
    temp_file.write("\n\nCoolest Station(s):\n")
    temp_file.write(f"Temperature: {coolest_temp:.2f}\n")
    temp_file.write("\n".join(coolest_stations))




