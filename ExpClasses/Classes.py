
class CountFromBy:
    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)

# h = CountFromBy(100, 10)
# print(h)
# h.increase()
# print(h)



class Return:
    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i

    def operation(self) -> tuple[int, float, int, int]:
        return self.val*self.incr, self.val/self.incr, self.val+self.incr, self.val-self.incr

    # def __repr__(self) -> str:
    #     return str(self.val)




r = Return(100, 10)
print(r)

a, b, c, d = r.operation()
print(a, b, c, d)



