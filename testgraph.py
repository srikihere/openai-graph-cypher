from neo4j import GraphDatabase, basic_auth

uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
username = "neo4j"
password = "neo4j123"

#driver = GraphDatabase.driver(uri, auth=(username, password))

#query = "MATCH (p:Person) RETURN p.name AS name"
#with driver.session(database='neo4j') as session:
#    result = session.run(query)
#    for record in result:
#        print(record["name"])


driver = GraphDatabase.driver(
  "enter url",
  auth=basic_auth("neo4j", "cell-signal-fists"))

#working
cypher_query = "MATCH (n) RETURN COUNT(n) AS count"
with driver.session(database="neo4j") as session:
    result = session.run(cypher_query)
    for record in result:
        print(record["count"])
#working end

#    results = session.execute_read(
#        lambda tx: tx.run(cypher_query).data())
#    for record in results:
#        print(record['count'])

#driver.close()


# Define a function to export the entire database to a Cypher dump file
def export_neo4j_to_cypher_dump():
    with driver.session() as session:
        # Export all nodes and relationships to the Cypher dump file
        query = """
        CALL apoc.export.cypher.all(null, {stream: true})
        """
        session.run(query)

# Call the function to export the database
#export_neo4j_to_cypher_dump()
