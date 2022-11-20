import hou
# import hapi

# def print_node_path(node: hou.Node) -> None:
#         """Print node's Path."""
#         print(f"{node.path()}")

# def length_of_two_added_vectors(a: hou.Vector3, b: hou.Vector3) -> hou.Vector3:
#     """Return length of a sum of two vectors."""
#     sum_vec: hou.Vector3 = a + b
#     return sum_vec.length()

# obj = hou.node('/obj')

# def print_tree(node, indent=0):
#     for child in node.children():
#         print (" " * indent + child.name())
#         print_tree(child, indent + 3)

# print_node_path(obj)


#get obj context and create a geo container
def test():
    obj      = hou.node('/obj');
    geo_node = obj.createNode('geo', 'fx_source');

    #create all the nodes
    sphere_node = geo_node.createNode('sphere');
    mtn_node = geo_node.createNode('mountain::2.0');
    clip_node = geo_node.createNode('clip');
    fill_node = geo_node.createNode('polyfill');

    #set inputs
    mtn_node.setInput(0, sphere_node, 0);
    clip_node.setInput(0, mtn_node, 0);
    fill_node.setInput(0, clip_node, 0);
    geo_node.layoutChildren(); #sort nodes on networkview

    #set flags
    fill_node.setDisplayFlag(True);
    sphere_node.setRenderFlag(False);

    #set params
    sphere_node.parm('type').set(1);
    fill_node.parm('fillmode').set(0);