from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for elem1, elem2 in zip_longest(
            (int(elem) for elem in version1.split(".")),
            (int(elem) for elem in version2.split(".")),
            fillvalue=0
        ):
            if elem1 < elem2:
                return -1
            if elem1 > elem2:
                return 1
        return 0
