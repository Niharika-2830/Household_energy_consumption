# Household Energy Consumption Monitoring 📊⚡

This is a Streamlit-based data visualization and analysis project for monitoring household energy consumption using IoT-generated data.

## 🔧 Project Overview

This project visualizes and analyzes energy consumption data in Indian households. It provides interactive charts and insights using Python libraries such as:

- `matplotlib`
- `seaborn`
- `pandas`
- `streamlit`
- `joblib`

##1. 📁 Project Structure

Household_energy_consumption/
│
├── app.py                    # Main Streamlit app
├── energy_data_india_*.csv   # Dataset (replace * with actual filename)
├── energy_predictor.pkl      # Trained ML model for prediction
├── requirements.txt          # Python dependencies
└── env/                      # Virtual environment (excluded from repo)

## 🖥️ Installation & Running the App

### 1. Clone the Repository
git clone https://github.com/your-username/Household_energy_consumption.git
cd Household_energy_consumption

##2. Create and Activate a Virtual Environment (Optional but recommended)
python -m venv env
### Windows
env\Scripts\activate
### macOS/Linux
source env/bin/activate

##3. Install Dependencies
pip install -r requirements.txt

##4. Run the Streamlit App
streamlit run app.py
