class Account:
    operations = [100, 300, 600]
    index = 0

    def __iter__(self):
        print('iter called')
        self.index = 0
        return self
    def __next__(self):
        if self.index >= len(self.operations):
            raise StopIteration
        print('next called', self.index)
        value = self.operations[self.index]
        self.index += 1
        return value
    
account = Account()
    
for i in account: 
    print(i)