class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        max_time = 0
        adj_list = []
        seen = {}
        for i in range(n): 
            adj_list.append([])
            seen[i] = False
            
        seen[headID] = True
        for emp_id in range(n): 
            if emp_id != headID: 
                adj_list[manager[emp_id]].append(emp_id)
        
        for neighbor in adj_list[headID]: 
            new_time = self.dfs(neighbor, adj_list, informTime, informTime[headID], seen)
            max_time = max(max_time, new_time)
        
        return max_time
            
    def dfs(self, vertex, adj_list, informTime, new_time, seen):
        if informTime[vertex] == 0: 
            return new_time
        seen[vertex] = True
        new_time += informTime[vertex]
        time = 0
        for neighbor in adj_list[vertex]: 
            if not seen[neighbor]:
                time = max(time, self.dfs(neighbor, adj_list, informTime, new_time, seen)) 
        return time