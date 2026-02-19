import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis keyspace hit/miss metrics and calculate hit ratio.
    Returns:
        dict: {'hits': int, 'misses': int, 'hit_ratio': float}
    """
    try:
        # Connect to the default Redis cache
        redis_conn = get_redis_connection("default")
        info = redis_conn.info("stats")  # get Redis statistics

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total = hits + misses
        hit_ratio = hits / total if total > 0 else 0.0

        metrics = {
            "hits": hits,
            "misses": misses,
            "hit_ratio": hit_ratio,
        }

        logger.info(f"Redis cache metrics: {metrics}")
        return metrics

    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {"hits": 0, "misses": 0, "hit_ratio": 0.0}
