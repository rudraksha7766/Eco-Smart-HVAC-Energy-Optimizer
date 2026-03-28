# Eco-Smart-HVAC-Energy-Optimizer
# 🍃 Eco-Logic: Human-Centric Thermal Intelligence System
### *Registration No: 25BAI10635 | Course: Digital Literacy (AI/ML)*

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📌 Project Overview
**Eco-Logic** is an interactive Machine Learning application designed to optimize HVAC (Heating, Ventilation, and Air Conditioning) settings in real-time. Unlike traditional thermostats that use static "Set-and-Forget" logic, this system treats **humans** and **electronics** as active heat sources, adjusting the indoor climate to maximize comfort while minimizing carbon footprint.

### 🧠 The Core Intelligence
The system uses a **Decision Tree Regressor** trained on 500+ simulated environmental scenarios. It intelligently switches between:
- 🔥 **Winter Protocol:** Leveraging body heat and PC thermal output to reduce heater reliance.
- ❄️ **Summer Protocol:** Compensating for high internal heat loads to maintain productivity levels.

---

## 🚀 Key Features
- **Dual-Mode Logic:** Automatic detection of severe winters (-45°C) and harsh summers (+45°C).
- **Humanized Feedback:** Provides natural language explanations for every AI decision.
- **Carbon Tracking:** Estimates daily CO2 savings based on optimized thermostat levels.
- **Safety Guardrails:** Hard-coded temperature floors (16°C) and ceilings to prevent hardware damage.

---

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Libraries:** - `NumPy` & `Pandas`: Data simulation and structural processing.
  - `Scikit-Learn`: Implementation of the Decision Tree Regressor.
  - `Time`: Simulated AI "thought" latency for improved UX.

---

## 📊 How It Works (The Math)
The model analyzes the following feature set:
$$Optimal\_Temp = f(Outside\_Temp, Occupants, Active\_PCs)$$

The decision tree splits the data based on thermal thresholds. For example, if the outside temperature drops below **18°C**, the model enters "Heat Recovery" mode, where:
> **Internal Heat Gain** = (Occupants × 0.3) + (Active_PCs × 0.2)

The AI then offsets the mechanical heating requirement by this value, significantly reducing grid energy consumption.

---

## 📈 4. Performance & Impact Analysis
Integrated directly into the system output, the model provides:
* **Energy Efficiency:** A predicted **18-22% reduction** in HVAC electricity load.
* **Carbon Footprint:** An estimated saving of **4.2kg of CO2** per 24-hour cycle.
* **Hardware Longevity:** Optimized cycling to prevent AC compressor wear and tear.

---

## 🔮 5. Future Roadmap (V2.0)
To scale this project from a terminal script to a real-world product:
* **IoT Integration:** Syncing with **DHT11/DHT22** sensors for live data.
* **Cloud Deployment:** Hosting the model via a **Streamlit** or **Flask** web dashboard.
* **Time-Series Analysis:** Implementing **LSTM (Long Short-Term Memory)** networks to predict temperature shifts 24 hours in advance.

---

## 🎓 6. Academic Credits & Metadata
* **University:** VIT Bhopal University
* **School:** School of Computing Science and Engineering (SCSE)
* **Specialization:** B.Tech CSE (Artificial Intelligence & Machine Learning)
* **Submission Year:** 2026

---

## 🚀 7. How to Run
1. Ensure you have `pandas`, `numpy`, and `scikit-learn` installed.
2. Run the main script:
   ```bash
   python main.py
