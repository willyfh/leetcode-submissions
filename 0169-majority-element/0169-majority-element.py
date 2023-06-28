class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        m_val = nums[0]
        m_count = 1
        for i in range(1, len(nums)):
            if nums[i] == m_val:
                m_count+=1
            else:
                m_count-=1
                if m_count==0:
                    m_val = nums[i]
                elif m_count < 0:
                    m_val = nums[i]
                    m_count = 1
                    
        return m_val