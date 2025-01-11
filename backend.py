import random

def generate_meal_plan(age, gender, weight, calories_target, meal_preference):
    # Calculate BMR using Harris-Benedict formula
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * 170) - (5.677 * age)  # Assume height is 170 cm
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * 170) - (4.330 * age)  # Assume height is 170 cm

    # Adjust TDEE based on a sedentary activity factor (1.2)
    tdee = bmr * 1.2

    # Meal distribution (divided into 4 meals)
    meal_calories = calories_target // 4
    meal_protein = (meal_calories * 0.3) // 4  # Assume 30% of calories come from protein

    # Food lists for each meal preference (Veg, Non-Veg, Both)
    veg_meals = {
        "Breakfast": [
            {"meal": "Poha", "calories": 250, "protein": 6, "quantity": "1 plate"},
            {"meal": "Upma", "calories": 200, "protein": 5, "quantity": "1 plate"},
            {"meal": "Paratha with Curd", "calories": 300, "protein": 7, "quantity": "2 parathas with 1 cup curd"},
            {"meal": "Chilla", "calories": 180, "protein": 8, "quantity": "2 chillas"},
            {"meal": "Methi Thepla", "calories": 220, "protein": 6, "quantity": "2 theplas"}
        ],
        "Lunch": [
            {"meal": "Dal Tadka with Rice", "calories": 400, "protein": 15, "quantity": "1 cup dal with 1 cup rice"},
            {"meal": "Chole with Bhature", "calories": 550, "protein": 20, "quantity": "1 plate chole with 2 bhatures"},
            {"meal": "Vegetable Pulao", "calories": 350, "protein": 10, "quantity": "1 bowl"},
            {"meal": "Palak Paneer with Roti", "calories": 450, "protein": 20, "quantity": "1 bowl palak paneer with 2 rotis"},
            {"meal": "Kadhi Pakora with Rice", "calories": 500, "protein": 14, "quantity": "1 cup kadhi with 1 cup rice"}
        ],
        "Evening Snack": [
            {"meal": "Fruit Salad", "calories": 150, "protein": 2, "quantity": "1 cup"},
            {"meal": "Chana Chaat", "calories": 180, "protein": 7, "quantity": "1 cup"},
            {"meal": "Vegetable Sandwich", "calories": 200, "protein": 8, "quantity": "2 sandwiches"},
            {"meal": "Moong Dal Chilla", "calories": 180, "protein": 12, "quantity": "2 chillas"},
            {"meal": "Soya Bean Bhel", "calories": 220, "protein": 10, "quantity": "1 bowl"}
        ],
        "Dinner": [
            {"meal": "Vegetable Khichdi", "calories": 350, "protein": 15, "quantity": "1 bowl"},
            {"meal": "Aloo Gobi with Roti", "calories": 300, "protein": 7, "quantity": "1 bowl aloo gobi with 2 rotis"},
            {"meal": "Vegetable Biryani", "calories": 400, "protein": 10, "quantity": "1 bowl"},
            {"meal": "Methi Thepla with Yogurt", "calories": 350, "protein": 12, "quantity": "2 theplas with 1 cup yogurt"},
            {"meal": "Pav Bhaji", "calories": 450, "protein": 8, "quantity": "1 plate with 2 pavs"}
        ]
    }

    non_veg_meals = {
        "Breakfast": [
            {"meal": "Egg Bhurji", "calories": 250, "protein": 20, "quantity": "2 eggs"},
            {"meal": "Chicken Sausages", "calories": 300, "protein": 25, "quantity": "3 sausages"},
            {"meal": "Omelette with Toast", "calories": 300, "protein": 20, "quantity": "2 eggs with 2 slices toast"},
            {"meal": "Chicken Paratha", "calories": 350, "protein": 25, "quantity": "2 parathas with 100g chicken"},
            {"meal": "Fish Tikka", "calories": 220, "protein": 20, "quantity": "5 pieces"}
        ],
        "Lunch": [
            {"meal": "Grilled Chicken with Rice", "calories": 500, "protein": 40, "quantity": "1 chicken breast with 1 cup rice"},
            {"meal": "Butter Chicken with Naan", "calories": 600, "protein": 35, "quantity": "1 bowl butter chicken with 1 naan"},
            {"meal": "Chicken Curry with Rice", "calories": 550, "protein": 40, "quantity": "1 bowl curry with 1 cup rice"},
            {"meal": "Fish Curry with Rice", "calories": 500, "protein": 35, "quantity": "1 bowl curry with 1 cup rice"},
            {"meal": "Chicken Pulao", "calories": 450, "protein": 35, "quantity": "1 bowl"}
        ],
        "Evening Snack": [
            {"meal": "Chicken Wings", "calories": 200, "protein": 25, "quantity": "3 wings"},
            {"meal": "Grilled Fish", "calories": 150, "protein": 30, "quantity": "1 fillet"},
            {"meal": "Egg Salad", "calories": 180, "protein": 15, "quantity": "2 eggs with salad"},
            {"meal": "Chicken Kebab", "calories": 250, "protein": 25, "quantity": "3 kebabs"},
            {"meal": "Tuna Salad", "calories": 220, "protein": 30, "quantity": "1 bowl"}
        ],
        "Dinner": [
            {"meal": "Chicken Biryani", "calories": 600, "protein": 40, "quantity": "1 plate"},
            {"meal": "Grilled Fish with Veggies", "calories": 450, "protein": 35, "quantity": "1 fillet with 1 cup veggies"},
            {"meal": "Egg Curry with Rice", "calories": 500, "protein": 30, "quantity": "1 bowl curry with 1 cup rice"},
            {"meal": "Mutton Rogan Josh with Naan", "calories": 650, "protein": 45, "quantity": "1 bowl rogan josh with 1 naan"},
            {"meal": "Chicken Shawarma", "calories": 550, "protein": 35, "quantity": "1 wrap"}
        ]
    }

    both_meals = {
        "Breakfast": veg_meals["Breakfast"] + non_veg_meals["Breakfast"],
        "Lunch": veg_meals["Lunch"] + non_veg_meals["Lunch"],
        "Evening Snack": veg_meals["Evening Snack"] + non_veg_meals["Evening Snack"],
        "Dinner": veg_meals["Dinner"] + non_veg_meals["Dinner"]
    }

    # Select meals based on preference
    if meal_preference == "Veg":
        meals = veg_meals
    elif meal_preference == "Non-Veg":
        meals = non_veg_meals
    else:
        meals = both_meals

    # Select random meals for each category
    selected_meals = {
        "Breakfast": random.choice(meals["Breakfast"]),
        "Lunch": random.choice(meals["Lunch"]),
        "Evening Snack": random.choice(meals["Evening Snack"]),
        "Dinner": random.choice(meals["Dinner"]),
    }

    # Generate a meal plan with calories and protein
    meal_plan = {
        "Breakfast": {
            "Meal": selected_meals["Breakfast"]["meal"],
            "Quantity": selected_meals["Breakfast"]["quantity"],
            "Calories": selected_meals["Breakfast"]["calories"],
            "Protein (g)": selected_meals["Breakfast"]["protein"]
        },
        "Lunch": {
            "Meal": selected_meals["Lunch"]["meal"],
            "Quantity": selected_meals["Lunch"]["quantity"],
            "Calories": selected_meals["Lunch"]["calories"],
            "Protein (g)": selected_meals["Lunch"]["protein"]
        },
        "Evening Snack": {
            "Meal": selected_meals["Evening Snack"]["meal"],
            "Quantity": selected_meals["Evening Snack"]["quantity"],
            "Calories": selected_meals["Evening Snack"]["calories"],
            "Protein (g)": selected_meals["Evening Snack"]["protein"]
        },
        "Dinner": {
            "Meal": selected_meals["Dinner"]["meal"],
            "Quantity": selected_meals["Dinner"]["quantity"],
            "Calories": selected_meals["Dinner"]["calories"],
            "Protein (g)": selected_meals["Dinner"]["protein"]
        },
        "Calories Target": calories_target,  # Add Calories Target here
        "Total Calories": calories_target,
        "Total Protein (g)": (selected_meals["Breakfast"]["protein"] +
                             selected_meals["Lunch"]["protein"] +
                             selected_meals["Evening Snack"]["protein"] +
                             selected_meals["Dinner"]["protein"])
    }

    return meal_plan
