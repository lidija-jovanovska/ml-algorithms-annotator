from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo,
                      Relationship, One, ZeroOrOne, OneOrMore, BooleanProperty)
from .dm_algorithm import DataMiningAlgorithm

class EnsembleAlgorithm(DataMiningAlgorithm):
    ensemble = BooleanProperty(default=True)
    learning = StringProperty(default=None)


class BaggingAlgorithm(EnsembleAlgorithm):
    learning = StringProperty(default='parallel')
    base_estimator = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'HAS_BASE_ESTIMATOR', cardinality=One)
    sampling = RelationshipTo('.sampling.Sampling', 'HAS_PART', cardinality=One)


class BoostingAlgorithm(EnsembleAlgorithm):
    learning = StringProperty(default='sequential')
    base_estimator = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'HAS_BASE_ESTIMATOR', cardinality=One)


class VotingAlgorithm(EnsembleAlgorithm):
    learning = StringProperty(default='parallel')
    estimators = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'HAS_ESTIMATOR', cardinality=OneOrMore)


class StackingAlgorithm(EnsembleAlgorithm):
    learning = StringProperty(default='parallel')
    estimators = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'HAS_ESTIMATOR', cardinality=OneOrMore)
    final_estimator = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'HAS_FINAL_ESTIMATOR', cardinality=One)