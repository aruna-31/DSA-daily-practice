class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def helpRe(ind,target,arr):
            if target == 0:
                return res.append(list(arr))
            
            if target <0:
                return
            for i in range(ind,n):
                if i>ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] >target:
                    break
                arr.append(candidates[i])
                helpRe(i+1,target-candidates[i],arr)
                arr.pop()
        helpRe(0,target,[])
        return res