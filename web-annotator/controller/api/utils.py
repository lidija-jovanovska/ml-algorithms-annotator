from .models import Algorithm
# from .constants import ALGORITHMS
from django.core.validators import EmailValidator, ValidationError
from django.core.mail import send_mail
from django.conf import settings
import random

def _send_email(email=None, link=None):
    send_mail(
        subject='E-mail validation for Algorithm Annotator',
        message=f'Please click on the following link {link} to verify your email.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )

def _generate_token_and_link(domain_name=None):
    token = str(random.random()).split('.')[1]
    # link = f'http://{domain_name}/verify/{token}'
    link = f'http://{domain_name}/api/verify/{token}'
    return token, link

def _validate_email(email=None):
    validator = EmailValidator()
    try:
        validator(email)
    except ValidationError:
        return False
    return True


MODEL_ENTITIES = {
    'Algorithm': Algorithm
}


# Filter nodes helper
# Note: need to set some default params or kwargs manipulation to not pass all possible parameters

def filter_nodes(node_type, search_text):
    node_set = node_type.nodes

    if node_type.__name__ == 'Algorithm':
        node_set.filter(name__icontains=search_text)

    # if node_type.name == 'Assumption':
    #     node_set.filter(name__icontains=search_text)

    return node_set


# Count nodes helper: returns length of specified node_set

# count_info = {
#     'node_type': '',
#     'name': '',
# }


def count_nodes(count_info):
    count = {}
    node_type = count_info['node_type']
    search_word = count_info['name']
    node_set = filter_nodes(MODEL_ENTITIES[node_type], search_word)
    count['count'] = len(node_set)

    return count


# Fetch nodes helper: returns a node subset with specified index and length

# fetch_info = {
#     'node_type': '',
#     'node_id': '',
#     'limit': 10,
#     'page': 1
# }

def fetch_nodes(fetch_info):
    node_type = fetch_info['node_type']
    search_word = fetch_info['name']
    limit = fetch_info['limit']
    start = fetch_info((fetch_info['page'] - 1) * limit)
    end = start + limit
    node_set = filter_nodes(MODEL_ENTITIES[node_type], search_word)
    fetched_nodes = node_set[start:end]

    return [node.serialize for node in fetched_nodes]


# Fetch node details helper: return single node details

# node_info = {
#     'node_type': '',
#     'node_id': ''
# }


def fetch_node_details(node_info):
    node_type = node_info['node_type']
    node_id = node_info['node_id']
    node = MODEL_ENTITIES[node_type].nodes.get(node_id=node_id)
    node_details = node.serialize
    # set node_connections key as empty array
    node_details['node_connections'] = []
    # check if node has connections and serialize method and set it accordingly
    if hasattr(node, 'serialize_connections'):
        node_details['node_connections'] = node.serialize_connections

    return node_details


# def fetch_algorithms():
#     return ALGORITHMS
