
import streamlit as st
import random

# --- Base de données des menus marocains (simplifiée, inspirée des Tables 1-9) ---
menus = {
    "Breakfast": [
        {"name": "Barley bread with olive oil + mint tea (no sugar)", "carbs": "low", "kcal": 280, "protein": 7, "fat": 10},
        {"name": "Harcha with low-fat cheese + unsweetened tea", "carbs": "medium", "kcal": 350, "protein": 9, "fat": 12},
        {"name": "Wholemeal bread + boiled egg + cucumber salad", "carbs": "medium", "kcal": 320, "protein": 12, "fat": 8},
        {"name": "Bissara (fava bean soup) + whole wheat bread", "carbs": "low", "kcal": 300, "protein": 14, "fat": 6}
    ],
    "Lunch": [
        {"name": "Vegetable tajine with chicken + whole wheat bread", "carbs": "medium", "kcal": 420, "protein": 28, "fat": 14},
        {"name": "Lentil soup + tomato and onion salad", "carbs": "low", "kcal": 310, "protein": 18, "fat": 7},
        {"name": "Grilled sardines + zaalouk (eggplant salad) + barley bread", "carbs": "low", "kcal": 390, "protein": 25, "fat": 13},
        {"name": "Couscous with vegetables (small portion semolina, more vegetables)", "carbs": "medium", "kcal": 450, "protein": 15, "fat": 12}
    ],
    "Dinner": [
        {"name": "Harira without vermicelli + wholemeal bread", "carbs": "medium", "kcal": 360, "protein": 16, "fat": 10},
        {"name": "Vegetable soup + chicken breast salad", "carbs": "low", "kcal": 280, "protein": 22, "fat": 8},
        {"name": "Vegetable omelette + zaalouk + whole wheat bread", "carbs": "low", "kcal": 340, "protein": 20, "fat": 11},
        {"name": "Chickpea stew + green salad", "carbs": "medium", "kcal": 370, "protein": 18, "fat": 9}
    ],
    "Ramadan": [
        {"name": "Chorba + boiled egg + whole wheat bread", "carbs": "medium", "kcal": 400, "protein": 20, "fat": 10},
        {"name": "Harira without dates + salad + grilled fish", "carbs": "low", "kcal": 380, "protein": 24, "fat": 9},
        {"name": "Vegetable soup + barley bread + yogurt (no sugar)", "carbs": "low", "kcal": 300, "protein": 15, "fat": 6}
    ]
}

# --- Application Streamlit ---
st.set_page_config(page_title="Moroccan T2D Meal Recommender", page_icon="🍲", layout="centered")

st.title("🍴 Healthy Moroccan Meals for Type 2 Diabetes Patients")
st.write("Prototype application suggesting **traditional Moroccan meals** adapted for type 2 diabetes patients.")

# Informations sur le patient
st.sidebar.header("👤 Patient Information")
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=45)
bmi = st.sidebar.number_input("BMI", min_value=15.0, max_value=45.0, value=27.0)
activity = st.sidebar.selectbox("Activity level", ["Low", "Moderate", "High"])
is_ramadan = st.sidebar.checkbox("Currently fasting (Ramadan)?")

# Choix du type de repas
if is_ramadan:
    meal_type = "Ramadan"
else:
    meal_type = st.selectbox("Choose your meal:", ["Breakfast", "Lunch", "Dinner"])

# Préférence glucidique
carb_pref = st.radio("Select carbohydrate preference:", ["low", "medium", "no preference"])

# Génération d'une recommandation
if st.button("Get Recommendation"):
    if carb_pref == "no preference":
        options = menus[meal_type]
    else:
        options = [m for m in menus[meal_type] if m["carbs"] == carb_pref]
        if not options:
            options = menus[meal_type]
    meal = random.choice(options)

    # Affichage
    st.success(f"👉 Suggested {meal_type}: **{meal['name']}**")
    st.write(f"🔹 Calories: {meal['kcal']} kcal")
    st.write(f"🔹 Proteins: {meal['protein']} g | Fats: {meal['fat']} g | Carbs: {meal['carbs']}")

# Ajout d'informations pratiques
st.markdown("""
---
✅ Meals inspired by Moroccan traditional cuisine.  
✅ Adapted to reduce glycemic peaks and improve metabolic balance.  
✅ Includes **Ramadan-specific options**.  
✅ Future extension: connect to a real database of Moroccan recipes and AI-based prediction of glycemic response.  
""")
