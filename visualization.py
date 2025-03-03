import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Ensuring reproducibility so that when the code runs, the results are the exact same ensuring consistency.

# Function used to generate weather data for analysis
# Generate dates using the .datetime64() and .arange() helps pick the dates sequentially and randomly 
def generateWeatherData(days=365):
    dates = np.arange(np.datetime64('2024-01-01'), np.datetime64('2024-01-01') + days)
    temperatures = np.random.uniform(-5, 35, days)  # Random temperatures
    precipitation = np.random.uniform(0, 20, days)  # Random precipitation
    return dates, temperatures, precipitation

# Function used to analyse weather tempratures 
def analyzeWeather(temperatures):
    average_temp = np.mean(temperatures) # Average temperature
    max_temp = np.max(temperatures) # Maximum temperature 
    min_temp = np.min(temperatures) # Minimum temperature 

    print(f"Average Temp: {average_temp:.2f}°C")
    print(f"Max Temp: {max_temp:.2f}°C")
    print(f"Min Temp: {min_temp:.2f}°C")

    return average_temp 

# Function used to find the extreme hot and cold days during the year  
def findExtremeDays(dates, temperatures):
    average_temp = np.mean(temperatures) # Average temperature 
    std_temp = np.std(temperatures) # Standard deviation of the temperatures 

    hot_days = dates[temperatures > average_temp + std_temp]
    cold_days = dates[temperatures < average_temp - std_temp]

    print("\n🔥 Extremely Hot Days:", hot_days)
    print("❄️ Extremely Cold Days:", cold_days)

    return hot_days, cold_days

# Function used to plot the weather trends 
def temperatureTrend(dates, temperatures, average_temp):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, color="aqua", label="Daily Temperature")
    plt.axhline(y=average_temp, color="pink", linestyle="--", linewidth = 7, label="Average Temp")
    plt.xlabel("Day of the Year")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trends Over a Year")
    plt.legend()
    plt.grid()
    plt.show()

# Function used to plot the temprtaure distributions using a histogram 
def temperatureDistribution(temperatures):
    plt.figure(figsize=(8, 5))
    plt.hist(temperatures, bins=10, color="purple", alpha=0.7, edgecolor="black")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.title("Temperature Distribution Over the Year")
    plt.grid()
    plt.show()

 #Function used to plot the precipitation trends over the year 
def precipitationTrend(temperatures, precipitation):
    plt.figure(figsize=(8, 6))
    plt.scatter(temperatures, precipitation, color='blue', alpha=0.6)
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Precipitation (mm)')
    plt.title('Temperature vs Precipitation Trends over the year')
    plt.grid()
    plt.show()

# Function that gives a weather advisory or warnings based of the analysis of the temperature,  
# average temperature and standard deviated temperature 
def weatherAdvisory(temp, average_temp, std_temp):
    if temp > average_temp + std_temp:
        return "Heatwave Alert! Stay hydrated."
    elif temp < average_temp - std_temp:
        return "Cold wave alert! Wear warm clothing."
    else:
        return "Normal weather conditions."
    
# Main Execution of code 
if __name__ == "__main__":
    dates, temperatures, precipitation = generateWeatherData() 
    # Generates the dates, temperatures and precipitation weather data
    avg_temp = analyzeWeather(temperatures) # Average temperature 
    hot_days, cold_days = findExtremeDays(dates, temperatures) # Hot and Cold days 

    temperatureTrend(dates, temperatures, avg_temp)
    temperatureDistribution(temperatures)
    precipitationTrend(temperatures, precipitation)

    # Displays the advisory for select days
    std_temp = np.std(temperatures)
    print("\n📢 Weather Advisories:")
    for day in range(0, 365, 30):  # Sample advisory for every 30 days
        print(f"Day {day+1}: {weatherAdvisory(temperatures[day], avg_temp, std_temp)}")