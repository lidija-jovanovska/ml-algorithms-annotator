from neomodel import db


class NodeUtils:

    def serialize_relationships(self, nodes):
        serialized_nodes = []
        for node in nodes:
            serialized_node = node.serialize

            # uncomment to check what it does (get relationship type apparently)
            # results, columns = self.cypher('''
            #     START start_node=node({self}), end_node=node({end_node})
            #     MATCH (start_node-[rel]-(end_node)
            #     RETURN type(rel) as node_relationship
            # ''',
            #                                {'end_node': node.id}
            #                                )

            serialized_nodes.append(serialized_node)

        return serialized_nodes
