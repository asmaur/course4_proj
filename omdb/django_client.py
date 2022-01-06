from django.conf import settings

from omdb.OmdbClient import OmdbClient
import logging

logger = logging.getLogger(__name__)


def get_client_from_settings():
    """Create an instance of an OmdbClient using the OMDB_KEY from the Django settings."""
    return OmdbClient(settings.OMDB_KEY)