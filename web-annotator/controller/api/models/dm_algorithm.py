from neomodel import (db, StructuredNode, StringProperty, UniqueIdProperty, UniqueProperty, RelationshipTo,
                      Relationship, One, ZeroOrOne, BooleanProperty)
from .nodeutils import NodeUtils
from .base_algorithm import Algorithm


class DataMiningAlgorithm(NodeUtils, Algorithm):

    data_mining_entity = BooleanProperty(default=True)
    ensemble = BooleanProperty(default=False)
    algorithms = RelationshipTo('.base_algorithm.Algorithm', 'HAS_PART')

    assumptions = RelationshipTo('.assumption.Assumption', 'HAS_ASSUMPTION')
    documents = RelationshipTo('.document.Document', 'IS_DESCRIBED_IN')
    train_complexity = RelationshipTo('.complexity.Complexity', 'HAS_TRAIN_TIME_COMPLEXITY', cardinality=ZeroOrOne)
    test_complexity = RelationshipTo('.complexity.Complexity', 'HAS_TEST_TIME_COMPLEXITY', cardinality=ZeroOrOne)
    space_complexity = RelationshipTo('.complexity.Complexity', 'HAS_SPACE_COMPLEXITY', cardinality=ZeroOrOne)
    parameters = RelationshipTo('.parameter.Parameter', 'HAS_PARAMETER')
    datasets = RelationshipTo('.dataset.Dataset', 'HAS_INPUT', cardinality=ZeroOrOne)
    tasks = RelationshipTo('.task.Task', 'ADDRESSES', cardinality=ZeroOrOne)
    optimization_problem = RelationshipTo('.optimization_problem.OptimizationProblem', 'SOLVES', cardinality=ZeroOrOne)
    generalization_specifications = RelationshipTo('.generalization.GeneralizationSpecification', 'HAS_OUTPUT', cardinality=ZeroOrOne)

    annotation = Relationship('.annotation.Annotation', 'HAS_ANNOTATION')


    @property
    def serialize(self):
        return {
            'node_properties': {
                'node_id': self.node_id,
                'name': self.name
            }
        }

    @property
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "complexity": self.train_complexity.single().name if self.train_complexity else '',
            "task": self.tasks.single().name if self.tasks else '',
            "optimization_problem": self.optimization_problem.single().name if self.optimization_problem else '',
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Assumption',
                'nodes_related': self.serialize_relationships(self.assumptions.all())
            },
            {
                'nodes_type': 'Document',
                'nodes_related': self.serialize_relationships(self.documents.all())
            },
            {
                'nodes_type': 'Complexity',
                'nodes_related': self.serialize_relationships(self.train_complexity.all())
            },
            {
                'nodes_type': 'Complexity',
                'nodes_related': self.serialize_relationships(self.test_complexity.all())
            },
            {
                'nodes_type': 'Complexity',
                'nodes_related': self.serialize_relationships(self.space_complexity.all())
            },
            {
                'nodes_type': 'Parameter',
                'nodes_related': self.serialize_relationships(self.parameters.all())
            },
            {
                'nodes_type': 'Dataset',
                'nodes_related': self.serialize_relationships(self.datasets.all())
            },
            {
                'nodes_type': 'Task',
                'nodes_related': self.serialize_relationships(self.tasks.all())
            },
            {
                'nodes_type': 'OptimizationProblem',
                'nodes_related': self.serialize_relationships(self.optimization_problems.all())
            },
            {
                'nodes_type': 'GeneralizationSpecification',
                'nodes_related': self.serialize_relationships(self.generalization_specifications.all())
            },
            {
                'nodes_type': 'Annotation',
                'nodes_related': self.serialize_relationships(self.annotation.all())
            }
        ]