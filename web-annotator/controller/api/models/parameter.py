from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, IntegerProperty, RelationshipTo)
from .nodeutils import NodeUtils


class Parameter(StructuredNode, NodeUtils):
    uid = UniqueIdProperty()
    node_id = StringProperty(index=True)
    name = StringProperty()

    ALG_PARAM = 0
    ALG_HYPERPARAM = 1
    MODEL_PARAM = 2

    INT = 3
    BOOL = 4
    REAL = 5
    DICT = 6
    DISCRETE = 7
    OTHER = 8
    FUNCTION = 9

    TYPES = {ALG_PARAM: 'ALGORITHM_PARAMETER',
             ALG_HYPERPARAM: 'ALGORITHM_HYPERPARAMETER',
             MODEL_PARAM: 'MODEL_PARAMETER'}

    DATATYPES = {INT: 'integer',
                 BOOL: 'boolean',
                 REAL: 'real',
                 DICT: 'dictionary',
                 DISCRETE: 'discrete',
                 OTHER: 'other',
                 FUNCTION: 'function'
    }

    type = IntegerProperty(required=True, choices=TYPES)
    datatype = IntegerProperty(choices=DATATYPES)

    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_PARAMETER_OF')

    @property
    def serialize(self):
        return {
            'node_properties': {
                'node_id': self.node_id,
                'name': self.name,
                'type': self.type
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

