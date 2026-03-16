class ClosestNumToZero :

    def solution(self,arr) :

        closest_number = arr[0]

        for num in arr :

            if abs(num) < abs(closest_number) :

                closest_number = num

        if closest_number < 0 and abs(closest_number) in arr :

            return abs(closest_number)
            
        return closest_number
    
clst_instance = ClosestNumToZero()

print(clst_instance.solution([-2,-3,-1,1,2,3,4]))