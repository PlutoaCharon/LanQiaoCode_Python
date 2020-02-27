class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法一
        '''
        def isPrime(n):
            if n == 2:
                return True
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        count = 0
        for i in range(2, n):
            if isPrime(i):
                count += 1
        return count
        '''
        # 方法二
        '''
        def is_prime(k):
            for i in range(len(prime)):
                if k > prime[i] and k % prime[i] == 0:
                    return False
            return True
        count = 2
        prime = [2, 3]
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 0
        elif n == 3:
            return 1
        else:
            for i in range(4, n):
                if is_prime(i):
                    prime.append(i)
                    count += 1
            return count
        '''
        # 方法三
        prime = []
        if n == 0 or n == 1 or n == 2:
            print(0)
        for i in range(n + 1):
            prime.append(True)
        for i in range(2, n + 1):
            if prime[i] == True:
                p = i
                j = 2
                while p * j <= n:
                    prime[p * j] = False
                    j += 1
        prime = prime[2:len(prime) - 1]
        ans = prime.count(True)
        return ans

