from bs4 import BeautifulSoup
from bs4.element import Tag


def convert_node_to_json(xml_node, is_root=True):
    node_list = []
    for item in xml_node:
        if isinstance(item, Tag):
            if item.is_empty_element:
                if is_root:
                    return {item.name: ""}
                node_list.append(
                    {item.name: ""}
                )
            elif len(item.findChildren()) == 0:  # is a Leaf Node
                if is_root:
                    return {item.name: item.getText()}
                node_list.append(
                    {item.name: item.getText()}
                )
            else:
                # the node is a Non Leaf
                nodes = []
                for node in item.children:
                    if isinstance(node, Tag):
                        nodes.append(
                            {
                                node.name: convert_node_to_json(node, is_root=False)
                            }
                        )

                return {
                    item.name: nodes
                }
    return node_list


def convert_to_json(xml_content):
    parser = BeautifulSoup(xml_content, "xml")
    dict_obj = convert_node_to_json(parser)
    return dict_obj
