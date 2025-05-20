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

def delete_collection_content(client, class_name: str, delete_entire_collection: bool = False):
    """
    Delete content from a Weaviate collection
    
    Args:
        client: Weaviate client
        class_name: Name of the collection to delete content from
        delete_entire_collection: If True, deletes the entire collection. If False, only deletes the objects.
    """
    if not client.collections.exists(class_name):
        print(f"Collection '{class_name}' does not exist")
        return
    
    if delete_entire_collection:
        client.collections.delete(class_name)
        print(f"Collection '{class_name}' has been deleted")
    else:
        collection = client.collections.get(class_name)
        collection.data.delete_all()
        print(f"All objects in collection '{class_name}' have been deleted")

def create_schema(client, class_name):
    if client.collections.exists(class_name):
        client.collections.delete(class_name)
        print(f"Collection '{class_name}' has been deleted.")

    # Create schema for Slack messages
    collection = client.collections.create(
        name=class_name,
        properties=[
            wvc.config.Property(
                name="user",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="text",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="thread_replies",
                data_type=wvc.config.DataType.TEXT_ARRAY,
            ),
            wvc.config.Property(
                name="url",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="type",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="timestamp",
                data_type=wvc.config.DataType.TEXT,
            )
        ]
    )

    print(f"Schema created for collection '{class_name}'")
    return collection