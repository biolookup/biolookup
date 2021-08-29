# -*- coding: utf-8 -*-

"""CLI for the Biolookup Service database loader.

Run with ``biolookup load``.
"""

import click
from more_click import verbose_option
from pyobo.resource_utils import ensure_alts, ensure_definitions, ensure_ooh_na_na

from ..constants import ALTS_TABLE_NAME, DEFS_TABLE_NAME, REFS_TABLE_NAME, get_sqlalchemy_uri

__all__ = [
    "load",
]


@click.command()
@click.option("--uri", default=get_sqlalchemy_uri, help="The database URL.", show_default=True)
@click.option("--refs-table", default=REFS_TABLE_NAME, show_default=True)
@click.option(
    "--refs-path", default=ensure_ooh_na_na, show_default=True, help="By default, load from Zenodo"
)
@click.option("--alts-table", default=ALTS_TABLE_NAME, show_default=True)
@click.option(
    "--alts-path", default=ensure_alts, show_default=True, help="By default, load from Zenodo"
)
@click.option("--defs-table", default=DEFS_TABLE_NAME, show_default=True)
@click.option(
    "--defs-path",
    default=ensure_definitions,
    show_default=True,
    help="By default, load from Zenodo",
)
@click.option("--test", is_flag=True, help="Test run with a small test subset")
@verbose_option
def load(
    uri: str,
    refs_table: str,
    refs_path: str,
    alts_table: str,
    alts_path: str,
    defs_table: str,
    defs_path: str,
    test: bool,
):
    """Load the SQL database."""
    from .loader import load as _load

    _load(
        uri=uri,
        refs_table=refs_table,
        refs_path=refs_path,
        alts_table=alts_table,
        alts_path=alts_path,
        defs_table=defs_table,
        defs_path=defs_path,
        test=test,
    )


if __name__ == "__main__":
    load()
