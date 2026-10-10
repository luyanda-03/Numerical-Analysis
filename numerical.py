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

    

