"""Ok so lemme just say I didn't understand what the question 
was asking because it was late at night. but it was quite easy to understand 
later. 

So... we're supposed to do math right? just find the shortest path from one 
point to another. Seems easy enough I could do that in just 2 seconds in a math exam."""

#here's the necessary equation for it if you're curious
#distance = √(∆y²+∆x²). 
#∆ symbol shows the substraction between the y values and the x values in themselves 

points = [(2, 3), (5, 6), (1, 1), (8, 9), (4, 7)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


min_distance = min(distances)
print("Minimum mesafe:", min_distance)
