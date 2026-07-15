git init
git add password_generator.py README.md
git commit -m "Add password generator"
git remote add origin <your-github-repo-url>
git push -u origin mainimport random
import string


def generate_password(length: int) -> str:
    """Generate a random password containing letters, digits, and symbols."""
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def prompt_for_length() -> int:
    while True:
        try:
            value = int(input("Enter desired password length (minimum 4): "))
            if value < 4:
                print("Please enter a number greater than or equal to 4.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main() -> None:
    length = prompt_for_length()
    password = generate_password(length)
    print("\nGenerated password:")
    print(password)


if __name__ == "__main__":
    main()
