from django.urls import path, include
from .views import verify
#
# urlpatterns = [
#     path('', main)
# ]

from django.conf.urls import url
from .views import (
    GetAlgorithms,
    PostAnnotation,
    SimpleAlgorithms,
    SingleGeneralizationAlgorithms,
    DataMiningAlgorithms
)

urlpatterns = [
    url(r'^algorithms[/]?$', GetAlgorithms.as_view(), name='get_algorithms'),
    url(r'^annotations[/]?$', PostAnnotation.as_view(), name='post_annotation'),
    url(r'^simple_algorithms[/]?$', SimpleAlgorithms.as_view(), name='simple_algorithms'),
    url(r'^single_generalization_algorithms[/]?$', SingleGeneralizationAlgorithms.as_view(), name='single_generalization_algorithms'),
    url(r'^data_mining_algorithms[/]?$', DataMiningAlgorithms.as_view(), name='data_mining_algorithms'),
    # path(r'verify/?$', verify, name='verify_email')
    path('verify/<str:token>', verify, name='verify_email')
]
