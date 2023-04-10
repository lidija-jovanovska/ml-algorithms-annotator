from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo)
from .nodeutils import NodeUtils


class Assumption(StructuredNode, NodeUtils):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    description = StringProperty()

    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_ASSUMPTION_OF')

    @property
    def serialize(self):
        return {
            'node_properties': {
                'node_id': self.node_id,
                'name': self.name,
                'description': self.description
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
