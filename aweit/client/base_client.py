import aiohttp
import asyncio
import inspect
import logging

from await.api import BaseAPI


logger = logging.getLogger(__name__)


def _is_api_endpoint(obj):
    return isinstance(obj, BaseAPI)


class BaseClient:

    def __new__(cls, *args, **kwargs):
        obj = super(BaseClient, cls).__new__(cls, *args, **kwargs)
        api_endpoints = inspect.getmembers(obj, _is_api_endpoint)
        for name, api in api_endpoints:
            api_cls = type(api)
            api = api_cls(obj)
            setattr(obj, name, api)
        return obj

    def __init__(self, appid, access_token=None):
        """"""



