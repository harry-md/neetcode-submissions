class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        _min = 0
        for i in range(k):
            if blocks[i] == "W":
                _min += 1

        count = _min
        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                count -= 1

            if blocks[i] == "W":
                count += 1

            _min = min(_min, count)
        return _min