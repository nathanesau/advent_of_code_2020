#def dfs_subbranches(graph, src):  # traverse entire graph
#    """
#    modified dfs from part 1
#    """
#    branches = []
#    parent = {}
#    # do not store visited
#    s = [src]
#    while s:
#        it = s.pop()
#        neighbors = graph[it]
#        if neighbors:
#            for neighbor in graph[it]:
#                # weight not used
#                nvalue = neighbor["value"]
#                if nvalue:
#                    s.append(nvalue)
#                    parent[nvalue] = it
#        else:  # this is an endpoint -> construct branch using parent
#            tmp = it
#            path = [tmp]
#            while tmp != src:
#                tmp = parent[tmp]
#                path.insert(0, tmp)
#            branches.append(tuple(path))
#    
#    # get subbranches from branches
#    subbranches = set()
#    for branch in branches:
#        cpath = [branch[0]]  # walk along branch
#        for node in branch[1:]:
#            cpath.append(node)
#            if tuple(cpath) not in subbranches:
#                subbranches.add(tuple(cpath))
#    return subbranches