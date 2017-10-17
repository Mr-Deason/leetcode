class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """

        #TLE
        ans = -1
        n = len(flowers)
        import numpy as np
        bloom = np.array([flowers[0]])
        for day in range(2, n+1):
            pos = flowers[day-1]
            find = np.searchsorted(bloom, pos)
            if find > 0 and bloom[find-1] == pos-k-1:
                return day
            if find < day-1 and bloom[find] == pos+k+1:
                return day
            bloom = np.insert(bloom, find, pos)
        return ans


def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return []
    return [int(number) for number in input.split(",")]


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            flowers = stringToIntegerList(line)
            line = lines.next()
            k = int(line)

            ret = Solution().kEmptySlots(flowers, k)

            out = str(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()