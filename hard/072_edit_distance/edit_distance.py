class Solution:
    '''
    两个字符串比较，求最值，直接看似乎并不能直接找出解决方案，这时往往需要使用动态规划的思想寻找递推关系。使用双
    序列动态规划的通用做法，不妨定义f[i][j]为字符串1的前i个字符和字符串2的前j个字符的编辑距离，那么接下来寻找其递
    推关系。增删操作互为逆操作，即增或者删产生的步数都是一样的。故初始化时容易知道f[0][j] = j, f[i][0] = i, 接下
    来探讨f[i][j] 和f[i - 1][j - 1]的关系，和 LCS 问题类似，我们分两种情况讨论，即word1[i] == word2[j] 与否，

    第一种相等的情况有：

    1. i == j, 且有word1[i] == word2[j], 则由f[i - 1][j - 1] -> f[i][j] 不增加任何操作，有f[i][j] = f[i - 1][j - 1].
    2. i != j, 由于字符数不等，肯定需要增/删一个字符，但是增删 word1 还是 word2 是不知道的，故可取其中编辑距离的较小值，
    即f[i][j] = 1 + min{f[i - 1][j], f[i][j - 1]}.

    第二种不等的情况有：

    1. i == j, 有f[i][j] = 1 + f[i - 1][j - 1].
    2. i != j, 由于字符数不等，肯定需要增/删一个字符，但是增删 word1 还是 word2 是不知道的，故可取其中编辑距离的较小值，
    即f[i][j] = 1 + min{f[i - 1][j], f[i][j - 1]}.

    最后返回f[len(word1)][len(word2)]
    '''
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = 0, 0
        if word1:
            len1 = len(word1)
        if word2:
            len2 = len(word2)
        if not word1 or not word2:
            return max(len1, len2)
        
        # 编辑距离f
        f = [[i + j for i in range(1 + len2)] for j in range(1 + len1)]
        
        for i in range(1, 1 + len1):
            for j in range(1, 1 + len2):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i - 1][j - 1], 1 + f[i - 1][j], 1 + f[i][j - 1])
                else:
                    f[i][j] = 1 + min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1])
 
        # [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
        # print(f[len1][len2])

        # [[0, 1, 2, 3], [1, 1, 2, 3], [2, 2, 1, 2], [3, 2, 2, 2], [4, 3, 3, 2], [5, 4, 4, 3]]
        # print(f)

        return f[len1][len2]

if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("horse", "ros"))
