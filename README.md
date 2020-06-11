# SevenSegmentMath
Some combinatorics on seven segment displays

Some inititial sources of info:
https://en.wikipedia.org/wiki/Seven-segment_display_character_representations

https://www.tutorialspoint.com/seven-segment-displays

https://puzzling.stackexchange.com/questions/38264/how-many-digits-can-you-create-with-only-one-seven-segment-display

A repo that will save me a lot of figuring out the python part:

https://github.com/martandsingh/alogorithm

# Initial questions

- Q. How many characters (valid or not) are possible on a seven digit display?
- A. 128.

- Q. How many valid numbers available on a seven segment display?  
- A. For now, I will only use one type of each number to make further questions more easily answered, so the answer is 10.

- Q. For any given digit, how many valid digits can be obtained by removing or adding a single segment?
- A. 

# Equations

I will look at three digit equations, with an operator (a separate plus or minus display)

Using 3 digits and an operator of the form X * Y = Z:
    Q. How many equations (valid or invalid) can we display?
    Q. Combinatorially this is 10 * 2 * 10 * 10 = 2000

    Q. How many of these equations are valid?
    A. To be answered

For a three digit equation with an operator (plus or minus):
    - Q. Given an invalid equation (with valid digits), how many valid equations can be obtained by moving a segment between numbers or operators? (a popular "brain training" exercise)
    - Q. Given a valid equation, how many valid equations can be obtained by moving a segment between numbers or operators?
    - Q. How many invalid equations (but with valid numbers) can we create?





