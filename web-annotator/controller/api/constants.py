from neomodel import db

# We created the constants.py module because we want to make the cypher queries once.
# Not each time we call fetch_countries, fetch_jurisdictions or fetch_data_source helpers.
# Since these queries might take some time to execute, we want them ready at the start of the application.
# We can do that by executing the constants.py code.

# get all algorithms nodes names

algorithms = db.cypher_query(
    '''
    MATCH (n:Algorithm)
    RETURN DISTINCT n.name
    '''
)[0]

ALGORITHMS = sorted(algorithm[0] for algorithm in algorithms)

# if __name__ == '__main__':


