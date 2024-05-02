# Essay Number 1 of Basic Programming
# Create a program to calculate the current age based on the input year of birth
# Name : Muhammad Fasya Surya Nugraha
# NIM : 20230040060

def calculate_age(year_of_birth):
    current_year = 2024  # Assuming the current year of today is 2024
    age = current_year - year_of_birth
    return age

def main():
    year_of_birth = int(input("Enter your year of birth: "))
    age = calculate_age(year_of_birth)
    print("Your current age is:", age)

if __name__ == "__main__":
    main()