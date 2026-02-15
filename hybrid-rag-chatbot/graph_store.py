import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv( override=True)

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(uri, auth=(user, password))

def graph_search(query):

    print("\n=== GRAPH QUERY EXECUTED ===")
    print(query)

    with driver.session() as session:
        result = session.run(query)

        data = []
        for record in result:
            data.append(record)

        print("\nGraph Results:")
        print(data)

        return str(data)
