class Item():
    def __init__(self,weight,value):
        self.value=value
        self.weight=weight
# test data:
items_list=[Item(2,3),Item(3,4),Item(1,5),Item(5,6)]
# items_list=[Item(2,3),Item(3,4),Item(1,5),Item(6,26)]

def knapsack01(n, w,items_list):
    """[summary]

    Args:
        n (int): the number of the items to be choose （originally)
        w (int): the max weight the knapsack could maintain
        items_list (list): list of items

    Returns:
        list: two dimesion list (the last element is the max value of the knapsack)
    """    
    k = [[0 for j in range(w+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,w+1):
            item=items_list[i-1]
            if j<item.weight:
                k[i][j]=k[i-1][j]
            else:
                k[i][j]=max(k[i-1][j],k[i-1][j-item.weight]+item.value)
    return k
                
k=knapsack01(4,6,items_list)
for line in k:
    print(line)
print("the max value:",k[-1][-1])
def test_copilot():
    print("test copilot")
if "__main__"==__name__:
    test_copilot()
    print("test copilot")
# todo a snapshot functon
def copilot():
    print("copilot")
def add(a:int,b:int):
    return a + b
def parce_expenses():
    

"""Parse the list of expenses and return the list of triples (date, value, currency).
    Ignore lines starting with #.
    Parse the date using datetime.
    Example expenses_string:
        2016-01-02 -34.01 USD
        2016-01-03 2.59 DKK
        2016-01-03 -2.72 EUR
    """    