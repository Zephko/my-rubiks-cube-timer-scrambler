My CS50 Final Project is a cube scramble generator and timer web app. This is something that can be used when competing with other
speedcubers or when trying to improve your solve times on a specific scramble.

Run flask with 'application.py'

At the top of the page is rubik's cube scramble in cube notation.

R means turn the right face clockwise. R' means turn the right face counter-clockwise. R2 means turn the right face twice.
All other faces the same format:

L - Left face
U - Top face
F - Front face
D - Bottom face
B - Back face

(note: cube notation can be tricky, if you'd like to try maybe watch a video!)

Starting with the red face in front and the white face on bottom, if those moves are executed the cube should look exactly
like the unfolded cube diagram on the web app.

Once scrambled, use the timer to time your solve. Reset the timer and try again on the same scramble or refresh the page for
a new scramble. You can also change the length of the scramble if you like.

Scrambles are generated using my generate_scramble function and the scrambled cube layout is determined using my
execute_scramble function. A solved cube is passed as a dictionary where faces are labelled cube['right'], cube['top'], etc.
All faces are 3x3 matrices. Execute_scramble will call functions from moves.py to modify the matrices and return the scrambled faces.

The stopwatch timer is made using javascript. A bootstrap theme is used but the cube diagram is custom made using CSS Grids.