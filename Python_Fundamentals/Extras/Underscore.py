class Underscore:
    def map(self, iterable, callback):

        # for i in range(len(iterable)):
        #     iterable[i] = (callback(iterable[i]))
        # return(iterable)

        return(list(map(callback, iterable)))

    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if(callback(iterable[i]) == True):
                return iterable[i]
    def filter(self, iterable, callback):
        newarray = []
        for i in range(len(iterable)):
            if(callback(iterable[i]) == True):
                newarray.append(iterable[i])
        return newarray
    def reject(self, iterable, callback):
        newarray = []
        for i in range(len(iterable)):
            if(callback(iterable[i]) == False):
                newarray.append(iterable[i])
        return newarray


_ = Underscore()
double = _.map([1,2,3], lambda x: x*2)
greater = _.find([1,2,3,4,5,6], lambda x: x>4)
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
odds = _.reject([1,2,3,4,5,6], lambda x: x % 2 == 0)
print(double, greater, evens, odds)