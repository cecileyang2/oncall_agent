import portkey_ai
import os

# https://doordash.atlassian.net/wiki/spaces/Eng/pages/3717661428/GenAI+Gateway+FAQs#Databricks
base_url = os.environ.get("PORTKEY_BASE_URL", "http://cybertron-service-gateway.service.prod.ddsd:8080/v1")
api_key = "+NZF4flAKntClRPhantgoT6xDE0n"
# NOTE: Fetch this from https://app.portkey.ai/virtual-keys
virtual_key = "openai-marketpl-2e986c"

def get_portkey_client():
    try:
        client = portkey_ai.Portkey(
            base_url=base_url,
            api_key=api_key,
            virtual_key=virtual_key,
        )
        return client
    except Exception as e:
        print(f"Error initializing Portkey client: {e}")
        raise

def get_vector(content: str):
    client = get_portkey_client()
    response = client.embeddings.create(input=content, model="text-embedding-3-large", encoding_format="float")
    return response

def generate_embeddings(content):
    return get_vector(content)





