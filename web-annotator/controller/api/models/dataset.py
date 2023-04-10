from neomodel import (db, Relationship, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo)
from .nodeutils import NodeUtils


class Dataset(StructuredNode, NodeUtils):
    uid = UniqueIdProperty()
    node_id = StringProperty(index=True)
    name = StringProperty()
    ontology_id = StringProperty()

    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_INPUT_OF')
    sampling = Relationship('.sampling.Sampling', 'HAS_PART')

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
