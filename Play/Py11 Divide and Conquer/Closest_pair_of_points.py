"""
(Update 11/dec: The exercise was updated and simplified. Sorry for the disturbance.)

The Euclidean distance between two points and is given by the formula

.

Given a list of points, for example P=[(5, 0), (2, 3), (6, 2), (1, 0)], in order to find the two closest points, we would need to compute that distance of every pair of points. That would be O(n²).

There is a faster algorithm which is O(n log(n)), as described here (planar case). Write a function closest_pair(points) that implements that algorithm and returns the minimum distance rounded to the units place.

    First of all: Pre-process step: order the points by the X-coordinate

    Now, call another function that:

    Splits the points into a left (L) and a right (R) list of same size.

Call your function recursively to compute the minimum distance of that left (dL) and right list (dR). Now, dLR = min(dL, dR). Do not forget to add the base case to the function.

In addition, we must also compare the points from the left list to the right list because there are points (like these two green points below) which are very close together. This step is slower than the previous one because computing the Euclidean distance between all points from the left list to all points of the right list is slow. We can improve that a little bit by first computing the X-distance between those points and filtering those points whose X-distance is smaller than dLR. (Computing the X-distance is much faster than the Euclidean-distance because the X-distance uses abs instead of sqrt.) The result of this will be dM.

Return the minimum between dLR and dM.

"""

def closest_pair(points):
    points = sorted(points, key = lambda x: x[0])
    if len(points) <= 4:
        min_dist = 99999999
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                if ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5 < min_dist:
                    min_dist = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
        return int(round(min_dist,0))

    else:
        left = points[:len(points)//2]
        right = points[len(points)//2:]

        return min(closest_pair(left), closest_pair(right), closest_pair([left[-1], right[0]]))
