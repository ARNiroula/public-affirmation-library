import boto3
import os
from botocore.exceptions import EndpointConnectionError, ClientError

# Load environment variables (if you're not using Django settings directly)
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "minio")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "minio123")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME", "library")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_URL", "http://localhost:9000")


def test_minio():
    print("Connecting to MinIO...")

    try:
        s3 = boto3.client(
            "s3",
            endpoint_url=AWS_S3_ENDPOINT_URL,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        print("Listing buckets...")
        buckets = s3.list_buckets()
        for b in buckets.get("Buckets", []):
            print(f" - {b['Name']}")

        print(f"Uploading test.txt to bucket '{AWS_STORAGE_BUCKET_NAME}'...")
        s3.put_object(
            Bucket=AWS_STORAGE_BUCKET_NAME,
            Key="test.txt",
            Body=b"Hello, MinIO from Django!",
        )

        print("Download the object to verify...")
        obj = s3.get_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key="test.txt")
        content = obj["Body"].read().decode("utf-8")
        print("File content:", content)
        print(" MinIO connection test successful!")

    except EndpointConnectionError as e:
        print("Failed to connect to MinIO endpoint:", e)
    except ClientError as e:
        print(" AWS Client error:", e)
    except Exception as e:
        print(" Unexpected error:", e)


if __name__ == "__main__":
    test_minio()
