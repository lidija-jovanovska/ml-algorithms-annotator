from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo)
from .nodeutils import NodeUtils


class Document(StructuredNode, NodeUtils):
    node_id = StringProperty(index=True)
    name = StringProperty()
    uid = UniqueIdProperty()

    # DOI/ISBN
    document_id = StringProperty()

    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'DESCRIBES')

    @property
    def serialize(self):
        return {
            'node_properties': {
                'node_id': self.node_id,
                'name': self.name
            }
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Algorithm',
                'nodes_related': self.serialize_relationships(self.algorithms.all())
            }
        ]
