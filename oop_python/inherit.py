class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        # self.__greet(iterable)
        self.__greet()
        self.__update(iterable)
    def greet(self):
        print("parent greet")
    __greet=greet
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):
    def __init__(self, iterable):
        super().__init__(iterable)
        
        
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
            
            
if __name__=="__main__":
    print("😎")
    