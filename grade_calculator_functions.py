def get_student_score() -> float:
    """
    Prompts the user to enter a score and returns it as a float.
    
    Returns:
        float: The student's score.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            # Check if the score is within a reasonable range
            if score < 0 or score > 100:
                print("Please enter a valid score between 0 and 100.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the score.
    
    Args:
        score (float): The student's score.
    
    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# Main Program Flow
def main():
    # Get the student's score
    score = get_student_score()
    
    # Calculate the grade based on the score
    grade = calculate_grade(score)
    
    # Display the grade
    print(f"Your Grade is: {grade}")


if __name__ == "__main__":
    main()
