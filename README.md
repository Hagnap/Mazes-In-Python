# Mazes-In-Python
This project is a collection of Maze Algorithms found in the book "Mazes for Programmers". This project was done to serve as a reference for when I implement this in Unity.

### How Mazes Work
Mazes are created using a 2D Array of Nodes but what are Nodes?

##### What are Nodes?
Nodes are spots in the maze. Each node has its own unique X and Y (row and column) coordinates. The nodes also store values that show if its Open, Closed/Walled Off, or Non-Accessible (Mask marked it unaccissble). These values are used during maze generation.
  - Open: '0'
  - Closed/Walled Off: '■' (alt code 254)
  - Non-Accessible: '-1'

Other than that Nodes references to their four neighbors (North, East, South, and West) and its parent. The parent reference is used when calculating the distance from the starting point of the maze.

### How Mazes Work (Continued)
When generating mazes, an empty maze is what the program starts with and then uses the specified maze algorithm to generate walls. Once walls are generated a random starting point is selected and then the program calculates this distance of each node from the starting point. If a node can not be accessed from the starting point it is assigned a value of -1. This helps show the node can not be accessed when the maze distances are printed out. 

### Maze Alogirthms
All of these algorithms are dependent on a 'coin flip'. This is emulated by getting a random number between 0.0 and 1.0, if its greater than .5 then a wall is placed, otherwise no wall is placed. 

***Binary Tree***
  * The Binary Tree algorithm will traverse the maze and will only add walls to the North or East of the current node. A coinflip is done to see if a wall will be added to the north, if no wall will be added then we do another coin flip but for the east neighbor. If the value is less than 0.5 for both the North and East then no wall will be added. 
  
***Sidewinder***
  * ToDo: Fill out info 
  
***Aldous Broder***
  * ToDo: Fill out info

***Wilsons***
  * ToDo: Fill out info

***Hunt and Kill***
  * ToDo: Fill out info

***Recursive Backtracking***
  * ToDo: Fill out info

***Test***
  * This algorithm is used to ensure everything runs fine and has no real purpose outside of that. It traverses every node and does a random coin flip to determine if a wall should be placed or not.

### Masks
*What is a mask?* A mask is like a layout for a maze. The mask can be used to create various designs on a maze by telling the maze which areas are accessible or not when generating the maze. 

Three masked are in this repo but the user can create more. This is done by making a text file and using 0s to mark open areas on the mask and 1s to mark as closed off areas. You can view the provided masks to get an idea of they can be created.  

### Conclusion
This program was a part of a passion project where I got to use algorithms that were new to me and improve my Python skills, however if you have any questions regarding the implementation feel free to contact me at jhaggard@gmail.com
