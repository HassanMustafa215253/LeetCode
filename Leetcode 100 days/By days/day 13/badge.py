class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        count=0
        for i,a in enumerate(students):
            print("students[i] = ",a)
            print("seats[i] = ",seats[i])
            if seats[i]<a:
                count+=a-seats[i]
                print("Smaller count = ",count)
            elif seats[i]>a:
                count+=seats[i]-a
                print("Bigger count = ",count)
        return count
s=Solution()
print(s.minMovesToSeat([4,1,5,9],[1,3,2,6]))