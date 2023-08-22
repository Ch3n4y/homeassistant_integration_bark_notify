"""Bark notification service."""

import logging
import requests
import voluptuous as vol
from homeassistant.const import CONF_URL, CONF_TOKEN
import homeassistant.helpers.config_validation as cv
from homeassistant.components.notify import (
    ATTR_TITLE_DEFAULT,
    ATTR_TITLE,
    ATTR_DATA,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)

CONF_KEY = 'key'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_KEY): cv.string,
    vol.Optional(CONF_URL, default='https://api.day.app'): cv.url,
    vol.Optional('sound'): cv.string,
    vol.Optional('icon'): cv.url,
    vol.Optional('group'): cv.string,
    vol.Optional('isArchive'): cv.boolean,
    vol.Optional('url'): cv.url,
    vol.Optional('level'): vol.In(['active', 'timeSensitive', 'passive']),
    vol.Optional('badge'): vol.Coerce(int),
    vol.Optional('autoCopy'): cv.boolean,
    vol.Optional('copy'): cv.string
})

_LOGGER = logging.getLogger(__name__)

def get_service(hass, config, discovery_info=None):
    url = config.get(CONF_URL)
    key = config[CONF_KEY]
    return BarkNotifyService(url, key, config)


class BarkNotifyService(BaseNotificationService):
    def __init__(self, url, key, config):
        self._url = url
        self._key = key
        self._config = config

    def send_request(self, url, data):
        return requests.post(url, headers={'Content-Type': 'application/json; charset=utf-8'}, json=data, timeout=10)

    async def async_send_message(self, message: str, **kwargs: Any):
        title = kwargs.get(ATTR_TITLE, ATTR_TITLE_DEFAULT)
        data = kwargs.get(ATTR_DATA, {})
        
        payload = {
            'body': message,
            'title': title,
            'device_key': self._key,
            'sound': data.get('sound', self._config.get('sound')),
            'icon': data.get('icon', self._config.get('icon')),
            'group': data.get('group', self._config.get('group')),
            'isArchive': data.get('isArchive', self._config.get('isArchive')),
            'url': data.get('url', self._config.get('url')),
            'level': data.get('level', self._config.get('level')),
            'badge': data.get('badge', self._config.get('badge')),
            'autoCopy': data.get('autoCopy', self._config.get('autoCopy')),
            'copy': data.get('copy', self._config.get('copy'))
        }

        # Filter out None values
        payload = {k: v for k, v in payload.items() if v is not None}

        _LOGGER.debug('Sending message to Bark: %s', payload)

        try:
            response = await self.hass.async_add_executor_job(self.send_request, f"{self._url}/push", payload)
            response.raise_for_status()
        except Exception as ex:
            _LOGGER.error('Error while sending Bark message: %s', ex)


