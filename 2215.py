from itertools import accumulate
def largestAltitude(gain: list[int]) -> int:
    for i in range(1, len(gain)):
        gain[i] += gain[i - 1]
    return max(0,*gain)

print(largestAltitude([-5,1,5,0,-7]))