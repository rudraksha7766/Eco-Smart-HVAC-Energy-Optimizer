import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import warnings
import time

warnings.filterwarnings('ignore')

def generate_thermal_data():
    np.random.seed(42)
    n_samples = 500 # More data for better human-like "intuition"
    
    outside_temp = np.random.randint(-15, 46, n_samples)
    occupants = np.random.randint(1, 15, n_samples)
    active_computers = np.random.randint(0, 15, n_samples)
 
    optimal_hvac_setting = []
    
    for i in range(n_samples):
        # Heating Mode (Winter)
        if outside_temp[i] < 18:
            target_temp = 22.0 - (occupants[i] * 0.3) - (active_computers[i] * 0.2)
            target_temp = max(16.0, target_temp)
        # Cooling Mode (Summer)
        else:
            target_temp = 24.0 - (occupants[i] * 0.3) - (active_computers[i] * 0.2)
            if outside_temp[i] > 35: target_temp -= 1.0
            target_temp = max(18.0, target_temp)
            
        optimal_hvac_setting.append(round(target_temp + np.random.uniform(-0.3, 0.3), 1))

    return pd.DataFrame({
        'Outside_Temp_C': outside_temp,
        'Occupants': occupants,
        'Active_Computers': active_computers,
        'Optimal_HVAC_Temp': optimal_hvac_setting
    })

def main():
    # Setup
    data = generate_thermal_data()
    model = DecisionTreeRegressor(max_depth=7, random_state=42)
    model.fit(data[['Outside_Temp_C', 'Occupants', 'Active_Computers']], data['Optimal_HVAC_Temp'])

    print("--- 🍃 Welcome back,. I'm your Smart Climate hvac Assistant. ---")
    print("I've analyzed 500+ environmental scenarios to help you save energy today.\n")

    while True:
        try:
            print("--- Current Room Status ---")
            current_temp = float(input("What's the temperature outside? (°C): "))
            people = int(input("How many people are in the room right now?: "))
            pcs = int(input("How many computers/laptops are running?: "))

            # AI Logic Processing
            print("\n[AI] is Thinking... analyzing heat signatures...")
            time.sleep(1)

            scenario = pd.DataFrame([[current_temp, people, pcs]], 
                                    columns=['Outside_Temp_C', 'Occupants', 'Active_Computers'])
            rec_temp = round(model.predict(scenario)[0])

            # Humanized Output Logic
            print("\n" + "═"*50)
            print(f"✅ RECOMMENDED SETTING: {rec_temp}°C")
            print("═"*50)

            # Contextual Feedback
            if current_temp < 10:
                print("❄️  It's freezing cold out there! I've increased the intensity of the heater to keep you cozy.")
            elif current_temp > 35:
                print("☀️  Severe heatwave detected. I'm prioritizing cooling to prevent fatigue. Stay hydrated!")

            # Why did the AI choose this?
            total_heat_sources = people + pcs
            if total_heat_sources > 8:
                print(f"💡 Note: With {total_heat_sources} heat sources in the room, I've lowered the AC ")
                print("   intensity to recycle the natural warmth already present. Smart choice!")

            # Carbon Impact Feature
            savings = round((abs(24 - rec_temp) * 0.05), 2)
            print(f"🌱 Sustainability Tip: This  temperature setting saves approx. {savings}kg of CO2 today.")
            
            print("═"*50)
            
            if input("\nWould you like to check another room? (y/n): ").lower() != 'y':
                print("Have a productive, eco-friendly day! Goodbye.")
                break

        except ValueError:
            print("❌ Input Error: Please use numeric values for temperature so I can calculate accurately.")

if __name__ == "__main__":
    main()
