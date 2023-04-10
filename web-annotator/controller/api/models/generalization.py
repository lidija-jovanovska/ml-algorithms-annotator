from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo,
                      IntegerProperty)
from .nodeutils import NodeUtils


class GeneralizationSpecification(StructuredNode, NodeUtils):
    uid = UniqueIdProperty()
    node_id = StringProperty(index=True)
    name = StringProperty()

    BAYES = 0
    DECISION_RULES = 1
    DECISION_TREES = 2
    GRAPHICAL_MODELS = 3
    MARKOV = 4
    NEURAL = 5
    OTHER = 6

    LANGUAGES = {
        BAYES: 'LANGUAGE OF BAYESIAN NETS',
        DECISION_RULES: 'LANGUAGE OF DECISION RULES',
        DECISION_TREES: 'LANGUAGE OF DECISION TREES',
        GRAPHICAL_MODELS: 'LANGUAGE OF GRAPHICAL MODELS',
        MARKOV: 'LANGUAGE_OF_MARKOV_CHAINS',
        NEURAL: 'LANGUAGE OF NEURAL NETS',
        OTHER: 'OTHER LANGUAGE'
    }

    generalization_language = IntegerProperty(required=True, choices=LANGUAGES)

    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_OUTPUT_OF')

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
        ]
