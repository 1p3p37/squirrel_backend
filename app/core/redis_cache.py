import functools
import logging
import json
import aioredis

from app.core.config import settings

# Asynchronous Redis connection
async def get_redis_connection():
    return await aioredis.from_url(
        settings.redis_url,
        encoding="utf-8",
        decode_responses=True,
    )


# Async cache decorator
def cache_response(ttl: int = 60):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            redis_client = await get_redis_connection()
            # Generate a cache key based on the function arguments
            cache_key = f"{func.__name__}:{str(args)},{str(kwargs)}"
            cached_response = await redis_client.get(cache_key)

            if cached_response is not None:
                return json.loads(cached_response)  # Deserialize the cached response

            response = await func(*args, **kwargs)
            logging.info(f"Cached response with {ttl} ttl: {response}")

            json_serializable_response = convert_to_json_serializable(response)
            await redis_client.setex(
                cache_key, ttl, json.dumps(json_serializable_response)
            )  # Cache the response as JSON
            return response

        return wrapper

    return decorator


def convert_to_json_serializable(data):
    # Implement conversion logic here
    # This function should convert non-serializable objects to JSON-serializable format
    # For example, if data is a list of SQLAlchemy ORM objects, convert them to dictionaries
    # You can use SQLAlchemy's built-in serialization methods or convert manually

    # Example: Convert a list of SQLAlchemy ORM objects to dictionaries
    if isinstance(data, list) and all(
        isinstance(item, YourORMBaseClass) for item in data
    ):
        return [item.to_dict() for item in data]

    # If no conversion is needed, return data as is
    return data
