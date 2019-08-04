# Ariel Delgado
# Puzzle Assingment for Mob Pro

# Open and read text file containing numbers
with open('input/large.txt', 'r') as f:
    for line in f:
        numbers = [int(num) for num in line.split()]

# Part 1
metadata = []
def get_license(data):
    if data:
        n_child_nodes = data.pop(0)
        meta_entries = data.pop(0)
        find_children(data, n_child_nodes)
    return find_meta(data, meta_entries)

def find_meta(data, meta_entries):
    for i in range(meta_entries):
        if data:
            metadata.append(data.pop(0))   
    return metadata

def find_children(data, n_child_nodes):
    for i in range(n_child_nodes):
       get_license(data)
    
# Part 2
class navigation_system:
    def __init__(self, lon):
        if lon:
            self.number_children = lon.pop(0)
            self.number_meta = lon.pop(0)
            self.children = [navigation_system(lon) for _ in range(self.number_children)]
            self.metadata = [lon.pop(0) for _ in range(self.number_meta)]

    def get_child_node(self, child_node):
        if child_node < len(self.children):
            return self.children[child_node].get_root_value()
        return 0

    def get_root_value(self):
        if not self.children:
            return sum(self.metadata)
        root_total = [self.get_child_node(i - 1) for i in self.metadata]
        return sum(root_total)


# Tests
"""
List in Python are mutable. 
If you are using the same list variable for more than one test make
sure to wrap it in list(). Fore example, list(list_of_test1). 
 """ 

small_test_list = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
small_test_list2 = [2, 2, 0, 3, 1, 1, 2, 1, 0, 1, 12, 0, 1, 11, 20, 21, 50, 52]

# Test Part 1
print(sum(get_license(list(numbers))))

# Test Part 2
test = navigation_system(list(numbers))
print(test.get_root_value())

