class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
        for i in range(2, A):
            if self.is_prime(i) and self.is_prime(A - i):
                return i, A - i
                
    def is_prime(self, n):
        if n < 2:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True