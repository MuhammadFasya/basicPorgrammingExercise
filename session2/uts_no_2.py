# Essay Number 2 of Basic Programming
# Create a program to calculate monthly installments on a motorbike loan at a price according to the input (for example 15 million rupiah) and interest of 2% per month for 3 years.
# Name : Muhammad Fasya Surya Nugraha
# NIM : 20230040060
def calculate_installment(principal, interest_rate, duration):
  monthly_interest_rate = interest_rate / 100 / 12
  number_of_payments = duration * 12
  installment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
  return installment

def main():
  price = float(input("Enter the price of the motorbike (in million rupiah): "))
  interest_rate = 2  # 2% interest rate per month
  duration = 3  # 3 years
  principal = price * 1000000  # convert million rupiah to rupiah
  installment = calculate_installment(principal, interest_rate, duration)
  print("Monthly installment for the motorbike loan: {:.2f} rupiah".format(installment))

if __name__ == "__main__":
  main()