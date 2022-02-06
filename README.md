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

# open the web

http://localhost:3000 to open the web

# ideas on how to improve

- need to implement better try-catch with logging in turtle_engine
- frontend's pretty crappy, it was written in vanilla js and code's pretty much unreadable (the purpose of this project was to practice ROS and python with less focus on js)
