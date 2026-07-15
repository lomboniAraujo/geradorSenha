import random
import string


def generate_password(length: int) -> str:
    """Return a random password of the requested length."""
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def prompt_for_int(prompt: str, minimum: int) -> int:
    """Prompt the user until they provide a valid integer greater than or equal to minimum."""
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def display_passwords(passwords: list[str]) -> None:
    """Print the generated passwords in an organized, numbered list."""
    print("\nGenerated passwords:")
    for index, password in enumerate(passwords, start=1):
        print(f"{index}. {password}")


def main() -> None:
    print("Password Generator")
    print("===================")

    count = prompt_for_int("How many passwords would you like to generate? ", 1)
    length = prompt_for_int("Enter desired password length for each password (minimum 4): ", 4)

    passwords = [generate_password(length) for _ in range(count)]
    display_passwords(passwords)


if __name__ == "__main__":
    main()
