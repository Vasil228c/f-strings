def main():
    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        age_input = input("Enter your age: ")
        try:
            age = int(age_input)
            if age <= 0:
                print("Age must be a positive number. Please try again.")
                continue
        except ValueError:
            print("Please enter a valid number for age.")
            continue

        hobby = input("Enter your hobby: ").strip()
        if not hobby:
            print("Hobby cannot be empty. Please try again.")
            continue

        city = input("Enter your city: ").strip()
        if not city:
            print("City cannot be empty. Please try again.")
            continue

        print(f"Hello, {name}! You are {age} years old, live in {city}, and your hobby is {hobby}.")
        break

if __name__ == "__main__":
    main()