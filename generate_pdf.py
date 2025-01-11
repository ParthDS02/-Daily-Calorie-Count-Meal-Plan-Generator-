from fpdf import FPDF

def generate_pdf(user_name, meal_plan):
    # Initialize PDF document
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt=f"Today's Meal Plan for {user_name}", ln=True, align='C')
    pdf.ln(10)  # Add some space after the title

    # Calories Target Section
    pdf.set_font("Arial", size=10)
    pdf.cell(100, 10, txt=f"Calories Target: {meal_plan['Calories Target']}", ln=True)

    # Add a horizontal line for better readability
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # Add table headers with Quantity column
    pdf.set_font("Arial", size=10, style='B')
    pdf.cell(30, 10, "Meal Time", border=1, align="C")
    pdf.cell(50, 10, "Meal", border=1, align="C")
    pdf.cell(30, 10, "Quantity", border=1, align="C")
    pdf.cell(30, 10, "Calories", border=1, align="C")
    pdf.cell(40, 10, "Protein (g)", border=1, align="C")
    pdf.ln()

    # Add meal plan details
    pdf.set_font("Arial", size=10)
    total_calories = 0
    total_protein = 0

    for meal_time in ["Breakfast", "Lunch", "Evening Snack", "Dinner"]:
        meal = meal_plan[meal_time]
        pdf.cell(30, 10, txt=meal_time, border=1, align="C")
        pdf.cell(50, 10, txt=meal['Meal'], border=1, align="C")
        pdf.cell(30, 10, txt=meal['Quantity'], border=1, align="C")  # Added Quantity column
        pdf.cell(30, 10, txt=str(meal['Calories']), border=1, align="C")
        pdf.cell(40, 10, txt=str(meal['Protein (g)']), border=1, align="C")
        pdf.ln()

        total_calories += meal['Calories']
        total_protein += meal['Protein (g)']

    # Add totals section
    pdf.ln(5)
    pdf.set_font("Arial", size=10, style='B')
    pdf.cell(30, 10, "Total", border=1, align="C")
    pdf.cell(50, 10, txt="Total Calories", border=1, align="C")
    pdf.cell(30, 10, "", border=1)  # Empty space for the Quantity column
    pdf.cell(30, 10, txt=str(total_calories), border=1, align="C")
    pdf.cell(40, 10, "", border=1)  # Empty space for the Protein column
    pdf.ln()

    pdf.set_font("Arial", size=10)
    pdf.cell(30, 10, "", border=1)  # Empty space for Meal Time
    pdf.cell(50, 10, txt="Total Protein (g)", border=1, align="C")
    pdf.cell(30, 10, "", border=1)  # Empty space for Quantity
    pdf.cell(30, 10, txt=str(total_protein), border=1, align="C")
    pdf.cell(40, 10, "", border=1)  # Empty space for the last column
    pdf.ln()

    # Output PDF
    pdf.output(f"{user_name}_meal_plan.pdf")
    print(f"PDF generated for {user_name}")
