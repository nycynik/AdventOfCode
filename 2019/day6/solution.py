# Day 6
#
# Simply makes a tree and increases the count per node by adding one to the parent

import sys
from anytree import Node, RenderTree


# Read the data
def read_command_line():
    if len(sys.argv) >= 2 and len(sys.argv[1]) > 0:
        return sys.argv[1]
    else:
        print("Please include the test data file as a command line argument.")


def find_orbits(file_name):
    data = open(file_name, "r")

    # build tree
    # walk tree to score it, COM=0, it's childrent all get 1, etc

    # init set
    orbits = {}

    for orbit_pair_raw in data:
        # print('\n', orbit_pair_raw)
        orbit_pair = orbit_pair_raw.strip().split(')')
        parent_name = orbit_pair[0]
        child_name = orbit_pair[1]

        # find or create parent.
        if parent_name not in orbits:
            orbits[parent_name] = Node(parent_name, val=0)
            # print(orbits[parent_name]) # new parent added
        parent_node = orbits[parent_name]

        # add child to the universe
        if child_name not in orbits:
            child_node = Node(child_name, val=parent_node.val + 1, parent=parent_node)
            orbits[child_name] = child_node
        else:
            # since child exists, we need to set it's parent and update its value.
            child_node = orbits[child_name]
            child_node.parent = parent_node
        # print(child_node)

    # print(orbits)

    # find the sum
    # print(sum(orbits.values()))
    total = 0
    for node in orbits.values():
        total += node.depth

    print("TOTAL:", total)

    if 'YOU' in orbits and 'SAN' in orbits:

        # choose one, and find all children, walk children and check if it is in
        # the children of the second, once a common ancestor is found, we have a solution.
        my_children = {}
        for node in orbits['YOU'].ancestors:
            my_children[node.name] = node

        best_match = None
        for node in orbits['SAN'].ancestors:
            if node.name in my_children:
                best_match = node

        if best_match is not None:
            distance = 0
            start = orbits['YOU'].parent
            while start.name != best_match.name:
                start = start.parent
                distance += 1

            start = orbits['SAN'].parent
            while start.name != best_match.name:
                start = start.parent
                distance += 1

        print('found it', distance)

    data.close()


if __name__ == "__main__":
    find_orbits(read_command_line())

