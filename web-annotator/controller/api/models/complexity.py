from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo, One)
from .nodeutils import NodeUtils


class Complexity(StructuredNode, NodeUtils):
    uid = UniqueIdProperty()
    node_id = StringProperty(index=True)
    name = StringProperty(unique_index=True)
    big_o = StringProperty()
    description = StringProperty()

    # TRAIN = 0,
    # TEST = 1,
    # SPACE = 2,
    #
    # TYPES = {TRAIN: 'TRAIN_TIME_COMPLEXITY',
    #          TEST: 'TEST_TIME_COMPLEXITY',
    #          SPACE: 'SPACE_COMPLEXITY'}
    # type = StringProperty(required=True, choices=TYPES)

    # Example: how to get val and display val of choice
    # tim = Person(sex='M').save()
    # tim.sex  # M
    # tim.get_sex_display()  # 'Male'

    # Example: array property
    # names = ArrayProperty(StringProperty(), required=True)


    train_algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_TRAIN_TIME_COMPLEXITY_OF', cardinality=One)
    test_algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_TEST_TIME_COMPLEXITY_OF')
    space_algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_SPACE_COMPLEXITY_OF')

    @property
    def serialize(self):
        return {
            'node_properties': {
                'node_id': self.node_id,
                'name': self.name,
            }
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Algorithm',
                'nodes_related': self.serialize_relationships(self.train_algorithms.all())
            },
            {
                'nodes_type': 'Algorithm',
                'nodes_related': self.serialize_relationships(self.test_algorithms.all())
            },
            {
                'nodes_type': 'Algorithm',
                'nodes_related': self.serialize_relationships(self.space_algorithms.all())
            },
        ]
