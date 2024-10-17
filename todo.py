import os

# Function to display menu options
def display_menu():
    print("1. View Notes")
    print("2. Add a Note")
    print("3. Delete a Note")
    print("4. Exit")

# Function to view notes
def view_notes():
    if not os.path.exists("notes.txt"):
        print("No notes found.")
    else:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes found.")
            else:
                print("Your Notes:")
                for note in notes:
                    print("- " + note.strip())

# Function to add a note
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")

# Function to delete a note
def delete_note():
    view_notes()
    try:
        note_number = int(input("Enter the number of the note to delete: ")) - 1
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        with open("notes.txt", "w") as file:
            for i, note in enumerate(notes):
                if i != note_number:
                    file.write(note)
        print("Note deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
