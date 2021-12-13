from collections import deque

def search(name):
    
    # create new queue
    search_queue = deque()

    # adds all neightbors of name to queue
    search_queue += graph[name]
    searched = []

    # while queue isn't empty
    while search_queue:
        print(search_queue)

        # grab the leftmost person off queue
        person = search_queue.popleft()

        # only search if haven't searched them yet
        if person not in searched:

            # check whether mango seller
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                # add new persons connections
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == "m"

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")