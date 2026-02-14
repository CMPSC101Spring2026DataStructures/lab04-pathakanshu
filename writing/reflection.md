# Reflection: Rock, Paper, Scissors Lab

Name: Anshu Pathak
Date: 2026-02-13

Please answer the following questions after you have completed the programming lab. Write your answers in complete sentences and provide thoughtful responses.

## Comprehension Questions

1. What is the purpose of breaking a program into functions? How did this help you in completing the lab?

Your Response:

Breaking the program into functions made the code easier to read and debug. It helped me focus on one small task at a time, like just checking who won or just getting the user's input, instead of dealing with everything at once.


2. Describe how you validated user input in your version of the Rock, Paper, Scissors game. Why is input validation important?

Your Response:

I used a while loop to keep asking the user for input until they typed 1, 2, 3 or the words rock, paper, or scissors. Validation is important so the program doesn't crash if someone types something random.

3. How did you use comments and docstrings in your code? Give an example of a helpful comment or docstring you wrote.

Your Response:

I used docstrings at the start of every function to explain what it does and what it returns. For example, my docstring for `determine_winner` says it returns "user", "computer", or "tie", which helped me remember what to check for later.

4. Explain how the computer's move is generated in your program. What Python features did you use to accomplish this?

Your Response:

I used the `random` library that comes with Python. Specifically, I used `random.choice(choices)` to pick a random item from the list of rock, paper, and scissors.

5. What was the most challenging part of refactoring the spaghetti code into a more structured program? How did you overcome this challenge?

Your Response:

The hardest part was figuring out which variables needed to be passed into functions and which ones could stay local. I fixed it by looking at the errors and seeing which variables were undefined, then adding them as arguments.

## Ethical Reflection Questions

1. Why is it important to write code that is easy for others to read and maintain? How does this relate to your responsibilities as a programmer?

Your Response:

It's important because other people (or me in the future) need to understand the code to fix bugs or add features. As a programmer, I'm responsible for making sure my work isn't a mess for the next person.

2. Consider the use of open source code (like the spaghetti code provided). What are some ethical considerations when using, modifying, or sharing code written by others?

Your Response:

When using code from others, you have to respect their license and give them credit. You shouldn't just copy it and claim it's yours, and you should try to improve it if you can.

---

(Did you remember to add your name and date at the top of your reflection file?)
