'''
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18
'''
def main():
    # Input for Team 1
    print("Team 1:")
    team1_name = input("Team Name: ")
    team1_score = input("Score: ")
    team1_overs = input("Overs played: ")
    
    # Input for Team 2
    print("Team 2:")
    team2_name = input("Team name: ")
    team2_score = input("Score: ")
    team2_overs = input("Overs played: ")

    # Display Match Details
    print("\nMatch Details:")
    print(f"Team 1: Name: {team1_name} Score: {team1_score} Overs played: {team1_overs}")
    print(f"Team 2: Name: {team2_name} Score: {team2_score} Overs played: {team2_overs}")

if __name__ == "__main__":
    main()

