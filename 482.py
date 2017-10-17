class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = list(S)
        s.reverse()
        ans = ''
        cnt = 0
        for ch in s:
            if ch != '-':
                if cnt > 0 and cnt % K==0:
                    ans += '-'
                ans += ch.upper()
                cnt += 1
        return ans[::-1]



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
            S = stringToString(line)
            line = lines.next()
            K = int(line)

            ret = Solution().licenseKeyFormatting(S, K)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()