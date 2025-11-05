import json
import os

# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty or just whitespace. Please try again.")


# This function repeatedly prompts for input until an integer between 1 and max_value is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt, max_value):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            num = int(value)
            if 1 <= num <= max_value:
                return num
        print(f"Please enter an integer between 1 and {max_value}.")


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
    with open("data.txt", "w") as file:
        json.dump(data, file, indent=4)


# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
if os.path.exists("data.txt"):
    try:
        with open("data.txt", "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []
else:
    data = []


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "One Must Go" Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()
        
    if choice == 'a':
        # Add a new category.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        category_name = input_something("Enter the new category name: ")
        description = input_something("Enter the category description: ")
        data.append({"name": category_name, "description": description})
        save_data(data)
        print(f"Category '{category_name}' added successfully.")


    elif choice == 'l':
        # List the current categories.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        if data:
            print("\nCurrent categories:")
            for i, category in enumerate(data, start=1):
                print(f"{i}. {category['name']}")
        else:
            print("No categories found.")


    elif choice == 's':
        # Search the current categories.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        query = input_something("Enter search term: ").lower()
        results = [c for c in data if query in c['name'].lower() or query in c['description'].lower()]
        if results:
            print("\nSearch results:")
            for i, category in enumerate(results, start=1):
                print(f"{i}. {category['name']} - {category['description']}")
        else:
            print("No matching categories found.")


    elif choice == 'v':
        # View a category.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if data:
            print("\nWhich category would you like to view?")
            for i, category in enumerate(data, start=1):
                print(f"{i}. {category['name']}")
            index = input_int("Enter number: ", len(data))
            category = data[index - 1]
            print(f"\nName: {category['name']}\nDescription: {category['description']}")
        else:
            print("No categories to view.")


    elif choice == 'd':
        # Delete a category.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if data:
            print("\nWhich category would you like to delete?")
            for i, category in enumerate(data, start=1):
                print(f"{i}. {category['name']}")
            index = input_int("Enter number: ", len(data))
            removed = data.pop(index - 1)
            save_data(data)
            print(f"Category '{removed['name']}' deleted successfully.")
        else:
            print("No categories to delete.")


    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Bye!")
        break


    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice. Please try again.")
