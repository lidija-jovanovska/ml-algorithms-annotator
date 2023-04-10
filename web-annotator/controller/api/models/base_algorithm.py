from neomodel import (
    StructuredNode,
    StringProperty,
    UniqueIdProperty,
    RelationshipTo,
    BooleanProperty )

class Algorithm(StructuredNode):
    # __abstract_node__ = True
    name = StringProperty(unique_index=True)
    uid = UniqueIdProperty()
    algorithms = RelationshipTo('.dm_algorithm.DataMiningAlgorithm', 'IS_PART_OF')
    data_mining_entity = BooleanProperty(default=False)

    @property
    def to_json(self):
        return {
            "id": self.uid,
            "name": self.name,
    }
