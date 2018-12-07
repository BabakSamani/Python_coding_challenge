import Node
from LinkedList import *


def main():
    linked_list = LinkedList(head=None)

    # nodes = [
    #     Node({'name': "Babak", 'age': 38}),
    #     Node({'name': "Saeideh", 'age': 32}),
    #     Node({'name': "Jafar", 'age': 35}),
    #     Node({'name': "Saman", 'age': 23})
    # ]

    nodes = [
        Node("Babak"),
        Node("Saeideh"),
        Node("Jafar"),
        Node("Saman")
    ]

    for i in range(0, len(nodes)):
        linked_list.insert(nodes[i])

    print(linked_list.get_size())

    linked_list.publish()


if __name__ == '__main__':
    main()