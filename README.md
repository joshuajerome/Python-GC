# Python Graphing Calculator Project

Find out more about me on [my site](https://sites.google.com/view/sherwin-jeromes-page/home)!

## About the Project

This was an invite-only project designed by my AP Computer Science teacher for the top two performing students in each of his classes. The APCS cirriculum taught Java programming language, but this project was in Python. Furthermore, this project focussed on Lambda functions. Students were expected to have no programming experience in Python, and were to code only in terminal. IDEs were restricted so students could find and resolve errors by themselves.

We used Python 3.7 (latest python version) at the time of this project.

## Starting the Project

Students were first taught what lambda functions were: small functions that could take _n_ number of arguments, but can only have one expression. Next, students were shown an example of very basic functions:

```markdown

import math
f = lambda x: 2 + x  `returns the sum of 2 and any given number`
g = lambda x: 2 * x `returns the product of 2 and any given number`

```

Using this basic understanding of functions, the next step was creating a _doTwice_ function which would essentially do a function twice. Students were expected to code this on their own which posed a challenge as we had to use our programming knowledge of Java to find a solution. For each succeding function, our teacher would conceptually describe its purpose and leave the coding to students. Students could not ask for help, search up solutions, and upon completion had to explain each piece in the one line of code.

## Goal

Ultimately, students would use their new-found knowledge of Lambda functions to write code for a fully functional graphing calculator. Features of the calculator include:

- returning a string with proper character syntax such that it could be copied and pasted into an online graphing utility such as [Desmos](https://www.desmos.com/calculator)
- Lagrange Interpolation
- Approxmation of Sine and Cosine up to 14 decimal points
- Polynomial arithmetics
- Differentiation and Integration

Upon completion of the Graphing Calculator, students were also asked to create Merge Sort and Binary Search Functions

## Code

All the code is listed with description in function.py. Running main.py will output a string that can be pasted into desmos or any online graphing utility to see the lagrange approximation.

## Video Example

Here is a [link](https://www.youtube.com/watch?v=CYzYW3znVHo&list=PL31HaAenzL5NA_1_7AqDwY1RZdEqE6jRM) to the video
