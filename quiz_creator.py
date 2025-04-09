import os


def questions_getter():
    """Get a question from the user."""
    while True:
        # Prompt the user to enter a question
        question = input("\nEnter your question: ").strip()
        if question:
            # Return the question if it is not empty
            return question
        # Notify the user that the question cannot be empty
        print("Question cannot be empty!")


def choices():
    """Get four possible answers from the user."""
    letters = ['a', 'b', 'c', 'd']
    answers = []

    # Loop through each letter to get four answers
    for letter in letters:
        while True:
            # Prompt the user to enter an answer for the current letter
            answer = input(f"\nEnter answer ({letter}): ").strip()
            if answer:
                # Append the answer to the list if it is not empty
                answers.append(answer)
                break
            # Notify the user that the answer cannot be empty
            print("Answer cannot be empty!")
    # Return the list of answers
    return answers


def correct_answer():
    """Get the correct answer from the user."""
    letters = ['a', 'b', 'c', 'd']

    while True:
        # Display the prompt to select the correct answer
        print("\nSelect the correct answer:")
        answers = choices()

        # Display the answers with their corresponding letters
        for letter, answer in zip(letters, answers):
            print(f"{letter}. {answer}")

        # Prompt the user to enter the letter of the correct answer
        choice = input("Enter the letter of the correct answer: ").lower().strip()
        if choice in letters:
            # Return the correct answer if the input is valid
            return choice
        # Notify the user of invalid input
        print("Invalid choice! Please enter a, b, c, or d.")


def quiz_question_saver(question, answers, correct_answer, filename="quiz_record.txt"):
    """Save the quiz data to a text file."""
    # Open the file in append mode
    with open(filename, 'a') as f:
        # Write the question to the file
        f.write(f"Question: {question}\n")

        # Write each answer with its corresponding letter
        letters = ['a', 'b', 'c', 'd']
        for letter, answer in zip(letters, answers):
            f.write(f"{letter}. {answer}\n")

        # Write the correct answer to the file
        f.write(f"Correct answer: {correct_answer}\n\n")


def display_menu():
    """Display the main menu."""
    # Print the menu options
    print("\n=== Quiz Creator Menu ===")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Exit")


def main():
    """Main function to run the quiz creator."""
    filename = "quiz_record.txt"

    # Welcome message for the user
    print("Welcome to Quiz Creator!")
    print("Add questions to your quiz. Press Ctrl+C to finish.")

    try:
        while True:
            # Display the main menu
            display_menu()

            # Prompt the user to select an option
            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == '1':
                # Add a new question to the quiz
                question = questions_getter()
                answers = choices()
                correct_answer_value = correct_answer()
                quiz_question_saver(question, answers, correct_answer_value)
                print("\nQuestion added successfully!")
            elif choice == '2':
                # View all saved questions
                if os.path.exists(filename) and os.path.getsize(filename) > 0:
                    with open(filename, 'r') as f:
                        print("\n=== Available Questions ===")
                        print(f.read())
                else:
                    # Notify the user if no questions are available
                    print("\nNo questions available!")
            elif choice == '3':
                # Exit the program
                print("\nQuiz creation completed!")
                print(f"All questions have been saved to {filename}")
                break
            else:
                # Notify the user of invalid input
                print("Invalid choice! Please enter a number between 1 and 3.")

    except KeyboardInterrupt:
        # Handle the user pressing Ctrl+C to exit
        print("\n\nQuiz creation completed!")
        print(f"All questions have been saved to {filename}")


if __name__ == "__main__":
    main()