# turtle_mover
a game where two robot turtles battle for salad - my ROS2 practice.

it starts two turtlesim robots using ROS2 turtlesim launch files.
frontend, written in plain ole javascript connects to one using
websockets and displays it's pose. it also connects to an API,
FastAPI to be exact, for two reasons:
- you can spawn yummy salads for tutles to eat
- get the other turtle's pose

the backend for the other turtle was made with python

# setting up



you absolutely need to enter the following into terminal:
$xhost local:root

this enables the forwarding of turtle sim gui to your machine

$docker-compose -f docker-compose.yml up -d --build

Wait for the images to build and the app should start

# playing the game

http://localhost:3000 to open the web

after you open the web you move the turtle by using WASD. W and S are reversed cause... handicap?

the other turtle seems to teleport around. that's cause it's really fast (you can actually see it's movement in the turtle's gui window) and poor ole websocket and my frontend render logic just can't keep up.

spawn salads and make your turtle eat as much as it can. there's a counter below.

there's no victory, you cannot win or lose, only keep score. just like in life, we're all just turtles moving around, fighting for salad until our websockets simply disconnect. in the end, the score doesn't really matter, does it?

# ideas on how to improve

- need to implement better try-catch with logging in turtle_engine
- frontend's pretty crappy, it was written in vanilla js and code's pretty much unreadable (the purpose of this project was to practice ROS and python with less focus on js)
