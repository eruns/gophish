class Asuit():

    def __init__(self, sts=None, st=None):
        # Args:
        # suits: list
        # suit: string
        self._suits = None
        self._suit = None

        if(self.validatesuits(sts)):
            self._suits = sts
        if(self.validatesuit(st)):
            self._suit = st

    @property
    def suits(self):
        return self._suits
    @suits.setter
    def suits(self, sts):
        if(self.validatesuits(sts)):
            self._suits = sts

    @property
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self, st):
        if(self.validatesuit(st)):
            self._suit = st

        return self._suits

    def validatesuits(self, sts):
        if (isinstance(sts, list)):
            if (4 == len(sts)):
                return True
            else:
                raise ValueError("Incorrect number of suits supplied!")
                return False
        else:
            raise TypeError("Incorrect type supplied for 'suits'!")
            return False
        return False

    def validatesuit(self, st):

        if(isinstance(st, str)):
            if( st in self._suits):
                return True
            else:
                return False
        # raise TypeError("Incorrect type supplied for variable'suit'!")
        return False


st = Asuit(["asdf", "qwer", "zxcv", "zxvczxvc"], 'asxxxdf' )
# print( st.validatesuit("zxcv"))
print(st.suits)
st.suit = "qwer"
print(st.suit)

