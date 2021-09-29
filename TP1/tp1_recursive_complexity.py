# define the hight and length by giving as tuple (h,l)
# add the tuple (h,l) in the given point list (GP) to define the limit of the region
# X and Y element index is for clairity, we can also use directly 0 and 1 in the code

L,H = (25,20)
GP = [ (2,5), (5,17), (11,4), (16,6), (20,1)]

def surface(pivot, point):
    print (pivot, point)
    return abs((pivot[0] - point[0]) * point[1]) 


def pickPivot(l) :
    pivot = min(l,key=lambda item:item[1])
    l.remove(pivot)
    return pivot

def splitList(l, pivot) :
    right = []
    left = []
    for point in l:
        if point[0] > pivot[0]:
            right.append(point)
        else:
            left.append(point)
    return left, right

def solveBranch (branch, pivot, h, lastPivot) :
    maxHeight = h
    surf = 0
    if len(branch) > 1 :
        surf = solveProblem(branch, h, pivot)
    else :
        if len(branch) == 1 :
             maxHeight = branch[0][1]
        surf = surface(pivot, (lastPivot[0], maxHeight))
    print (surf, branch)
    return surf


def solveProblem(points, h, lastPivot):
    
    pivot = pickPivot(points)
    left, right = splitList( points, pivot )
    
    rightMaxSurface = solveBranch(right, pivot, h, lastPivot)
    leftMaxSurface = solveBranch(left, pivot, h, lastPivot)
        
    return max(rightMaxSurface, leftMaxSurface)
   


if __name__=="__main__":
    
    print(solveProblem(GP, H, (L,H)))
    
    
    
    
    
    
