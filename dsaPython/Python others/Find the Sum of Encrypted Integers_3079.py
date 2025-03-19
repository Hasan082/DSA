def sumOfEncryptedInt(nums):
        s = 0
        for num in nums:
            max_digit = max(str(num))
            s+=int(max_digit * len(str(num)))
        return s
