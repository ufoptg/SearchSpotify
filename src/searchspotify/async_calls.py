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
 
# THIS FILE IS RESPONSABLE FOR API CALLS

import aiohttp
from . import async_urlbuilder

async def call_acess_token(credentials):
    """
    Calls Spotify API to obtain an access token using client credentials asynchronously.

    :param credentials: Encoded client credentials.
    :return: Response object containing the access token.
    """
    endpoint = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    headers = {"Authorization": f"Basic {credentials}"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url=endpoint, data=data, headers=headers) as response:
            return await response.json()

async def call_search(access_token, args):
    """
    Calls Spotify API to search for entities using the provided access token and arguments asynchronously.

    :param access_token: Access token for authentication.
    :param args: Tuple of arguments for the search endpoint.
    :return: Response object containing the search results.
    """
    endpoint = await urlbuilder.search_endpoint(*args)  # Await the result of async call
    headers = {"Authorization": f"Bearer {access_token}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url=endpoint, headers=headers) as response:
            return await response.json()

async def call_track_preview(track_id, access_token):
    """
    Calls Spotify API to retrieve the preview URL for a given track asynchronously.

    :param track_id: Spotify track ID.
    :param access_token: Access token for authentication.
    :return: Preview URL if available, None otherwise.
    """
    endpoint = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url=endpoint, headers=headers) as response:
            if response.status == 200:
                track_data = await response.json()
                if "preview_url" in track_data:
                    return track_data["preview_url"]
    return None
