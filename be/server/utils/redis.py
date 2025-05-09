# redis_client.py
import redis
import os

# Configure pool
pool = redis.ConnectionPool(
    host=os.environ.get("REDIS_HOST", "127.0.0.1"),
    port=os.environ.get("REDIS_PORT", 6379),
    db=os.environ.get("REDIS_DB", 0),
    decode_responses=True,  # If you want strings instead of bytes
)

# Redis client using the pool
redis_client = redis.Redis(connection_pool=pool)
