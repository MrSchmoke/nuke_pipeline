import hou
import hapi

def print_node_path(node: hou.Node) -> None:
        """Print node's Path."""
        print(f"{node.path()}")

def length_of_two_added_vectors(a: hou.Vector3, b: hou.Vector3) -> hou.Vector3:
    """Return length of a sum of two vectors."""
    sum_vec: hou.Vector3 = a + b
    return sum_vec.length()

obj = hou.node('/obj')

def print_tree(node, indent=0):
    for child in node.children():
        print (" " * indent + child.name())
        print_tree(child, indent + 3)

print_node_path(obj)