class SemanticAction:
    """
    Example of usage:

    def soma(a,b):
        return a+b 
    action = SemanticAction(soma, 5, 7)
    result = action.function(*action.parameters)
    print(result)
    """


    def __init__(self, function, *parameters):
        self.function = function
        self.parameters = parameters
