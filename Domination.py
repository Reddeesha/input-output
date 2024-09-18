'''
It were the days of domination from the traditional metros in the team selections and everytime the team is announced for the Indian Squad, mere disappointment was left with this small town player. Dhoni’ill fate continued even during the team selections for the India A squad to tour to Zimbabwe.3 new players from Mumbai were on the list for the Indian team and it was claimed by the selectors that Dhoni was a bit younger than the 3 selected players.
  Assume the 3 players are Named X,Y and Z. The ages of the players X and Y are the same and the age of the Z is 10 more than other 2 players. Given the total age of the 3 players, find the age of the 3 players.
Input format:
First line of the input is an integer that corresponds to the total age of the 3 players.
Output format:
Output should display the ages of the three players in 3 lines. The age of the eldest player should be displayed in the last line.
Sample input and output 1:
70
20
20
30
Sample input and output 2:
100
30
30
40
7)
You are given principal amount, rate of interest per annum, and time in years. You need to calculate the simple interest.
'''
def main():
    # Input for principal amount, rate, and time
    principal = float(input("Enter the principal amount (in rupees): "))
    rate = float(input("Enter the rate of interest (per annum in %): "))
    time = float(input("Enter the time (in years): "))

    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100

    # Display the calculated simple interest
    print(f"\nSimple Interest: {simple_interest:.2f} rupees")

if __name__ == "__main__":
    main()
  def main():
    # Input for temperature in Celsius
    celsius = float(input("Enter temperature in Celsius: "))

    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Display the temperature in Fahrenheit
    print(f"\nTemperature in Fahrenheit: {fahrenheit:.2f}")

if __name__ == "__main__":
    main()

