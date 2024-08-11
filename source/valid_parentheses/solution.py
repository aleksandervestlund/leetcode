class Solution:
    def isValid(self, s: str) -> bool:
        complement = {"{": "}", "(": ")", "[": "]"}
        queue: list[str] = []

        for char in s:
            end = complement.get(char)
            if end is None:
                if not (queue and char == queue.pop()):
                    return False
            else:
                queue.append(end)

        return not queue
