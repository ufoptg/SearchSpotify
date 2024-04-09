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

# THIS FILE IS RESPONSABLE FOR DEALING WITH THE CLIENT

import re
import requests
from bs4 import BeautifulSoup
from . import calls
from .classes import Authenticator, Results


class Client:

    def __init__(self, client_id, client_secret):
        self.auth = Authenticator(client_id, client_secret)

    def search(
        self,
        keywords: str,
        *,
        types: list = ["track"],
        filters: dict = {},
        market: str = None,
        limit: int = None,
        offset: int = None
    ) -> Results:
        access_token = self.auth.get_acess_token()

        if "spotify.com/track" in keywords:
            title = self.extract_title(keywords)
            if title:
                keywords = title

        elif "spotify.com" in keywords:
            entities = ["track", "playlist", "album", "artist"]
            for entity in entities:
                if entity in keywords:
                    entity_id = self.extract_id(keywords, entity)
                    if not entity_id:
                        raise ValueError(f"Invalid {entity.capitalize()} link")
                    keywords = f"{entity}::{entity_id}"
                    break
            else:
                raise ValueError("Unsupported Spotify link")


        args = (keywords, types, filters, market, limit, offset)
        response = calls.call_search(access_token, args)
        return Results(response.json())

    def extract_id(self, link, entity):
        """
        Extracts ID from the Spotify link based on the entity type.
        :param link: Spotify link
        :param entity: Entity type (track, playlist, album, artist)
        :return: Extracted ID or None if not found
        """
        pattern = rf'/{entity}/([a-zA-Z0-9]+)'
        match = re.search(pattern, link)
        if match:
            return match.group(1)
        return None

    def extract_title(self, link):
        """
        Extracts the title from the Spotify link.
        :param link: Spotify link
        :return: Extracted title or None if not found
        """
        try:
            response = requests.get(link)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, "html.parser")
                title_tag = soup.find("title")
                title = title_tag.text if title_tag else None
                if title and " - " in title and "by" in title:
                    title_parts = title.split(" - ", 1)
                    if len(title_parts) > 1:
                        title = (
                            title_parts[0].strip()
                            + " "
                            + title_parts[1].split(" by ", 1)[-1].strip()
                        )
                    else:
                        title = title_parts[0].strip()
                if title and "| Spotify" in title:
                    title = title.split("| Spotify")[0].strip()
                return title
        except Exception as e:
            print(f"Error extracting title: {e}")
        return None