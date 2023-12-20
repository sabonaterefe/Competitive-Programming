class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                _sum, count = 0, 0

                for dx in range(max(0, i - 1), min(i + 2, m)):
                    for dy in range(max(0, j - 1), min(j + 2, n)):
                        _sum += img[dx][dy]
                        count += 1

                res[i][j] = _sum // count

        return res