from neomodel import (db, StructuredNode, StringProperty, UniqueProperty, UniqueIdProperty, RelationshipTo)
from .nodeutils import NodeUtils


class OptimizationProblem(StructuredNode, NodeUtils):
    uid = UniqueIdProperty()
    node_id = StringProperty(index=True)
    name = StringProperty(unique_index=True)
    math_desc = StringProperty()
    lang_desc = StringProperty()

    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_SOLVED_BY')

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