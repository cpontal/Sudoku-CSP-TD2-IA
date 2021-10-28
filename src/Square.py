class Square:
    def __init__(self, value):
        self.value = value
        # if true the number is possible
        # example self.binCondition[1] = True
            # the number 2 is possible for this square
        if value == 0 :
            self.binCondition = [True,True,True,True,True,True,True,True,True]
        else:
            self.binCondition = [False,False,False,False,False,False,False,False,False]