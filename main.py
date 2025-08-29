from pathlib import Path 
from participant_pkg.file_ops import save_participant, load_participants  # # Import helper functions

def get_valid_input(prompt, validator, error_msg):
    while True:
        value = input(prompt)  # Get user input
        if validator(value):   # Check if input is valid
            return value       # Return valid input
        print(error_msg)        # Show error message

def main():
    csv_path = Path("contacts.csv")  # Define the CSV file path
    print("Welcome to Contact Saver!\n")

    while True:  # Loop to add multiple participants
        name = get_valid_input(
            "\tEnter participant name: ",
            lambda x: len(x.strip()) > 0,  # Name must not be empty
            "Name cannot be empty. Please try again."
        )

        # Age input and validation
        while True:
            age_input = input("\tEnter participant age: ")  # Prompt for age
            try:
                age = int(age_input)  # try converting age to integer
                if age > 0:
                    break
                else:
                    print("Age must be a positive number.")
            except ValueError:
                print("Invalid age. Please enter a number.")

        # Get and validate phone number
        phone = get_valid_input(
            "\tEnter phone number: ",
            lambda x: x.isdigit() and len(x) == 11,
            "Phone number must be 11 digits. Please try again."
        )
        
        # Get and validate track
        track = get_valid_input(
            "\tEnter participant track: ",
            lambda x: len(x.strip()) > 0,
            "Track cannot be empty. Please try again."
        )
        
        # Store participant details in a dictionary
        participant = {
            "Name": name.strip(),
            "Age": age,
            "Phone": phone,
            "Track": track.strip()
        }

        # Save participant details to CSV file 
        try:
            save_participant(csv_path, participant)
            print("Participant saved successfully!\n")
        except Exception as e:
            print(f"Error saving participant: {e}")

        # Ask if user want to add another participant
        more = input("Add another participant? (yes/no): ").lower()
        if more != 'yes':
            break

    # Load and display all participants
    try:
        participants = load_participants(csv_path)
        print("\n=== Workshop Participants Summary ===")
        print(f"Total participants: {len(participants)}")
        for i, p in enumerate(participants, 1):
            print(f"{i}. {p['Name']} (Age: {p['Age']}, Phone: {p['Phone']}, Track: {p['Track']})")
    except Exception as e:
        print(f"Error loading participants: {e}")

if __name__ == "__main__":
    main()