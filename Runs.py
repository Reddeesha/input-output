'''
Extras are runs scored by a means other than a batsman hitting the ball. A batsman is not given credit for extras other than runs scored off the bat from a no ball, and the extras are tallied separately on the scorecard and count only towards the team’s score. the types of extras are No ball, Wide, Bye, Leg-bye and Penalty. 1 Penalty corresponds to 5 runs.
Find the total runs that the Extras contribute to the team’s score, given the number of No-balls, wides, byes, leg-byes and penalty given off by the bowlers in innings.
'''
def main():
    # Input for extra runs
    no_balls = int(input("Enter the number of No-balls: "))
    wides = int(input("Enter the number of Wides: "))
    byes = int(input("Enter the number of Byes: "))
    leg_byes = int(input("Enter the number of Leg-byes: "))
    penalty_runs = int(input("Enter the number of Penalty runs: "))

    # Calculate total extra runs
    total_extra_runs = (no_balls + wides + byes + leg_byes + penalty_runs)

    # Display extra runs details
    print("\nExtra Runs Details:")
    print(f"No-balls: {no_balls}")
    print(f"Wides: {wides}")
    print(f"Byes: {byes}")
    print(f"Leg-byes: {leg_byes}")
    print(f"Penalty runs: {penalty_runs}")
    print(f"Total Extra Runs: {total_extra_runs}")

if __name__ == "__main__":
    main()
