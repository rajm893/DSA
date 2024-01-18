class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_list = []
        arr_set = set(arr)
        for num in arr_set:
            freq = arr.count(num)
            if freq in count_list:
                return False
            count_list.append(freq)
        return True
