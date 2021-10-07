
# define the hight and length by giving as tuple (h,l)
# add the tuple (h,l) in the given point list (GP) to define the limit of the region

L,H = (25,20)
GP = [ (2,5), (5,17), (11,4), (16,6), (20,1)]

# function for calculating the surface or rectangle
# Complexity O(1)
def surface(pivot, point):
   
    return abs((pivot[0] - point[0]) * point[1]) 

# function in serching for pivot.
# In our case the pivot is the one with lowest y-value in each divided section
# Complexity O(n)
def pickPivot(l) :
    pivot = min(l,key=lambda item:item[1])
    l.remove(pivot)
    return pivot

# Split the list to right list and left list by giving point of pivot
# complexity is O(n)
def splitList(l, pivot) :
    right = []
    left = []
    for point in l:
        if point[0] > pivot[0]:
            right.append(point)
        else:
            left.append(point)
    return left, right

# function to find the lowest y-value (height) in each divied section.
# if there is no point within the section then the maximum height concider as h, which is 20 in our example.
# solveBranch function and solveProblem function inter-calls each other, forming a second degree of recursivity
# apply master theoreme to calculate the complexity T(n) = 2*T(n/2)+O(n)
# d = logb a = 1, T(n) = O(n logn)
def solveBranch (branch, pivot, h, lastPivot) :
    maxHeight = h
    surf = 0
    if len(branch) > 1 :
        surf = solveProblem(branch, h, pivot)
    else :
        if len(branch) == 1 :
             maxHeight = branch[0][1]
        surf = surface(pivot, (lastPivot[0], maxHeight))
    
    return surf


def solveProblem(points, h, lastPivot) :
    
    pivot = pickPivot(points)
    
    left, right = splitList(points, pivot )
    
    rightMaxSurface = solveBranch(right, pivot, h, lastPivot)
    leftMaxSurface = solveBranch(left, pivot, h, lastPivot)
        
    return max(rightMaxSurface, leftMaxSurface)
   


if __name__=="__main__":
    
    print(solveProblem(GP, H, (L,H)))
    
    
    
    
    
    
