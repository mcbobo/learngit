class Stack(object):
    def __init__(self, s=list()):
        self.s = s

    def isempty(self):
        return 1 if len(self.s) == 0 else 0

    def push(self, d):
        print('push:', d)
        self.s.append(d)

    def peek(self, index=-1):
        if self.isempty():
            print('empty list')
        else:
            return self.s[index]

    def pop(self, index=-1):
        if self.isempty():
            print('empty list')
        elif 'pop' in dir(self.s):
            print('pop:', self.s.pop(index))
        else:
            print('no pop,peek:', self.peek(index))
            del self.s[index]

    def viewstack(self):
        print(self.s)


if __name__ == '__main__':
    s = Stack()
    print(s.isempty())
    s.push(3)
    s.viewstack()
    s.peek()
    s.viewstack()
    s.pop()
    s.viewstack()
