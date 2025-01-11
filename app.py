import streamlit as st
from backend import generate_meal_plan
from generate_pdf import generate_pdf
from io import BytesIO

# Input fields
st.title("🥗 Daily Calorie Count Meal Plan Generator 🍽️")

user_name = st.text_input("Full Name:")
age = st.number_input("Age:", min_value=0, max_value=100, value=30)
gender = st.radio("Gender:", ["Male", "Female"])
weight = st.number_input("Weight (kg):", min_value=0.0, max_value=200.0, value=70.0)
calories_target = st.number_input("Calories Target:", min_value=0, max_value=5000, value=2000)
meal_preference = st.radio("Meal Preference:", ["Veg", "Non-Veg", "Both"])

# Submit button
submit = st.button("Submit")

if submit:
    # Backend logic to calculate the meal plan based on user input
    meal_plan = generate_meal_plan(age, gender, weight, calories_target, meal_preference)
    
    # Display meal plan
    st.write("**Today's Meal Plan**")
    
    # Display individual meals
    for meal_time in ["Breakfast", "Lunch", "Evening Snack", "Dinner"]:
        meal = meal_plan[meal_time]
        st.write(f"{meal_time}: {meal['Meal']} - {meal['Calories']} calories, {meal['Protein (g)']}g protein")
    
    st.write(f"**Total Calories**: {meal_plan['Total Calories']}")
    st.write(f"**Total Protein**: {meal_plan['Total Protein (g)']}g")
    
    # Generate the PDF as a BytesIO object to allow download
    pdf_file = BytesIO()
    generate_pdf(user_name, meal_plan)  # This function should now save the PDF to the BytesIO object

    # Generate the PDF file in memory
    with open(f"{user_name}_meal_plan.pdf", "rb") as pdf_output:
        pdf_file.write(pdf_output.read())
    
    # Provide the user with a download button
    pdf_file.seek(0)  # Reset the file pointer to the start of the file
    st.download_button(
        label="Download Your Meal Plan PDF",
        data=pdf_file,
        file_name=f"{user_name}_meal_plan.pdf",
        mime="application/pdf"
    )
