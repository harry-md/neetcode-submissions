class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        elif k > 0:
            cur_sum = sum(code[1 : k + 1])
            res[0] = cur_sum

            for i in range(1, n):
                cur_sum -= code[i]
                if i + k >= n:
                    cur_sum += code[i + k - n]
                else:
                    cur_sum += code[i + k]
                res[i] = cur_sum
        else:
            cur_sum = sum(code[-1 - 1 : -1 + k - 1 : -1])
            res[-1] = cur_sum
            for i in range(-2, -n - 1, -1):
                cur_sum -= code[i]
                if -i - k - 1 < n:
                    cur_sum += code[i + k]
                else:
                    cur_sum += code[i + k + n]
                res[i] = cur_sum
        return res