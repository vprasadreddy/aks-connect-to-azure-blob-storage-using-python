import boto3
from botocore.exceptions import ClientError
import os
import time

def main():
    bucket_name = "test-s3-bucket-access-from-aks-pod"

    role_arn = os.environ.get("AWS_ROLE_ARN")
    token_file = os.environ.get("AWS_WEB_IDENTITY_TOKEN_FILE")
    
    print("Checking environment variables for AWS federation:")

    if role_arn:
        print(f"AWS_ROLE_ARN is set: {role_arn}")
    else:
        print("AWS_ROLE_ARN is NOT set!")

    if token_file and os.path.exists(token_file):
        print(f"AWS_WEB_IDENTITY_TOKEN_FILE exists: {token_file}")
    else:
        print("AWS_WEB_IDENTITY_TOKEN_FILE is missing or path is incorrect!")

    # Optional: set region if needed
    session = boto3.session.Session(region_name='us-east-1')

    # Create S3 client (it will automatically use the federated credentials)
    s3_client = session.client('s3')

    try:
        print(f"Listing contents of S3 bucket: {bucket_name}\n")
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"{obj['LastModified']} - {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("Bucket is empty or not found.")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    while True:
        time.sleep(60) # Keep the script running to maintain the connection
        # This is useful for debugging and testing purposes
