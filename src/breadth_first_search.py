from collections import deque

def search(users_graph):
    if users_graph is None:
        raise Exception("No user graph provided")
    
    search_queue = deque()
    search_queue.insert(0, "you")
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if _is_mango_seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += users_graph[person]
                searched.append(person)
    return False

#
# If the name ends with the letter 'm', then we consider the user to be a mango seller
#
def _is_mango_seller(name):
    return name[-1] == "m"