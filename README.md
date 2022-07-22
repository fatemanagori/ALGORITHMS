# ALGORITHMS_DEPTH-FIRST-SEARCH_MAZE
<img width="304" alt="Maze" src="https://user-images.githubusercontent.com/109574120/180377033-f3ed310c-8e9b-4666-bb9e-087da9af7393.png">

**DESCRIPTION**

**To solve Maze there are 2 approaches:**

[DEPTH-FIRST SEARCH](https://youtu.be/W9F8fDQj7Ok)

[BREADTH-FIRST SEARCH](https://youtu.be/hettiSrJjM4)


In this Project we solve maze using **Depth First Search(DFS)** approach, we also demonstrate manual solution to find the shortest path of MAZE that has clear spaces (like Robots without wheel)  using **TREE** and the manual solution for MAZE with unclear route(like self driving cars with wheels) using **MATRIX** , both the methods are used to analyse the cost, time and business it can provide in real time.






**ANALYSIS**

The shortest path can be find using Depth-First Search and Breadth-First Search . However In this project  Depth-First Search is used to find shortest path successfully. For the Leetcode question both the approaches takes same time and space, but in general For mazes specifically (if we define a maze as there being only one way to reach a cell from the starting point without backtracking, meaning it's essentially a tree), **BFS** will generally use more memory, as we'll need to keep multiple paths in memory at the same time, where **DFS** only needs to keep track of a single path at any given time.





**INSTALLATION**

I use python and [pipenv](https://docs.pipenv.org/) as a primary tools for 
development. See [Pipfile](Pipfile), [Pipfile.lock](Pipfile.lock), 
[requirements-dev.txt](requirements-dev.txt)(if any) and
[requirements.txt](requirements.txt) for full specification of 
platform, python and dependency packages.  
Basically, to reproduce enviroment, you need to run `pip install -r 
requirements.txt` with certain [version of python](Pipfile.lock#L15). However, 
it is recommended to use [virtualenv](https://virtualenv.pypa.io/en/stable/).

[MAZE_DEPTH-FIRST SEARCH](https://docs.google.com/presentation/d/1qfbWG4AkeXxGv2HY4-Xgng8I6K4pJeYjv_3et40Tb_c/edit#slide=id.g13d8509030d_0_31)




**CREDIT**

Special Thanks to **Prof Henry Chang** for providing guidence throughout this project
