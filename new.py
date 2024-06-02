"""Ok so lemme just say I didn't understand what the question 
was asking because it was late at night. but it was quite easy to understand 
later. 

So... we're supposed to do math right? just find the shortest path from one 
point to another. Seems easy enough I could do that in just 2 seconds in a math exam."""

#here's the necessary equation for it if you're curious
#distance = √(∆y²+∆x²). 
#∆ symbol shows the substraction between the y values and the x values in themselves 

# ok lets just do this clculations for 2 points.
point1 = (2, 3)
point2 = (5, 6)

# Define the Euclidean distance function
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

# Calculate the distance between the two points
distance = euclideanDistance(point1, point2)

# Print the result
print("The Euclidean distance between point1 and point2 is:", distance)

#that's basically all there is to it in two points.

"""now to get to the more complicated part...
my task currently is to make a list of different points, calculate the
distances between each adjacent pairs of points and put them in a list.. nice

And then picking the shortest path between all the combinations of the points
huh.. it makes me think where this can be integrated in the graph theory for example
So lets start by defining a random list of points"""

points = [(2, 3), (5, 6), (1, 1), (8, 9), (4, 7)]
distances_in_itr = []
for i in range(len(points)):
#using another iterator(j) and making it start ftom i+1 and end at the length of the 
#list prevents the algorithm from calculating the same pairs twice. 
#example calculated points: (1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4)... 
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances_in_itr.append(distance)
#defining what exactly is min distance 
min_distance = min(distances_in_itr)
#printing the min distance
print("Minimum mesafe:", min_distance)

#now this program isn't very.. flexible. it doesn't take any imputs and it doesnt calculate
#anything other than the first list we gave it. every single time we want to calculate a 
#new group of points we have to go in there and rewrite the list of points. 
"""There's probably a better and more optimized way of doing this but honestly? 
I'm leazy to research and this is good enough for now"