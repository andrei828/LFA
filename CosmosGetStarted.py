import azure.cosmos.cosmos_client as cosmos_client

config = {
    'ENDPOINT': 'https://testing-cosmosdb.documents.azure.com:443/',
    'PRIMARYKEY': 'cBq357xNNkAPREfczWrL9Jlq5ZmL4uuNC9bg1zn6Z15mQ5EP1SCZBg0lXXotAvaczuZhzzwwecEpkHCy0ZeOtQ==',
    'DATABASE': 'service',
    'CONTAINER': 'UsersContainer'
}

enviroment = {
	'DATABASE_LINK': 'dbs/service',
	'CONTAINER_LINK': 'dbs/service/colls/UsersContainer'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})

# Create a database
#db = client.CreateDatabase({'id': config['DATABASE']})

# Create container options  
options = {
    'offerThroughput': 400
}

container_definition = {
    'id': config['CONTAINER']
}

# Create a container
# container = client.CreateContainer(config['DATABASE'], container_definition, options)

# Create and add some items to the container
item1 = client.CreateItem(enviroment['CONTAINER_LINK'], {
    'id': '2',
    'name': 'Liviu Ungureanu',
    'age': 20,
    'Web Site': 0,
    'Cloud Service': 0,
    'Virtual Machine': 0,
    'message': 'Hello World from Server 1!'
    }
)


# Query these items in SQL
query = {'query': 'SELECT * FROM c'}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryItems(enviroment['CONTAINER_LINK'], query, options)
for item in iter(result_iterable):
    print("id:", item["id"])
    print("name:", item["name"])
    print("age:", item["age"])
    print()
