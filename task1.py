def get_name():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Please try again.")
        return get_name()
    return name

def get_age():
    while True:
        age_input = input("Enter your age: ")
        try:
            age = int(age_input)
            if age <= 0:
                print("Age must be a positive number. Please try again.")
                continue
            return age
        except ValueError:
            print("Please enter a valid number for age.")

def main():
    name = get_name()
    age = get_age()
    print(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    main()