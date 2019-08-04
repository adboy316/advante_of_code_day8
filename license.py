# Ariel Delgado
# Puzzle Assingment for Mob Pro


# Open and read text file containing numbers
with open('input/large.txt', 'r') as f:
    for line in f:
        numbers = [int(num) for num in line.split()]

# Part 1
"""
For the first part I decided to use a set of recursive methods.
When I saw the second part of the problem I realized that this was not 
the best approach. But I left it here anyways because I still 
think it is a decent solution.
"""

def get_license(data, metadata = None):
    """
    This method checks to see if data is not empty, and then pops the 
    first and second values from the list, which are the number of child
    nodes and meta entries. It then passes those values to the find_children
    and find_meta mehotds respectively. 

    Popping from the left works nicely because it is guranteed that if 
    a node has any children, it's first child will be directly next to it
    in the array. And the child's first child will also be next to it. If
    there are no children, then that must be metadata. This logic works 
    recursively if you pop from the left every time. 
    """
    if metadata is None:
        metadata = []

    if data:
        n_child_nodes = data.pop(0)
        meta_entries = data.pop(0)
        find_children(data, n_child_nodes, metadata)
    return find_meta(data, meta_entries, metadata)
  

def find_children(data, n_child_nodes, metadata):
    """
    This method acts as a recursive helper for get_license, calling it
    for each of the node's children. If there are no children it does 
    not get called and the find_meta method gets called.
    """
    for i in range(n_child_nodes):
       get_license(data, metadata)

def find_meta(data, meta_entries, metadata):
    """
    This method just iterates over each meta entry and appends it to the 
    metadata variable.
    """
    for i in range(meta_entries):
        if data:
            metadata.append(data.pop(0))   
    return metadata


    
# Part 2
"""
This part of the problem threw me off because my first solution does not 
hold any information about the data structure. I realized that I would
need to build a tree structure in order to go back and retrieve each 
child of the root, and its corresponding metadata, without losing the
state of the entire structure. 

I built the class below, which I realize would have been way simpler
to do from the beggining. But whatever, it was still fun. 

"""
class navigation_system:
    """
    This class works pretty similar to the functions above in Part I, except I 
    use the class itself to make the recursive call on the trees children. 
    I think this is the simplest approach to recursion in Python anyways, but 
    I was not thinking about it in the first part. 
    """
    def __init__(self, lon):
        if lon:
            self.number_children = lon.pop(0)
            self.number_meta = lon.pop(0)
            self.children = [navigation_system(lon) for _ in range(self.number_children)]
            self.metadata = [lon.pop(0) for _ in range(self.number_meta)]

    def get_child_node(self, child_node):
        """
        If child node is within range of the root's children, 
        make recursive call to get_root
        """
        if child_node < len(self.children):
            return self.children[child_node].get_root_value()
        return 0

    def get_root_value(self):
        """
        Check if a node has children, if it does not return its metadata sum.
        Else create a list by calling get_child for each of its metadata
        values and return the sum of that list.
        """
        if not self.children:
            return sum(self.metadata)
        root_total = [self.get_child_node(i - 1) for i in self.metadata]
        return sum(root_total)

# Tests
"""
List in Python are mutable. 
If you are using the same list variable for more than one test make
sure to wrap it in list(). Fore example, list(numbers). 
 """ 

# Here are some extra tests to try
small_test_list = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
small_test_list2 = [2, 2, 0, 3, 1, 1, 2, 1, 0, 1, 12, 0, 1, 11, 20, 21, 50, 52]

# Test Part 1
print(sum(get_license(list(numbers))))
print(sum(get_license(list(numbers))))
# Test Part 2
test = navigation_system(list(numbers))
print(test.get_root_value())

# Thanks for the challenge! 