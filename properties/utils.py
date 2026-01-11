import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    all_properties = cache.get('all_properties')
    if not all_properties:
        all_properties = Property.objects.all()
        cache.set('all_properties', all_properties, 3600)
    return all_properties

def get_redis_cache_metrics():
    """
    Retrieve and analyze Redis cache hit/miss metrics.
    """
    try:
        # Connect to Redis via django_redis
        redis_conn = get_redis_connection("default")
        
        # Get keyspace_hits and keyspace_misses from INFO
        info = redis_conn.info()
        hits = int(info.get('keyspace_hits', 0))
        misses = int(info.get('keyspace_misses', 0))
        
        # Calculate hit ratio
        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0
        
        metrics = {
            'hits': hits,
            'misses': misses,
            'hit_ratio': hit_ratio
        }
        
        # Log metrics
        logger.info(f"Redis Metrics: {metrics}")
        
        return metrics
    except Exception as e:
        logger.error(f"Error retrieving Redis metrics: {e}")
        return {'error': str(e)}
