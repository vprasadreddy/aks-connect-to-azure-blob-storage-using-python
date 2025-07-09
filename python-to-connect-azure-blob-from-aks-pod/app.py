import os
import sys
import time

# Ensure the Azure SDK for Python is installed
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import AzureError

def main():
    try:
        # Use DefaultAzureCredential which supports Workload Identity
        credential = DefaultAzureCredential()

        # Replace with your storage account and container details
        STORAGE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
        CONTAINER_NAME = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

        # Replace with your actual storage account URL
        storage_account_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net"

        # Create the BlobServiceClient
        blob_service_client = BlobServiceClient(account_url=storage_account_url, credential=credential)

        # Get the ContainerClient
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # List blobs in the container
        print(f"Listing blobs in container: {CONTAINER_NAME}")
        blobs = container_client.list_blobs()

        for blob in blobs:
            print(f"- {blob.name}")

    except AzureError as e:
        print(f"Azure error occurred: {e}")
    except Exception as e:
        print(f"General error occurred: {e}")

if __name__ == "__main__":
    main()
    while True:
        time.sleep(60) # Keep the script running to maintain the connection
        # This is useful for debugging and testing purposes