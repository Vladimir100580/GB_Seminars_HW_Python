

class Lop:
    def __init__(self, head=None):
        self.head = 3
    def recurs(self, data):
        print(f'{self.head=}, {data=}')
        self.head = 2 * data
    def print_lst(self):
        pass


l = Lop()

l.recurs(5)
l.recurs(7)
l.recurs(9)
# lst.add_node('3')
# lst.add_node('4')

