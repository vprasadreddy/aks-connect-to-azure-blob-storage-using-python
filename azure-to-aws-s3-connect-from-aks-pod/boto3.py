import boto3

def main():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    print(response)

if __name__ == "__main__":
    main()
