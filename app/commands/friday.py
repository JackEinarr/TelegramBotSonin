from typing import Optional

from aiogram import MagicFilter
from aiogram.filters import Command


class CommandFriday(Command):
    def __init__(
        self,
        deep_link: bool = False,
        deep_link_encoded: bool = False,
        ignore_case: bool = False,
        ignore_mention: bool = False,
        magic: Optional[MagicFilter] = None,
    ):
        super().__init__(
            "friday",
            prefix="*",
            ignore_case=ignore_case,
            ignore_mention=ignore_mention,
            magic=magic,
        )
        self.deep_link = deep_link
        self.deep_link_encoded = deep_link_encoded
