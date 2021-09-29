Y_ELEMENT_INDEX = 1
X_ELEMENT_INDEX = 0

h = 25
l = 20
XL = [2,5,11,16,20,25]
YL = [5,17,4,6,1,20]
GP = [(2,5), (5,17), (11,4), (16,6), (20,1), (25,0)]
areas = []
 
def isInBetween (x, y, a):
    if x < a and a < y :
        return True
    return False
# a for loop to verify if a point is contained inside a rectangle, 
# and we use an if condition there to detect if there is any point inside a rectangle,
# by comparing the value of x and y position.
# if yes, we return True
# if no, we return False
# complexity of O(n)
def contains (left, right, points):
    for inner in points :
        if isInBetween(left[X_ELEMENT_INDEX], right[X_ELEMENT_INDEX] , inner[X_ELEMENT_INDEX]) and isInBetween(left[Y_ELEMENT_INDEX], right[Y_ELEMENT_INDEX] , inner[Y_ELEMENT_INDEX]) :
           return True
    return False

# calculating the surface of a rectangle
# complexity of O(1)
def surface(currentBase, right):
    return (right[X_ELEMENT_INDEX] - currentBase[X_ELEMENT_INDEX]) * right[Y_ELEMENT_INDEX]

# lamda function to subsitute x from each points given
# complexity of O(n)
def currentBasesFrom(points):
    return [(x,0) for x,_ in points]

# we subsitute x position of the currentBase by using the x position of all the points
# since we are calculating the surface base on x = 0
# we compare always the points on the right side of currentBase points
# however in this version we calulate the surface first and find the maxsurface then verify if this surface contains any points
# therefore in this version the complexity is O(N3)
def solveProblem (points, width, height):
    currentBase = (0,0)
    maxsurface = 0
    for currentBase in currentBasesFrom(points) :
        for x,_ in points :
            for _,y in points :
                right = (x,y)
                temp = surface(currentBase, right)
                if temp > maxsurface:
                    if not contains(currentBase, right, points) :
                        maxsurface =  temp
                     
                    
    return maxsurface

        
            
    
if __name__ == "__main__":
    # execute only if run as a script
    print(solveProblem(GP,l,h))
    
    