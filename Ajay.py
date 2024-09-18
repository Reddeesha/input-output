'''
Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a python program to find the midpoint of the line. Input Format: Input consists of 4 integers. The first integer corresponds to x1 . The second integer corresponds to y1. The third and fouth integers correspond to x2 and y2 respectively. Output Format: Refer Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 1 decimal place]
 
Input (stdin)
2
4
10
15
 
Output (stdout)
Binoy's house is located at (6.0,9.5)
10)
'''
def main():
    # Input for the coordinates of the endpoints
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    # Calculate the midpoint
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    # Display the result
    print(f"Binoy's house is located at ({midpoint_x:.1f},{midpoint_y:.1f})")

if __name__ == "__main__":
    main()
Ajay, Binoy, and Chandru decide to play a game of distance calculation. Each of them will give their house coordinates and they need to calculate the distance between Ajay's house and Chandru's house. Given the coordinates of the 2 endpoints of a line (x1,y1)(x_1, y_1)(x1​,y1​) and (x2,y2)(x_2, y_2)(x2​,y2​), write a Python program to find the distance between the points.
Input Format
Input consists of 4 integers. The first integer corresponds to x1x_1x1​. The second integer corresponds to y1y_1y1​. The third and fourth integers correspond to x2x_2x2​ and y2y_2y2​ respectively.
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]
Sample Input
3
4
6
8

Sample Output
The distance between Ajay's house and Chandru's house is 5.00

import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"The distance between Ajay's house and Chandru's house is {distance:.2f}")
