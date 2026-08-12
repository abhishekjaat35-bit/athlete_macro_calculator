# 🥗 Athlete Macro Calculator

A Python sports-science project that estimates daily energy requirements and macronutrient targets for athletes using basic anthropometric and activity data.

The project combines Python, Pandas, nutritional calculations, and sports-science concepts to produce structured athlete nutrition targets.

---

## 🎯 Project Objective

The program calculates:

- Basal Metabolic Rate (BMR)
- Estimated Total Daily Energy Expenditure (TDEE)
- Daily calorie target
- Protein target
- Carbohydrate target
- Fat target

The results are also exported to a CSV file for further analysis.

---

## 📊 Data Flow

```text
Athlete Profile
      ↓
Age
Sex
Height
Weight
Activity Level
      ↓
BMR
      ↓
Activity Factor
      ↓
Estimated TDEE
      ↓
Calorie Target
      ↓
Protein + Fat
      ↓
Remaining Calories
      ↓
Carbohydrate Target
      ↓
Athlete Nutrition Report
```

---

## 🧮 Calculations

### Basal Metabolic Rate

The project uses the Mifflin-St Jeor equation.

For males:

```text
BMR =
10 × Weight
+ 6.25 × Height
− 5 × Age
+ 5
```

For females:

```text
BMR =
10 × Weight
+ 6.25 × Height
− 5 × Age
− 161
```

---

## 🔥 Activity Factors

The project uses the following activity multipliers:

| Activity Level | Factor |
|---|---:|
| Low | 1.375 |
| Moderate | 1.55 |
| High | 1.725 |
| Very High | 1.90 |

Estimated daily energy expenditure:

```text
TDEE = BMR × Activity Factor
```

---

## 💪 Macronutrient Targets

The example calculation uses:

```text
Protein = 1.8 g/kg body weight
Fat = 0.8 g/kg body weight
```

Calories are calculated using:

```text
Protein = 4 kcal/g
Carbohydrate = 4 kcal/g
Fat = 9 kcal/g
```

Carbohydrate is calculated from the remaining calorie budget:

```text
Carbohydrate Calories =
Total Calories
− Protein Calories
− Fat Calories
```

Then:

```text
Carbohydrate grams =
Carbohydrate Calories ÷ 4
```

---

## 📁 Project Structure

```text
athlete-macro-calculator/
│
├── athlete_macro_calculator.py
├── athlete_data.csv
├── athlete_macro_results.csv
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🗂️ Dataset

The input dataset contains:

| Variable | Description |
|---|---|
| Athlete | Athlete identifier |
| Age | Age in years |
| Sex | Biological sex used by the selected BMR equation |
| Height_cm | Height in centimeters |
| Weight_kg | Body mass in kilograms |
| Activity_Level | Estimated activity category |

The supplied dataset contains synthetic data for educational purposes.

---

## 🐍 Technologies Used

- Python
- Pandas
- CSV
- Functions
- Dictionaries
- Loops
- Conditional statements
- DataFrames
- Mathematical calculations
- CSV export

---

## ⚙️ Installation

Install Pandas:

```bash
pip install pandas
```

---

## ▶️ How to Run

Open a terminal inside the project folder.

Run:

```bash
python athlete_macro_calculator.py
```

The program reads:

```text
athlete_data.csv
```

and creates:

```text
athlete_macro_results.csv
```

---

## 📈 Example Results

| Athlete | Calories | Protein | Carbohydrate | Fat |
|---|---:|---:|---:|---:|
| Rahul | ~3041 kcal | 140.4 g | ~375.0 g | 62.4 g |
| Arjun | ~3411 kcal | 144.0 g | ~464.6 g | 64.0 g |
| Vikram | ~2579 kcal | 129.6 g | ~361.3 g | 57.6 g |
| Priya | ~2321 kcal | 108.0 g | ~307.4 g | 48.0 g |

---

## 🔬 Sports Science Application

Nutrition calculations can support athlete monitoring and planning by providing an initial framework for estimating energy and macronutrient requirements.

Potential applications include:

- Athlete nutrition monitoring
- Strength and conditioning support
- Training-day nutrition planning
- Performance nutrition analysis
- Athlete database development
- Sports performance dashboards

---

## ⚠️ Scientific Limitations

This calculator provides **estimates**, not individualized clinical nutrition prescriptions.

Actual energy expenditure can vary substantially according to:

- Training volume
- Training intensity
- Sport
- Body composition
- Non-exercise activity
- Metabolic differences
- Recovery demands
- Competition schedule
- Environmental conditions

The Mifflin-St Jeor equation is an estimation equation and should not be treated as a direct measurement of energy expenditure.

The protein, carbohydrate, and fat values in this project are example programming targets rather than individualized nutrition recommendations.

For real athletes, nutrition planning should be individualized using appropriate assessment and qualified sports-nutrition guidance.

---

## 🚀 Future Improvements

Planned improvements:

- [ ] Add goal selection
- [ ] Add weight-gain calculations
- [ ] Add weight-loss calculations
- [ ] Add maintenance calculations
- [ ] Add training-day calories
- [ ] Add rest-day calories
- [ ] Add sport-specific carbohydrate targets
- [ ] Add body-composition data
- [ ] Add meal distribution
- [ ] Add weekly nutrition tracking
- [ ] Add athlete dashboard
- [ ] Add visualization with Matplotlib
- [ ] Add automated nutrition reports

---

## 🧠 Skills Demonstrated

```text
Python
   ↓
Functions
   ↓
Dictionaries
   ↓
Pandas
   ↓
Data Processing
   ↓
Scientific Calculations
   ↓
Macronutrient Calculation
   ↓
CSV Export
   ↓
Sports Nutrition Analytics
```

---

## 👨‍💻 Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

---

## 📜 License

This project is licensed under the MIT License.

---

## 📌 Project Status

Completed ✅