'''Destination City
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
'''

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        fro = []
        to = []
        
        for path in paths:
            fro.append(path[0])
            to.append(path[1])

        for path in to:
            if path not in fro:
                return path
        
        return None