import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x > 0:
            return int(math.sqrt(x))
        return x