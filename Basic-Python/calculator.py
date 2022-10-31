"""Calculator"""
class calculator:
    """calculator substraction and addition"""

    def __init__(self, _i):
        self.i = _i

    def add(self, _i): return self.i + _i

    def subtract(self, _i):
        return self.i - _i
    
    #tested with pycodestyle, pylint, and flake8
