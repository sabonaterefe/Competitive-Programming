class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        typed_ptr = 0
        name_ptr = 0

        while typed_ptr < len(typed):
            if name_ptr < len(name) and typed[typed_ptr] == name[name_ptr]:
                typed_ptr += 1
                name_ptr += 1
            elif typed_ptr > 0 and typed[typed_ptr] == typed[typed_ptr - 1]:
                typed_ptr += 1
            else:
                return False

        return name_ptr == len(name)