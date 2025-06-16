from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import os

# Replace with your storage account and container details
# STORAGE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
# CONTAINER_NAME = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

STORAGE_ACCOUNT_NAME = "demoakstgacc123"
CONTAINER_NAME = "test-container"

# Construct the storage account URL
account_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"

# Use DefaultAzureCredential (supports workload identity in AKS)
credential = DefaultAzureCredential()

# Create the BlobServiceClient
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

# Get the container client
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# List blobs in the container
print(f"Blobs in container '{CONTAINER_NAME}':")
for blob in container_client.list_blobs():
    print(f" - {blob.name}")
