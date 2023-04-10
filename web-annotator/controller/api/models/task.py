from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo,
                      IntegerProperty, One)
from .nodeutils import NodeUtils


class Task(StructuredNode, NodeUtils):
    uid = UniqueIdProperty()
    node_id = StringProperty(index=True)
    name = StringProperty()
    ontology_id = StringProperty()

    ONLINE = 0
    BATCH = 1

    TYPES = {ONLINE: 'ONLINE_MODE',
             BATCH: 'BATCH_MODE'}
    mode = IntegerProperty(required=True, choices=TYPES)

    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_ADDRESSED_BY', cardinality=One)

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