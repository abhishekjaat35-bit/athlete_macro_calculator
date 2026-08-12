# ==========================================
# Athlete Macro Calculator
# Sports Science Python Project
# Author: Abhishek Tomar
# ==========================================

import pandas as pd


print("=" * 70)
print("                 ATHLETE MACRO CALCULATOR")
print("=" * 70)


# ------------------------------------------
# Load Athlete Data
# ------------------------------------------

data = pd.read_csv("athlete_data.csv")


# ------------------------------------------
# Display Athlete Data
# ------------------------------------------

print("\nATHLETE INFORMATION")
print("=" * 70)

print(data.to_string(index=False))


# ------------------------------------------
# Activity Factors
# ------------------------------------------

activity_factors = {
    "Low": 1.375,
    "Moderate": 1.55,
    "High": 1.725,
    "Very High": 1.90
}


# ------------------------------------------
# Macro Targets
# ------------------------------------------

protein_per_kg = 1.8
fat_per_kg = 0.8


# ------------------------------------------
# Calculation Functions
# ------------------------------------------

def calculate_bmr(sex, weight, height, age):
    """
    Calculate Basal Metabolic Rate using
    the Mifflin-St Jeor equation.
    """

    if sex.lower() == "male":
        bmr = (
            10 * weight
            + 6.25 * height
            - 5 * age
            + 5
        )

    elif sex.lower() == "female":
        bmr = (
            10 * weight
            + 6.25 * height
            - 5 * age
            - 161
        )

    else:
        raise ValueError(
            "Sex must be Male or Female."
        )

    return bmr


def calculate_macros(weight, calories):
    """
    Calculate protein, fat and carbohydrate
    targets from body weight and calorie target.
    """

    protein_grams = weight * protein_per_kg

    fat_grams = weight * fat_per_kg

    protein_calories = protein_grams * 4

    fat_calories = fat_grams * 9

    carbohydrate_calories = (
        calories
        - protein_calories
        - fat_calories
    )

    carbohydrate_grams = (
        carbohydrate_calories / 4
    )

    return (
        protein_grams,
        carbohydrate_grams,
        fat_grams
    )


# ------------------------------------------
# Calculate Athlete Results
# ------------------------------------------

results = []


for _, athlete in data.iterrows():

    name = athlete["Athlete"]
    age = athlete["Age"]
    sex = athlete["Sex"]
    height = athlete["Height_cm"]
    weight = athlete["Weight_kg"]
    activity = athlete["Activity_Level"]

    # Calculate BMR
    bmr = calculate_bmr(
        sex,
        weight,
        height,
        age
    )

    # Get activity factor
    activity_factor = activity_factors[activity]

    # Calculate estimated daily energy expenditure
    tdee = bmr * activity_factor

    # Use TDEE as calorie target
    calorie_target = tdee

    # Calculate macros
    protein, carbohydrates, fat = calculate_macros(
        weight,
        calorie_target
    )

    results.append({
        "Athlete": name,
        "BMR": bmr,
        "TDEE": tdee,
        "Calories": calorie_target,
        "Protein_g": protein,
        "Carbs_g": carbohydrates,
        "Fat_g": fat
    })


# ------------------------------------------
# Create Results DataFrame
# ------------------------------------------

results_df = pd.DataFrame(results)


# ------------------------------------------
# Display Results
# ------------------------------------------

print("\n" + "=" * 70)
print("ATHLETE NUTRITION TARGETS")
print("=" * 70)

print(
    results_df.to_string(
        index=False,
        formatters={
            "BMR": "{:.0f}".format,
            "TDEE": "{:.0f}".format,
            "Calories": "{:.0f}".format,
            "Protein_g": "{:.1f}".format,
            "Carbs_g": "{:.1f}".format,
            "Fat_g": "{:.1f}".format
        }
    )
)


# ------------------------------------------
# Detailed Athlete Reports
# ------------------------------------------

print("\n" + "=" * 70)
print("INDIVIDUAL ATHLETE REPORTS")
print("=" * 70)


for _, result in results_df.iterrows():

    print("\n" + "-" * 70)

    print(f"Athlete      : {result['Athlete']}")
    print(f"BMR          : {result['BMR']:.0f} kcal/day")
    print(f"Estimated TDEE : {result['TDEE']:.0f} kcal/day")
    print(f"Calorie Target : {result['Calories']:.0f} kcal/day")

    print("\nMacro Targets:")

    print(
        f"Protein      : "
        f"{result['Protein_g']:.1f} g/day"
    )

    print(
        f"Carbohydrate : "
        f"{result['Carbs_g']:.1f} g/day"
    )

    print(
        f"Fat          : "
        f"{result['Fat_g']:.1f} g/day"
    )


# ------------------------------------------
# Export Results
# ------------------------------------------

results_df.to_csv(
    "athlete_macro_results.csv",
    index=False
)


print("\n" + "=" * 70)
print("RESULTS SAVED")
print("=" * 70)

print(
    "File created: athlete_macro_results.csv"
)

print("\n" + "=" * 70)
print("MACRO CALCULATION COMPLETE")
print("=" * 70)