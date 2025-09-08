import networkx as nx

class CausalGraph:
    
    def __init__(self,
                 mode,
                 data_path=None, 
                 ):

                 assert mode in ['custom', 'notears']
                 self.mode = mode
                 self.data_path = data_path
    
    def causal_graph(self):
        if self.mode == 'custom':

            causal_graph = nx.DiGraph([('X0', 'Y'), ('X1', 'Y'), ('X2', 'Y'), ('X3', 'Y'), ('X4', 'Y'), ('X5', 'Y'), ('X6', 'Y'), ('X7', 'Y'), ('X8', 'Y'), ('X9', 'Y'), ('X10', 'Y'), ('X11', 'Y'), ('X12', 'Y'), 
                                    ('X13', 'Y'), ('X14', 'Y'), 
                                    ('X6', 'X2'), ('X9', 'X2'), ('X11', 'X2'), ('X4', 'X0'), ('X7', 'X0'), ('X10', 'X0'), ('X11', 'X0'), 
                                    ('X4', 'X1'), ('X5', 'X1'), ('X7', 'X1'), ('X8', 'X1'), ('X10', 'X1'), ('X11', 'X1'), 
                                    ('X4', 'X14'), ('X5', 'X14'), ('X6', 'X14'), ('X7', 'X14'), ('X8', 'X14'), ('X9', 'X14'), ('X10', 'X14'), 
                                    ('X2', 'X3'), ('X0', 'X3'), ('X1', 'X3'), ('X13', 'X12'), ('X14', 'X12')])
        
        elif self.mode == 'notears':
            """
            we would supprt the notears to extract the causal graph ASAP
            """
            pass

        else:
            raise ValueError("Unknown model {} !!!".format(self.mode))    
        
        return causal_graph



