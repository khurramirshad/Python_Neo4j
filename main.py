import os
from neo4j import GraphDatabase, basic_auth


driver = GraphDatabase.driver('bolt://localhost:7687',auth=basic_auth("neo4j","12345678"))

def get_db():
    if not hasattr(g,'neo4j_db'):
        g.neo4j_db= driver.session()
    return g.neo4j_db


unique_transaction_types = ["MATCH (n) RETURN n LIMIT 25"]

def get_data(transaction_execution_commands, return_result = False):
    data_base_connection = GraphDatabase.driver(uri = "bolt://localhost:7687", auth=("neo4j", "12345678"))
    session = data_base_connection.session()
    #session = get_db()
    return_list = []
    
    for i in transaction_execution_commands:
        transaction_result = session.run(i)
        return_list = [j[0] for j in transaction_result]
    
    if return_result:
        return return_list

unique_transaction_results = get_data(unique_transaction_types, True)
print(unique_transaction_results)



#Create custom labels for each node representing its transaction type

# create_labels_commands = []
# for i in unique_transaction_results:
#     create_labels_commands.append("match (t:Transaction) where t.transaction_type = '" + i + "' set t :" + i )
# print(create_labels_commands)
# execute_transactions(create_labels_commands)