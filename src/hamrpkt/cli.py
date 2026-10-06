"""Command line entry point.

Options override the saved settings for this run only; F9 inside the
application changes them for good.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import __version__
from . import config as config_module
from .config import DEFAULT_TCP_PORTS, LINK_TYPES


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hamrpkt",
        description="Keyboard-only packet radio terminal for a remote LinBPQ (AGWPE or Telnet).",
    )
    parser.add_argument("--version", action="version", version=f"hamrpkt {__version__}")
    parser.add_argument("--config", type=Path, metavar="FILE",
                        help=f"settings file (default {config_module.default_config_path()})")
    parser.add_argument("--host", help="machine running the node, e.g. wpsd.alcocer.net")
    parser.add_argument("--port", type=int, help="TCP port (AGWPE 8000, Telnet 8010)")
    parser.add_argument("--link", choices=LINK_TYPES, help="interface of the node to use")
    parser.add_argument("--mycall", help="own callsign, with SSID if any")
    parser.add_argument("--radio-port", type=int, help="radio port of the node, from 1")
    parser.add_argument("--user", help="node user")
    parser.add_argument("--password", help="node password")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    config = config_module.load(args.config)
    link = config.link
    if args.link:
        if args.link != link.type and not args.port:
            link.port = DEFAULT_TCP_PORTS[args.link]
        link.type = args.link
    for name in ("host", "port", "radio_port", "user", "password"):
        value = getattr(args, name)
        if value is not None:
            setattr(link, name, value)
    if args.mycall:
        config.mycall = args.mycall.upper()

    from .tui.app import HamrpktApp

    HamrpktApp(config, args.config).run()
    return 0
