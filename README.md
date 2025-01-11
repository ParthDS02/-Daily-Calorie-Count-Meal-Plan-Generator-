# 🥗 **Daily Calorie Count Meal Plan Generator** 🍽️

Welcome to the **Daily Calorie Count Meal Plan Generator** project! This Streamlit web application is designed to create personalized meal plans based on user inputs such as age, weight, gender, and calorie goals. It also allows users to download their customized meal plans as PDFs.

---

## 🔎 **Project Overview**

This project uses **Streamlit** for building a simple yet powerful web interface and **FPDF** for generating downloadable PDFs. Users can input their personal details (age, weight, gender) and calorie target, and the app will generate a daily meal plan that meets their nutritional needs. The meal plan is based on predefined food categories and is fully customizable based on the user's preferences.

### 💡 **Why this Project?**

The goal of this project is to help individuals with their daily nutritional planning. It allows users to:
- **Track their daily calories** in an easy-to-use interface.
- **Generate personalized meal plans** based on individual requirements.
- **Download meal plans** for offline use.

This project is not only a functional tool but also an excellent demonstration of how data science can be applied to real-world problems such as personalized nutrition planning. By combining data-driven meal recommendations with the power of Streamlit and Python, this app serves as a practical example of data science in action.

---

## 🔗 **How Does This Relate to Data Science?**

Data Science is about extracting insights from data and making informed decisions based on that data. In this project, several key data science principles are applied:

1. **Data Processing and Analysis**: The app uses user input data (such as age, weight, gender) to perform data analysis and recommend a balanced meal plan based on calorie goals.
   
2. **Modeling and Personalization**: The meal plan generation involves calculating a person's Basal Metabolic Rate (BMR), Total Daily Energy Expenditure (TDEE), and calorie needs. It’s a data-driven approach to making personalized recommendations for meal planning.

3. **Data Visualization**: Through Streamlit, the app visualizes meal plans in an easy-to-read format, helping users to understand their dietary needs and track their progress visually.

4. **PDF Generation**: The app’s PDF generation feature showcases how Python can be used to create dynamic documents based on real-time data, which is particularly useful for report generation in data-driven applications.

---

## 🖥️ **Web Screen Snapshot**

The web interface of the **Daily Calorie Count Meal Plan Generator** is designed to be user-friendly and intuitive. Users will encounter a simple form where they can enter their personal information (age, weight, gender) and calorie goals. The app will use this data to calculate and display a personalized meal plan.

### Features:
- **Input Fields**: Age, weight, gender, and calorie target.
- **Real-time Meal Plan Display**: As users input their data, the app will generate a tailored meal plan in real-time.
- **Customizable Meal Options**: Users can choose preferences for types of food or specific dietary restrictions.
- **Responsive Layout**: The design is responsive to fit various screen sizes, ensuring a seamless experience on mobile, tablet, and desktop.

![image](https://github.com/user-attachments/assets/f28224dc-62ae-4c7c-a434-365914070078)


---

## 📑 **Report Result Screen Snapshot**

The **Report Result Screen** displays the final meal plan in a downloadable PDF format. This screen provides a summary of the daily meal recommendations, including meals for breakfast, lunch, dinner, and snacks, aligned with the user’s calorie goals. 

### Features:
- **Meal Plan Overview**: Detailed breakdown of meals with calorie counts for each.
- **Downloadable PDF**: The meal plan can be downloaded as a PDF for offline reference.
- **Personalized Recommendations**: Shows specific calorie counts for each meal based on user inputs.

![image](https://github.com/user-attachments/assets/ed2fb00c-c529-46a8-8f2c-960a58988cd7)

---

## 💻 **Technologies Used**

- **Streamlit**: For building the interactive web interface.
- **FPDF**: For generating downloadable PDF meal plans.
- **Python**: For backend logic and data processing.

---

## 🚀 **Getting Started**

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/daily-calorie-count-meal-plan-generator.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

