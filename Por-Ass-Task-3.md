# Scenario
You are employed as a junior software developer at a boutique software house called Softwares-R-
Us in Perth.
You have been assigned to the Games team and will provide some of the code required for various
games that the company builds and releases.
You will be updating the existing code from the previous tasks to sort a list of players based on their
scores.

# Instructions
Your code must adhere to certain style guides, the most important being PEP-8 – Style Guide for
Python Code. You should familiarise yourself with PEP-8 before continuing.
Use of a Git repository is standard practice at Softwares-R-Us and most of the steps require the use
of Git and GitHub.
There are multiple steps in this task, and you must perform each step to a satisfactory level. Please
note that you’ll need the results of the tasks outlined in this assessment tool for future tasks as well.
You may answer any questions in the provided template (if available) and the use of screenshots is
encouraged. However, you must also provide the actual source code as a ZIP-file of the project for
any programming tasks. Make sure to remove the Virtual Environment folder (venv or .venv) from the
ZIP-file before uploading.
You must document your code properly. Use docstrings where needed including but not limited to
entire classes and methods. Use inline comments to clarify certain parts of code.
If you use any external resources, you should provide references.

## Step 1 – Knowledge Question (40-70 words)
In your own words, describe what sorting is in general.

    Take a collection of similar things, in a list or array, and put them in some sort of order. For example numbers can be put into ascending and descending order. If the collection are words it will be in alphabetical.

## Step 2 – Knowledge Question (60-100 words)
Research sorting algorithms. Describe advantages and disadvantages for at least three different
sorting algorithms. Please provide references for external resources.

    https://en.wikipedia.org/wiki/Sorting_algorithm

    Insertion sort
    Advantages
    - simple implementation
    - effective for small data sets
    - adaptive, is effective on mostly sorted data
    - stable, it doesn't change the order while sorting.
    - in place, needs a constant amount of extra memory for larger sets
    - online, values can be streamed into
    Disadvantages
    - average time n<sup>2</sup>
    - not good on large data sets
    https://en.wikipedia.org/wiki/Insertion_sort

    Bubble Sort
    Advantages
    - easy to learn
    - simple implementation
    - can be parallelisation
    Disadvantages
    - slow average n<sup>2<sup>
    - slower than other with same average
    https://en.wikipedia.org/wiki/Bubble_sort

    Advantages
    - fast on large data sets
    - has good memory usage
    - can be parallelisation
    Disadvantages
    - not good at very small data sets
    - with very large data sets need to make the call stack taller
    https://en.wikipedia.org/wiki/Quicksort

## Step 3 – Knowledge Question (20-50 words)
In your own words, describe why you generally need comparison operators to successfully sort a list of objects.

    It makes your code dry, easier to write and read because you override the dunder methods with your own comparison logic.

In addition, describe how you could sort a list of objects without adding comparison operators.

    When comparing objects you would need to say what in the objects want to compare.
    eg. if (player0.score > player1.score):

## Step 4 – Implement comparison operators and sort
In this step, you will be sorting a list of player objects based on their score. This step has multiple
parts to it.
### a. 
Add a private instance variable to the Player class that will hold the score (a positive integer value).
Provide a getter (property) and a setter method for this value.
### b. 
Implement the comparison operators __eq__, __ge__, etc.) for the Player class. Implement each so
that the comparison uses the score.
### c. 
Add unit tests to test the new operators.
### d. 
Implement a static method for the Player class that will sort a list of Player objects in descending
order (higher scores come first). Choose an algorithm of your liking based on the answers you
provided to the Knowledge Questions and describe why you chose it.

    I chose quicksort for two reasons 1, it is efficient in time and space complexity as outlined in the advantages section. 2, from the lecture it was the only one I did't understand and I wanted to learn it.
     
IMPORTANT: you must implement this algorithm yourself; you may not use Python’s sort method.
### e. 
Add unit tests to test the new sorting functionality.
### f. 
Add and commit all changes, then push your changes to the remote repository on GitHub

https://meta.stackexchange.com/questions/226869/how-can-i-add-the-mathematical-symbol-for-power-like-x-2-to-a-question