import streamlit as st  
import pandas as pd    
import matplotlib.pyplot as plt 
import seaborn as sns 
# Step 1: Load dataset
# Load dataset
df = pd.read_csv("energy_data_india_coYOUOMGWA")

st.title("Energy Dashboard for Housing Complex")

# Step 2: Create Sidebar Filters
# Sidebar Filters
region = st.sidebar.selectbox("Select Region", ["All"] + sorted(df["Region"].unique().tolist()))

if region != "All":
    df = df[df["Region"] == region]

st.subheader(" Household Energy Consumption Overview")
st.write(df.head())

# Step 3: Metrics
avg_energy = df["Monthly_Energy_Consumption_kWh"].mean()
total_energy = df["Monthly_Energy_Consumption_kWh"].sum()
st.metric("Average Monthly Consumption (kWh)", f"{avg_energy:.2f}")
st.metric("Total Energy Consumption (kWh)", f"{total_energy:.0f}")

# Step 4: Visualizations
# Energy vs Income
st.subheader(" Income vs Energy Consumption")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x="Monthly_Income_INR", y="Monthly_Energy_Consumption_kWh", hue="Region", ax=ax1)
st.pyplot(fig1)

# Appliance Contribution
st.subheader(" Appliance-wise Count vs Energy Consumption")
appliances = ["Appliance_AC", "Appliance_Fan", "Appliance_Light", "Fridge", "Washing_Machine", "EV_Charging"]
selected_appliance = st.selectbox("Select Appliance", appliances)
fig2, ax2 = plt.subplots()
sns.barplot(x=df[selected_appliance], y=df["Monthly_Energy_Consumption_kWh"], ax=ax2, color="green")
ax2.set_xlabel(f"No. of {selected_appliance.replace('_', ' ')}")
ax2.set_ylabel("Energy Consumption (kWh)")
st.pyplot(fig2)

# Step 5: Recommendations
st.subheader(" Smart Recommendations")
for _, row in df.iterrows():
    if row["Monthly_Energy_Consumption_kWh"] > 250:
        st.warning(f"Household ID {row['Household_ID']} - High usage! Recommend switching to solar and LED bulbs.")
    elif row["EV_Charging"] == 1:
        st.info(f"Household ID {row['Household_ID']} - Consider installing a separate EV meter for optimal billing.")

# Step 6: Download Recommendations
recommendations = []
for _, row in df.iterrows():
    if row["Monthly_Energy_Consumption_kWh"] > 250:
        recommendations.append(f"Household ID {row['Household_ID']} - High usage! Recommend switching to solar and LED bulbs.")
    elif row["EV_Charging"] == 1:
        recommendations.append(f"Household ID {row['Household_ID']} - Consider installing a separate EV meter for optimal billing.")

if recommendations:
    st.download_button("Download Recommendations", "\n".join(recommendations), "recommendations.txt")

#Model
import joblib

# Load model
model = joblib.load(r"C:\Users\NIHARIKA\Desktop\My projects\IoT Project(31-07-2025)\energy_predictor.pkl")

st.subheader("📊 Predict Your Household Energy Consumption")

# User input form
income = st.number_input("Monthly Income (INR)", min_value=0)
ac = st.slider("No. of ACs", 0, 5)
fan = st.slider("No. of Fans", 0, 10)
light = st.slider("No. of Lights", 0, 20)
fridge = st.slider("No. of Fridges", 0, 2)
washing_machine = st.slider("No. of Washing Machines", 0, 2)
ev = st.selectbox("EV Charging Enabled?", [0, 1])

if st.button("Predict"):
    input_df = pd.DataFrame([[income, ac, fan, light, fridge, washing_machine, ev]],
                            columns=["Monthly_Income_INR", "Appliance_AC", "Appliance_Fan", "Appliance_Light", 
                                     "Fridge", "Washing_Machine", "EV_Charging"])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Monthly Energy Consumption: {prediction:.2f} kWh")
