class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort(), depart.sort()
        i = j = k = 0

        while i < len(arrive):
            if j < len(depart) and depart[j] <= arrive[i]:
                k, j = k - 1, j + 1
            else:
                k, i = k + 1, i + 1

            if k > K:
                return False
        return True