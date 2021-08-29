# -*- coding: utf-8 -*-

"""Constants for the biolookup service."""

import pystow

REFS_TABLE_NAME = "obo_reference"
ALTS_TABLE_NAME = "obo_alt"
DEFS_TABLE_NAME = "obo_def"

MODULE = pystow.module("biolookup")


def get_sqlalchemy_uri() -> str:
    """Get the SQLAlchemy URI."""
    rv = pystow.get_config("biolookup", "sqlalchemy_uri")
    if rv is not None:
        return rv

    # Default value
    return MODULE.joinpath_sqlite(name="biolookup.db")
