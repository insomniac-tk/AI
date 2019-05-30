""" Using the boilerplate code of problem and node, now I'll implement that for specific problem instances viz. Breadth-First-Search,
Depth-First-Search,A-Star, etc."""


import problem as p 
import node as n

class BreadthFirstSearchProblem(p.Problem):
    
    '''
        Here TM is the transition model. A dict that maps 
        states to the actions that can be performed in that
        state.
        E-g: 
        {'}
    '''
    def __init__(self, initial, goal,TM):
        super().__init__(self,initial,goal)

        self.TransitionModel = TM
    
    
    def actions(self,state):
        return self.TransitionModel[state]
        
    



if __name__=='__main__':
    BFS_Problem = BreadthFirstSearchProblem('A','G')
    #InitialNode = Node('A',['B','C','D'])
    print(BFS_Problem.initial,BFS_Problem.goal)
    BFS_Problem.value()