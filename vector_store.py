import weaviate
import weaviate.classes as wvc

def initialize_vector_store():
    client = weaviate.connect_to_local()
    return client

def add_to_vector_store(client, class_name, embeddings, properties):
    message_collection = client.collections.get(class_name)
    try:
        message_collection.data.insert(uuid=uuid, properties=properties, vector=embeddings)
    finally:
        client.close()

def create_schema(client, class_name):
    if client.collections.exists(class_name):
        client.collections.delete(class_name)
        print(f"Collection '{class_name}' has been deleted.")

    #todo: have a better schema
    questions = client.collections.create(
        name=class_name,
        properties=[
            wvc.config.Property(
                name="text",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="file_path",
                data_type=wvc.config.DataType.TEXT,
            )
        ]
    )

    print(questions.config.get(simple=False))
    print("schema created")