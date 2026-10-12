import math

class Error:


    #  Chapter 1 - Types of errors

    @staticmethod
    def error(actual, approx):
        return actual - approx
    
    @staticmethod
    def abs_error(actual, approx):
        return abs(Error.error(actual, approx))
    
    @staticmethod
    def relative_error(actual, approx):
        return Error.abs_error(actual, approx) / abs(actual)

    @staticmethod
    def percentage_error(actual, approx):
        return Error.relative_error(actual, approx) * 100


class Gaussian:

        @staticmethod
        def guassian_elimination(matrix):
            pass

        @staticmethod 
        def partial_pivot():
            pass

        @staticmethod
        def scaled_pivot():
            pass

        @staticmethod
        def complete_pivot():
            pass


class Differentiation:

   

    @staticmethod
    def solve_diff(x:tuple, y:tuple, a:int|float):
        pass

    @staticmethod
    def first_diff_forward(x:tuple, y:tuple, a:int|float):
        try:

            index = x.index(a)
            h = x[index+1] - a
            results = (y[index+1] - y[index]) / h
            return results
        
        except IndexError as e:
            return f"Error: {e}, please use a different method."
        except TypeError as e:
            return f"Error: {e}."
        except ValueError as e:
            return f"Error: {e}."



    @staticmethod
    def first_diff_backward(x:tuple, y:tuple, a:int|float):
        try:
        
            index = x.index(a)
            h = - 1 * (x[index - 1] - a)
            results = (y[index] - y[index - 1]) / h
            return results
                
        except IndexError as e:
            return f"Error: {e}, please use a different method."
        except TypeError as e:
            return f"Error: {e}."
        except ValueError as e:
            return f"Error: {e}."
        

    @staticmethod
    def central_diff(x:tuple, y:tuple, a:int|float):
        try:
                
            index = x.index(a)
            if index - 1 < 0:
                raise IndexError
            h = x[index + 1]  - x[index - 1]
            results = (y[index + 1] - y[index - 1]) / h
            return results
                        
        except IndexError as e:
            return f"Error: {e}, please use a different method."
        except TypeError as e:
            return f"Error: {e}."
        except ValueError as e:
            return f"Error: {e}."


            

    

