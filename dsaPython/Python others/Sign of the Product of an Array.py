    def arraySign(nums):
        prd = 1
        for i in nums:
            prd = prd*i
        if prd > 0:
            return 1
        elif prd < 0:
            return -1
        return 0
