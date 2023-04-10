from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo,
                      Relationship, One, ZeroOrOne, BooleanProperty, IntegerProperty)

class Sampling(StructuredNode):
    uid = UniqueIdProperty()

    TYPES = {0: 'sampling random subsets of the samples',
             1: 'sampling random subsets of the samples (with replacement)',
             2: 'sampling random subsets of the features',
             3: 'sampling random subsets of both samples and features'}

    type = IntegerProperty(required=True, choices=TYPES)
    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'HAS_PART')
    datasets = Relationship('.dataset.Dataset', 'HAS_PART')
