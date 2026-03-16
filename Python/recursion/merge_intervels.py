class MergeIntervels :

    def solution(self, arr) :

        merged = []

        arr.sort()

        for intervels in arr :

            if not merged :

                merged.append(intervels)

            elif intervels[0] <= merged[-1][1]   :

                merged[-1][1] = intervels[1]

            else :

                merged.append(intervels)

        return merged


merge_instance = MergeIntervels()

print(merge_instance.solution([[13,15],[1,5],[7,11]]))
