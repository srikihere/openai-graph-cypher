import os
os.environ['OPENAI_API_KEY'] ='ENTER'
os.environ['NEO4J_URL'] = "bolt://localhost:7687"
os.environ['NEO4J_USERNAME'] = 'neo4j'
os.environ['NEO4J_PASSWORD'] = 'neo4j123'

import os
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI

graph = Neo4jGraph(url=os.environ['NEO4J_URL'], username=os.environ['NEO4J_USERNAME'], password=os.environ['NEO4J_PASSWORD'])

graph.refresh_schema()
chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0), graph=graph, verbose=True
)

#chain.run("How many different directors are there in total? List the names of persons who directed")
chain.run("What is the current age of Tom Hanks ?")
