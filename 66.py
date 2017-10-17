class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        digits[0] += 1
        for i in range(len(digits)):
            if digits[i] >= 10 and i == len(digits)-1:
                digits += [1];
            elif i < len(digits)-1:
                digits[i+1] += digits[i] / 10
            digits[i] %= 10
        digits = digits[::-1]
        return digits



def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return []
    return [int(number) for number in input.split(",")]


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    if not len_of_list:
        return "[]"

    result = ""
    for index in range(len_of_list):
        num = nums[index]
        result += str(num) + ", "
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            digits = stringToIntegerList(line)

            ret = Solution().plusOne(digits)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()