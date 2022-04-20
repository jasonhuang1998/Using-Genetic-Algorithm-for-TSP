# Using Genetic Algorithm for TSP

## Table of Content
- [Introduction](#Introduction)
- [Input File](#Input-File)
- [Input](#Input)
- [Output](#Output)
- [Usage](#Usage)
- [Requirments](#Requirments)

## Introduction
* The code for Artificial Intelligence cources at NCUE.
* Using Genetic Algorithm to implement Travelling salesman problem(TSP).
* Two ways of mating and mutation  are designed.

## Input File
* Integer n in the first line means that there are n nodes 
* The second line to the n+1<sup>th</sup> line is a n*n matrix
* The elements in the matrix mean the distance between a node to another, and the elements must be positive integer or 0(means that there is no edge between those nodes).
* A connection from a node to itself is not permitted(all diagonal element are 0).
* All elements in the matrix are seperated by space.

Example:  
5  
0 1 2 3 4  
3 0 3 5 7  
4 6 0 5 1  
3 1 9 0 7  
1 4 8 5 0  


## Input 
* Crossover probability
* Mutation probability
* Population size
* Generation

## Output
* The best, worst, average cost of each generation
* Computing time
* Using matplotlib to draw the graph, including best, worst, average cost

## Usage
```
pip install -r requirements.txt
pip main.py
```

## Requirements
* matplotlib
