class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        h_idx = 0
        citations = sorted(citations, reverse=True)
        for idx, cite in enumerate(citations):
            if idx >= cite:
                return idx
        return len(citations)