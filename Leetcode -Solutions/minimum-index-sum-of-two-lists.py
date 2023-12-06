class Solution:
    def findRestaurant(self, list1, list2):
        index_dict = {}
        for i, string in enumerate(list1):
            index_dict[string] = i

        min_index_sum = float('inf')
        result = []

        for i, string in enumerate(list2):
            if string in index_dict:
                index_sum = i + index_dict[string]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [string]
                elif index_sum == min_index_sum:
                    result.append(string)

        return result