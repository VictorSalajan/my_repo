class Stuff(object):
    def __init__(self, name, value, weight):
        self.weight = weight
        self.value = value
        self.name = name

    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def getName(self):
        return self.name

    def __repr__(self):
        return '<' + str(self.value) + ', ' + str(self.weight) + '>'

dirt = Stuff('dirt', 0, 4)
computer = Stuff('computer', 30, 10)
fork = Stuff('fork', 1, 5)
problem_set = Stuff('problem_set', -10, 0)

items = [dirt, computer, fork, problem_set]

def density_metric(item):
    try:
        return item.getValue() / item.getWeight()
    except:
        return 0

def weight_metric(item):
    """ Prioritizes lighter objects """
    return -item.getWeight()

def value_metric(item):
    return item.getValue()

metrics = [density_metric, weight_metric, value_metric]


def sort_items(metric, items):
    """
    Input: metric, items 
    Returns sorted list of object of class Stuff
    Sorting criteria: specified metric
    Algorithm for sorting: Selection Sort, decreasing order 
    """
    for i in range(len(items) - 1):
        j = i + 1
        while j < len(items):
            if metric(items[j]) > metric(items[i]):
                items[i], items[j] = items[j], items[i]
            j += 1
    return items

def optimize(sort_items):
    """
    Input: function sort_items - a list of objects ordered by a metric
    Returns optimized list by eliminating objects with value <= 0
    """
    for obj in items[:]:
        if obj.getValue() <= 0:
            items.remove(obj)
    return items

def knapsack_results_by_metric(metric):
    """
    Returns Knapsack contents, weight & value, 
    according to optimization criteria (metric)
    """
    count = 0
    knapsack_weight = 0
    knapsack_contents = []
    items_ordered = sort_items(metric, items)
    for el in items_ordered:
        while knapsack_weight <= 14 and count <= len(items_ordered):
            count += 1
            val = el.weight
            knapsack_weight += val
            knapsack_contents.append(el)
            if knapsack_weight > 14:
                knapsack_weight -= val
                knapsack_contents.remove(el)
            break
    return f'Knapsack contains: {knapsack_contents} --> {[obj.getName() for obj in knapsack_contents]}\n' \
           f'Knapsack weight: {knapsack_weight}\n' \
           f'Knapsack value: {sum([obj.getValue() for obj in knapsack_contents])}'


for metric in metrics:
    print(f'Items ordered by {metric.__name__}: {sort_items(metric, items)}\n')
    print(knapsack_results_by_metric(metric), '\n')

print('\n<<< Optimized metric - eliminating useless objects (value <= 0) >>>\n')

for metric in metrics:
    print(f'Items ordered by {metric.__name__}: {optimize(sort_items(metric, items))}\n')
    print(knapsack_results_by_metric(metric), '\n')
