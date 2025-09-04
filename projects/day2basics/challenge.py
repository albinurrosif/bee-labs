print("=== ENHANCED STUDY PLANNER ===")

# Get user inputs
name = input("Enter your name: ").title()

# Validate study hours input
while True:
    try:
        study_hours = float(input("Enter target study hours (0-12): "))
        if 0 <= study_hours <= 12:
            break
        else:
            print("Please enter between 0-12 hours!")
    except ValueError:
        print("Please enter a valid number!")

# Get additional info
subject = input("What subject are you studying? ")

# Calculations
total_minutes = study_hours * 60
recommended_breaks = int(total_minutes / 50)  # Break every 50 minutes

# Enhanced output
print(f"\n{'='*50}")
print(f"STUDY PLAN FOR {name.upper()}".center(50))
print(f"{'='*50}")
print(f"📚 Subject: {subject}")
print(f"⏰ Total Study Time: {study_hours:.1f} hours ({total_minutes} minutes)")
print(f"☕ Recommended Breaks: {recommended_breaks} sessions")
print(f"{'='*50}")

if study_hours >= 4:
    print("💪 Amazing commitment! Remember to take breaks!")
else:
    print("🎯 Good start! Every minute counts!")