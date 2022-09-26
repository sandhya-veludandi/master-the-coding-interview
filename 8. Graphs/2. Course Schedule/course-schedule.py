class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj_list = []
        inDegree = {}
        seen = {}
        
        for i in range(numCourses):
            adj_list.append([])
            inDegree[i] = 0
           
        for p in prerequisites: 
            course = p[0]
            prereq = p[1]
            adj_list[prereq].append(course)
            inDegree[course] = inDegree[course] + 1
        
        while len(inDegree) > 0:
            # search for where inDegree[i] == 0
            count = len(inDegree)
            for node in inDegree: 
                if inDegree[node] == 0:
                    for child in adj_list[node]: 
                        inDegree[child] = inDegree[child] - 1
                    inDegree.pop(node)
                    break
                count = count - 1
            if count == 0: 
                return False
        return True