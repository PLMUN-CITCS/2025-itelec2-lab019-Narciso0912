def get_grade(score):
    """Determines the letter grade based on the given score."""
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def main():
    """Handles user input and displays the grade."""
    try:
        score = int(input("Enter your score: "))
        if 0 <= score <= 100:
            grade = get_grade(score)
            print(f"Your Grade is: {grade}")
        else:
            print("Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Run the program
main()
