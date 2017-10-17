class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = {}
        mmm = 10000000
        now = int(time[0:2])*60 + int(time[3:5])
        for ch in time:
            if ch != ':':
                digits[ch] = 1;
        digits = list(digits.keys())
        ans = ''
        for h1 in digits:
            for h2 in digits:
                for m1 in digits:
                    for m2 in digits:
                        h = int(h1+h2)
                        m = int(m1+m2)
                        if h < 24 and m < 60:
                            miniutes = h*60+m
                            if miniutes > now and miniutes - now < mmm:
                                ans = h1+h2+':'+m1+m2
                                mmm = miniutes - now
                            if miniutes+24*60-now < mmm:
                                ans = h1 + h2 + ':' + m1 + m2
                                mmm = miniutes+24*60-now
        return ans






def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            time = stringToString(line)

            ret = Solution().nextClosestTime(time)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()