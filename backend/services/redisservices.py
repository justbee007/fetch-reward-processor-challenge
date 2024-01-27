import redis
import json, os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logfile.log")
logger.addHandler(file_handler)
try:
    # Establish a connection to the Redis server
    redis_url = os.environ.get(
        "REDIS_HOST", "localhost"
    )  # Default to localhost if not set
    redis_port = os.environ.get("REDIS_PORT", 6379)
    connection = redis.Redis(
        host=redis_url, port=int(redis_port), decode_responses=True
    )
    if connection.ping() == False:
        raise Exception
    else:
        logger.debug("Connection to redis was successful")
except Exception as e:
    logger.error("Unable to connect to redis")
    # Handle connection errors

    print(f"Error establishing Redis connection: {e}")


def insertReceipt(receiptId, receiptJson):
    try:
        # Convert the receiptJson dictionary to a JSON string
        receiptJsonString = json.dumps(receiptJson)

        # Store the JSON string in Redis with the provided receiptId as the key
        connection.set(receiptId, receiptJsonString)

    except Exception as e:
        # Handle errors during JSON conversion or Redis insertion
        print(f"Error inserting receipt into Redis: {e}")
        raise Exception

    # Return True to indicate successful insertion
    return True


def getReceipt(receiptId):
    # Retrieve the JSON string from Redis using the provided receiptId
    receiptJsonString = connection.get(receiptId)

    # Check if the receiptId is not found in Redis
    if receiptJsonString is None:
        # Raise an exception to indicate that the receipt is not found
        raise Exception("Receipt not found in Redis")

    # Convert the JSON string back to a Python dictionary
    receiptJson = json.loads(receiptJsonString)

    # Return the retrieved receipt as a dictionary
    return receiptJson
