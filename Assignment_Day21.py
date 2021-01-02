from collections import Counter

class MyCallable:
    def __call__(self,val):
        self.value = val
        co2 = Counter(self.value)
        return ('MyCallable'+'('+str(dict(co2))+')')


co1 = MyCallable()
print(co1('intel'))
