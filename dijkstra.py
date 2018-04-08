
graph = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}
def dijkstra(graph,start,end,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in start
    """    
    # a few sanity checks
    if start not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if end not in graph:
        raise TypeError('The target of the shortest path cannot be found')    
    # ending condition
    if start == end:
        # We build the shortest path and display it
        path=[]
        pred=end
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[end])) 
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[start]=0
        # visit the neighbors
        for neighbor in graph[start] :
            if neighbor not in visited:
                new_distance = distances[start] + graph[start][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = start
        # mark as visited
        visited.append(start)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with start='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,end,visited,distances,predecessors)
    
    

