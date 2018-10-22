import aiohttp
import asyncio
import logging

from await.client.base_client import BaseClient


logger = logging.getLogger(__name__)


class EnterpriseClient(BaseClient):

    def __init__(self, corp_id, secret, access_token=None):
        super(EnterpriseClient, self).__init__()
        self.corp_id = corp_id
        self.secret = secret


