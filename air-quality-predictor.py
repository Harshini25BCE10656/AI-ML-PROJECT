print("------------------------------------------")
print("   WELCOME TO AIR QUALITY PREDICTOR    ")
print("------------------------------------------")

temp = float(input("Enter Temperature in Celsius: "))
humidity = float(input("Enter Humidity percentage: "))
pm25 = float(input("Enter PM2.5 concentration (ug/m3): "))


calculated_aqi = pm25 * 1.5 + (temp * 0.1)

print("\n--- Processing Data ---")
print(f"Current Temperature: {temp}")
print(f"Current Humidity: {humidity}%")
print(f"Calculated AQI Value: {calculated_aqi}")

print("------------------------------------------")

if calculated_aqi <= 50:
    print("Final Result: The air is FRESH and CLEAN.")
    print("Advice: Great day for a walk!")
elif calculated_aqi > 50 and calculated_aqi <= 100:
    print("Final Result: The air is MODERATE.")
    print("Advice: Sensitive people should be careful.")
elif calculated_aqi > 100 and calculated_aqi <= 200:
    print("Final Result: The air is POLLUTED.")
    print("Advice: Please wear a mask outside.")
else:
    print("Final Result: The air is HAZARDOUS!")
    print("Advice: Stay indoors and use an air purifier.")

print("------------------------------------------")
print("Program Finished.")
