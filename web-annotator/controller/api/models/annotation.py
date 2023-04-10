from neomodel import (
    StructuredNode,
    StringProperty,
    DateTimeProperty,
    EmailProperty,
    BooleanProperty, UniqueIdProperty
)

from .nodeutils import NodeUtils


class Annotation(StructuredNode, NodeUtils):

    uid = UniqueIdProperty()
    node_id = StringProperty(index=True)
    annotator_name = StringProperty()
    affiliation = StringProperty()
    email = EmailProperty(required=True)
    # creation_date = DateTimeProperty(default_now=True)
    token = StringProperty()
    is_verified = BooleanProperty(default=False)


    @property
    def serialize(self):
        return {
            'node_properties': {
                'node_id': self.node_id,
                'annotator_name': self.name,
                'annotation_creation_date': self.annotation_creation_date,
                'annotator_email': self.annotator_email
            }
        }