# AI-ML-PROJECT
AIR QUALITY PREDICTOR 
OVERVIEW
The Air Quality Predictor is a simple Python-based application designed to calculate and categorize air quality based on environmental parameters. It provides users with immediate feedback on atmospheric conditions and safety advice based on the calculated results. The core of the application lies in its ability to process key environmental pollutants and meteorological factors specifically Particulate Matter (PM2.5), Temperature, and Humidity. By applying a calculated algorithmic approach, the program translates these complex numerical inputs into a simplified Air Quality Index (AQI).
WHY THIS PROJECT?
With rising pollution levels in urban areas, understanding air quality is essential for health and safety. I developed this project to:
•	Apply basic Python programming concepts (Input/Output, Data Types, and Conditionals).
•	Understand how environmental factors like PM2.5 and Temperature relate to the Air Quality Index (AQI).
•	Create a tool that provides actionable health advice based on environmental data.
FEATURES
•	Real-time User Input: Accepts live data for Temperature, Humidity, and PM2.5.
•	Automatic AQI Calculation: Uses a mathematical formula to estimate air quality.
•	Health Advisory: Provides specific advice (e.g., "Wear a mask" or "Stay indoors") based on the pollution level.
•	User-Friendly Interface: Simple command-line interface (CLI) that is easy to navigate.
HOW THE PROGRAM WORKS
1.	Input Phase: The program prompts the user to enter three values: Temperature (°C), Humidity (%), and PM2.5 concentration (ug/m^3).
2.	Calculation Phase: It applies a linear formula:
                              AQI = (PM2.5 \times 1.5) + (Temperature \times 0.1)
3.	Logic Phase: The program compares the calculated AQI against standard safety thresholds using if-elif-else statements.
4.	Output Phase: It displays the final AQI value, the air category, and a health tip.
TECHNOLOGIES OR TOOLS USED
•	Language: Python 3.x
•	IDE: VS Code (Visual Studio Code)
•	Libraries: Built-in Python functions (no external installations required).
STEPS TO INSTALL AND RUN
1.	Install Python: Download and install Python from python.org.
2.	Setup VS Code: Install VS Code and the Python Extension.
3.	Create File: Create a new file named main.py and paste the code into it.
4.	Run Program:
o	Open the terminal in VS Code.
o	Type python main.py and press Enter.
5.	Enter Data: Follow the on-screen prompts to get your results.
LIMITATIONS
•	Static Formula: The calculation is a simplified estimate and does not use real-time complex meteorological equations.
•	No Data Storage: The program does not save previous readings to a database or file.
•	Manual Entry: Users must manually type the data instead of the program fetching it from an API or sensor.
FUTURE ENHANCEMENTS
•	API Integration: Connect the program to a live weather API to get real-time data automatically.
•	GUI Development: Create a graphical window using Tkinter or PyQt for a better user experience.
•	Machine Learning: Implement scikit-learn to predict future air quality based on historical datasets.
CONCLUSION
This project successfully demonstrates how basic programming logic can be used to solve real-world problems. While simple, it serves as a foundation for more advanced environmental monitoring systems involving IoT sensors and Artificial Intelligence.
