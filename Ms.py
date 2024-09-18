'''
MS Dhoni is a grade A player according to BCCI Central Contracts in 2016. MSD's net worth in 2016 is around 31 million and is said to be the richest Indian cricketer.
Apart from his salary as an Indian cricketer, Dhoni endorses various popular brands and earns a large amount from endorsements. Besides that individual and team bonuses are also given on the basis of individual and team performances. So precisely the sources of income for Dhoni are from - Salary, Bonuses and Awards through Winning and Endorsements.
'''
def main():
    # Input for income sources
    salary = int(input("Enter Dhoni's income from Salary (in rupees): "))
    bonuses = int(input("Enter Dhoni's income from Bonuses and Awards (in rupees): "))
    endorsements = int(input("Enter Dhoni's income from Endorsements (in rupees): "))

    # Calculate total income
    total_income = salary + bonuses + endorsements

    # Display income details
    print("\nIncome Details:")
    print(f"Salary: {salary} rupees")
    print(f"Bonuses and Awards: {bonuses} rupees")
    print(f"Endorsements: {endorsements} rupees")
    print(f"Total Income: {total_income} rupees")

if __name__ == "__main__":
    main()
