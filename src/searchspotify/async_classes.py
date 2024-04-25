#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
# Nimbus ~ UserBot
# Copyright (C) 2023 NimbusTheCloud, ufoptg, @TrueSaiyan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# This file is a part of < https://github.com/ufoptg/Nimbus/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ufoptg/Nimbus/blob/main/LICENSE/>.
# If not, see <https://www.gnu.org/licenses/>.

# THIS FILE IS RESPONSABLE FOR MANY CLASS DECLARATIONS

import json
import math
from base64 import b64encode
from urllib.request import urlretrieve

from . import async_calls, constructor


class Authenticator:
    """
    Handles authentication and token retrieval for Spotify API.
    """

    def __init__(self, client_id: str, client_secret: str):
        """
        Initializes the Authenticator with client credentials.

        :param client_id: Spotify client ID.
        :param client_secret: Spotify client secret.
        """
        self.credentials = self.encode_credentials(client_id, client_secret)

    def encode_credentials(self, client_id, client_secret):
        """
        Encodes client credentials for token retrieval.

        :param client_id: Spotify client ID.
        :param client_secret: Spotify client secret.
        :return: Encoded credentials.
        """
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = b64encode(credentials.encode("utf-8"))
        return str(encoded_credentials, "utf-8")

    async def get_access_token(self):
        """
        Retrieves access token using encoded credentials asynchronously.

        :return: Access token.
        """
        response = await calls.call_acess_token(self.credentials)
        return response["access_token"]

