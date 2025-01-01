def ListssAdder(list1, list2):
    return [item1 + item2 for item1, item2 in zip(list1, list2)]

def ListssSubtractor(list1, list2):
    return [item1 - item2 for item1, item2 in zip(list1, list2)]

def ListssMultiplier(list1, list2):
    return [item1 * item2 for item1, item2 in zip(list1, list2)]

def ListssDivider(list1, list2):
    return [item1 / item2 for item1, item2 in zip(list1, list2)]

def ListssPower(list1, list2):
    return [item1 ** item2 for item1, item2 in zip(list1, list2)]