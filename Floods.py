'''
Tamilnadu was battling one if it’s worst floods in a century last December, as several part of the state have been submerged and cut off from essential supplies. It was heartening that the Cricketers came forward to contribute for the cause of floods and it was decided amongst the team that the senior players donate 50% of their salary and junior players to donate 40% against the flood relief measures
Assume there are 6 senior players and 5 junior players. The salary of senior players Rs.X and that of junior players is Rs.Y. Find the total contribution from the cricket team towards the floods.
'''
def main():
    # Input for salaries
    senior_salary = int(input("Enter the salary of senior players (in rupees): "))
    junior_salary = int(input("Enter the salary of junior players (in rupees): "))

    # Display salary details
    print("\nSalary Details:")
    print(f"Salary of Senior Players: {senior_salary} rupees")
    print(f"Salary of Junior Players: {junior_salary} rupees")

if __name__ == "__main__":
    main()
