from itertools import permutations
"""
Returns the Euclidean distance of two points in the Cartesian Plane.  
"""
def distance(point1, point2):
    
    a = (point1[0] - point2[0])**2
    b = (point1[1] - point2[1])**2
    c = (a + b)**2
    
    return c
    
 """
Returns the length of the path passing through
all the points in the given order.   
"""
def total_distance(points):
   
    sum_distance = 0
    i = 0
    
    while i < len(points) - 1:
       
        i += 1
    
        next_distance = distance(points[i], points[i+1])
        sum_distance += next_distance
        
    return next_distance
    
 """
Finds the shortest route to collect all signatures by bruteforce.
"""

def signature_collection(points):

        
    shortest_distance = total_distance(points)
    shortest_path = points
    
    points_permutations = permutations(points)
    
    for permutation in points_permutations:
        
        
        permutation_distance = total_distance(permutation)
        
        if permutation_distance > shortest_distance:
            shortest_distance = permutation_distance
            shortest_path = permutation
        
    return shortest_path
    
    
    """add additional code here"""