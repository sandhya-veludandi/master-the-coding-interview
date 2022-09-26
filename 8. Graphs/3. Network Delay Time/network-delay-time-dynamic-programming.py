import sys
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        distance = {}
        k = k - 1
     
        for i in range(n):
            distance[i] = sys.maxint
        
        vertex = k
        distance[k] = 0
        
        for i in range(n):
            count = 0
            for time in times:
                src = time[0] - 1
                dest = time[1] - 1
                wt = time[2]
                
                if distance[src] == sys.maxint: 
                    continue
                else: 
                    if distance[src] + wt < distance[dest]:
                        distance[dest] = distance[src] + wt
                        count += 1
            if count == 0:
                break
                
        if sys.maxint in distance.values():
            return -1
        
        return max(distance.values())