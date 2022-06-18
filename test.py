# # # # Remember, all submissions are being checked for plagiarism.
# # # # Your recruiter will be informed in case suspicious activity is detected.
# # #
# # # # you can write to stdout for debugging purposes, e.g.
# # # # print("this is a debug message")
# # # def getSumOfDigit(n):
# # #     sum = 0
# # #     for digit in str(n):
# # #         sum += int(digit)
# # #     return sum
# # #
# # #
# # # def solution(A):
# # #     # write your code in Python 3.6
# # #     n = len(A)
# # #     mp = {}
# # #     ans = -1
# # #     pairi = 0
# # #     pairj = 0
# # #     for i in range(n):
# # #         temp = getSumOfDigit(A[i])
# # #         if (temp not in mp):
# # #             mp[temp] = 0
# # #
# # #         if (mp[temp] != 0):
# # #             if (A[i] + mp[temp] > ans):
# # #                 pairi = A[i]
# # #                 pairj = mp.get(temp)
# # #
# # #         mp[temp] = max(A[i], mp[temp])
# # #     digitsum = pairi + pairj
# # #     if digitsum == 0:
# # #         return -1
# # #     else:
# # #         return digitsum
# # #
# # #
# # #
# # # #[51, 71, 17, 42]
# #
# # from collections import Counter
# # l = [1,2,2,3,3,3,5,8]
# #
# # x = Counter(l)
# # print(x)
# # max_key = max(x, key=x.get)
# #
# # v = []
# # print(max_key)
# # for i in x:
# #     if i == x[i]:
# #        v.append(i)
# # print(max(v))
# #
# # # you can write to stdout for debugging purposes, e.g.
# # # print("this is a debug message")
# # from collections import Counter
# #
# #
# # def solution(A):
# #     # write your code in Python 3.6
# #     get_counter = Counter(A)
# #     count_list = []
# #     for i in get_counter:
# #         if i == get_counter[i]:
# #             count_list.append(i)
# #     if count_list:
# #         return max(count_list)
# #     else:
# #         return 0
# #
#
#https://www.geeksforgeeks.org/minimum-removals-required-such-that-a-string-can-be-rearranged-to-form-a-palindrome/
# # Python3 implementation to find
# # minimum number of deletions
# # to make a string palindromic
#
# # Returns the length of
# # the longest palindromic
# # subsequence in 'str'
# def make_palindrom(str):
#     n = len(str)
#     L = [[0 for x in range(n)] for y in range(n)]
#     for i in range(n):
#         L[i][i] = 1
#     for cl in range(2, n + 1):
#         for i in range(n - cl + 1):
#             j = i + cl - 1
#             if (str[i] == str[j] and cl == 2):
#                 L[i][j] = 2
#             elif (str[i] == str[j]):
#                 L[i][j] = L[i + 1][j - 1] + 2
#             else:
#                 L[i][j] = max(L[i][j - 1], L[i + 1][j])
#     return L[0][n - 1]
#
#
# def DeletionsCount(str):
#     n = len(str)
#     l = make_palindrom(str)
#     return (n - l)
#
#
# # Driver Code
# if __name__ == "__main__":
#     str = "aaabab"
#     print("Minimum number of deletions = "
#           , DeletionsCount(str))


# Python3 program for
# the above approach

# Function to find the number of deletions
# required such that characters of the
# string can be rearranged to form a palindrome
def minDeletions(str):
    fre = [0] * 26
    n = len(str)
    for i in range(n):
        fre[ord(str[i]) - ord('a')] += 1
    count = 0
    for i in range(26):
        if (fre[i] % 2):
            count += 1
    if (count == 0 or count == 1):
        return 0

    else:
        return count - 1


# Driver Code
if __name__ == '__main__':
    str = "ervervige"

    # Function call to find minimum
    # number of deletions required
    print(minDeletions(str))

# This code is contributed by mohit kumar 29.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    chr_fre = [0] * 26
    n = len(S)
    for i in range(n):
        chr_fre[ord(S[i]) - ord('a')] += 1
    count = 0
    for i in range(26):
        if (chr_fre[i] % 2):
            count += 1
    if (count == 0 or count == 1):
        return 0
    else:
        return count - 1


