def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    left=0
    right=len(matrix)-1
    midglobal=-1

    while left<=right:
        mid = (right+left)//2
        if matrix[mid][0] <= target and matrix[mid][-1]>=target:
            midglobal=mid
            break
        elif matrix[mid][0]<=target:
            left=mid+1
        else:
            right=mid-1
    
    if midglobal==-1:
        return False
    
    left=0
    right=len(matrix[midglobal])-1

    while left<=right:
        mid2 = (right+left)//2
        if matrix[midglobal][mid2] == target:
            return True
        elif matrix[midglobal][mid2]<=target:
            left=mid2+1
        else:
            right=mid2-1
    else:
        return False

print(searchMatrix([[1,3]],3))