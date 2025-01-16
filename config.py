"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", 28372387)
        self.API_HASH: str = os.environ.get("API_HASH", 11edc85521fb2d8f75e751bb284507e1)
        self.SESSION: str = os.environ.get("SESSION", BQGw7aMAmIJc10VKJtKHP_A4ACgoeV2dGiho_4_cD8K254m8tlfCCm4D56wW8x4SESqdPQFMzSzkiTh98RrqoI4Z2JkKC450WjyGuqZ8jUvqOwsiwrwvjQJNDJjzk88Qilx06xS6pVmh4hnszKHzmQDnd59tuG9dIO9J_ftcYrG9fWnRht9qtOS1g5Al5KZ_LJOTFnDqdHx_s4zp8tKNxaWwKZGAZUdPBv7TiMhhVIWdsWkqHxRtigAY5XK-KaiK-37MurTw4HRyzZ8HcH2qlIjmf0vHrRQn-PX-VKf5uyQDzIJg8nBMeUOujVHgZmMKOAjx5yjt1jca6WukfBP589kiMcCL2AAAAAFg8RCoAA)
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", 7100168038:AAFsblGEFhadkanoAPyB0zv4h-oIkOnMY9c)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5921378472").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", 7876548217)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
