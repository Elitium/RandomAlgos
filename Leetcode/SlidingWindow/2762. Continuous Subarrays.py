class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        MaxQue = deque()  
        minQue = deque() 
        l, res = 0, 0  
        
        for r in range(len(nums)):
            while MaxQue and nums[MaxQue[-1]] <= nums[r]: #sorts maximum values in window desc, this filtering is needed as nums[r] is guaranteed to be in the window
                MaxQue.pop()
            MaxQue.append(r)
            
            while minQue and nums[r] <= nums[minQue[-1]]: #sorts minimum values in window asc, this filtering is needed as nums[r] is guaranteed to be in the window
                minQue.pop()
            minQue.append(r)
            
            while 2 < nums[MaxQue[0]] - nums[minQue[0]]:
                #if maximum and minimum in subarray have bigger than 2 difference, if left pointer is equal to one of the maximums or minimums, popleft from the respective queue, as it is no longer in window
                if MaxQue[0] == l:
                    MaxQue.popleft()
                if minQue[0] == l:
                    minQue.popleft()
                l += 1 #closing window
        
            res += (r - l + 1) #size of window plus 1 is number of subarrays
        
        return res
