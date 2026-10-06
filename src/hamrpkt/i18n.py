"""Minimal translation layer.

Messages are written in English in the code and looked up in a catalog at
display time. Spanish is the only catalog for now; it is picked from the
usual locale variables, or forced with ``HAMRPKT_LANG``.
"""

from __future__ import annotations

import os

#: Listed by /help. Kept here because it doubles as its own catalog key.
HELP_TEXT = (
    "/c [port] CALL [v DIGI …]    connect (also F4)\n"
    "/c bpq:CALL                  enter a station of LinBPQ (bpq:EA7KLX-1 BBS…)\n"
    "/d                           disconnect (also F5)\n"
    "/ui DEST text                send an unconnected UI frame\n"
    "/port N                      default radio port\n"
    "/mon                         monitor on/off (also F10)\n"
    "/clear                       clear the view (also Ctrl+L)\n"
    "/reconnect                   redo the link with the node (also F6)\n"
    "/quit                        quit (also Ctrl+Q)\n"
    "//text                       send a line starting with /"
)

ES: dict[str, str] = {
    # Status line
    "no callsign": "sin indicativo",
    "LINK": "ENLACE",
    "PORT": "PUERTO",
    "SESSION": "SESIÓN",
    "offline": "sin enlace",
    "connecting": "conectando",
    "idle": "en espera",
    "node": "nodo",
    # Frame titles
    "Terminal": "Terminal",
    "Monitor": "Monitor",
    "Heard stations": "Estaciones oídas",
    # Footer
    "frames": "tramas",
    "heard": "oídas",
    "F1 Terminal · F2 Monitor · F3 Heard · Ctrl+Q Quit":
        "F1 Terminal · F2 Monitor · F3 Oídas · Ctrl+Q Salir",
    "F1 Terminal · F2 Monitor · F3 Heard": "F1 Terminal · F2 Monitor · F3 Oídas",
    # Entry
    "CMD": "CMD",
    "Enter sends · /c CALL connects · /d disconnects · ↑↓ history · F4 connect · F5 disconnect · F9 setup · /help":
        "Enter envía · /c IND conecta · /d desconecta · ↑↓ histórico · F4 conectar · F5 desconectar · F9 ajustes · /help",
    "↑↓ choose station · Enter connects · F1 back to the terminal":
        "↑↓ elige estación · Enter conecta · F1 vuelve al terminal",
    "PgUp/PgDn scroll · Ctrl+L clear · F10 monitor on/off · F1 back to the terminal":
        "RePág/AvPág desplaza · Ctrl+L limpia · F10 monitor sí/no · F1 vuelve al terminal",
    # Heard table
    "CALL": "INDICATIVO",
    "LAST HEARD": "ÚLTIMA VEZ",
    "FRAMES": "TRAMAS",
    "TO": "A",
    "VIA": "VÍA",
    # Messages
    "Connecting to {host}:{port} ({kind})…": "Conectando con {host}:{port} ({kind})…",
    "Link up with {host}:{port}": "Enlace establecido con {host}:{port}",
    "Link lost: {error}": "Enlace perdido: {error}",
    "Link closed": "Enlace cerrado",
    "Cannot reach {host}:{port}: {error}": "No puedo llegar a {host}:{port}: {error}",
    "F6 or /reconnect to try again": "F6 o /reconnect para reintentar",
    "Connected to {call}": "Conectado con {call}",
    "Disconnected from {call}": "Desconectado de {call}",
    "Calling {call}…": "Llamando a {call}…",
    "Not connected. Use /c CALL to connect, or /ui DEST text for an unproto frame.":
        "No hay conexión. Usa /c IND para conectar, o /ui DEST texto para una trama sin conexión.",
    "No link. F6 or /reconnect": "No hay enlace. F6 o /reconnect",
    "Already connected to {call}: /d first": "Ya hay conexión con {call}: primero /d",
    "Callsign {call} registered": "Indicativo {call} registrado",
    "The node refused to register {call}": "El nodo no acepta registrar {call}",
    "Radio ports: {ports}": "Puertos de radio: {ports}",
    "AGWPE server version {version}": "Servidor AGWPE versión {version}",
    "Monitor on": "Monitor activado",
    "Monitor off": "Monitor desactivado",
    "The monitor needs an AGWPE link": "El monitor necesita un enlace AGWPE",
    "Port set to {port}": "Puerto fijado en {port}",
    "Unknown command: {cmd}. /help lists them": "Orden desconocida: {cmd}. /help las enumera",
    "Usage: {usage}": "Uso: {usage}",
    "Settings saved": "Ajustes guardados",
    "Set your callsign and the node address with F9": "Configura tu indicativo y la dirección del nodo con F9",
    "Session log: {path}": "Registro de la sesión: {path}",
    "Nothing to disconnect": "No hay nada que desconectar",
    "No station selected": "No hay estación seleccionada",
    "Logging in as {user}": "Entrando como {user}",
    "Commands": "Órdenes",
    HELP_TEXT: (
        "/c [puerto] IND [v DIGI …]   conectar (también F4)\n"
        "/c bpq:IND                   entrar en una estación de LinBPQ (bpq:EA7KLX-1 BBS…)\n"
        "/d                           desconectar (también F5)\n"
        "/ui DEST texto               enviar una trama UI sin conexión\n"
        "/port N                      puerto de radio por defecto\n"
        "/mon                         monitor sí/no (también F10)\n"
        "/clear                       limpiar la vista (también Ctrl+L)\n"
        "/reconnect                   rehacer el enlace con el nodo (también F6)\n"
        "/quit                        salir (también Ctrl+Q)\n"
        "//texto                      enviar una línea que empieza por /"
    ),
    # Dialogs
    "Connect": "Conectar",
    "Callsign": "Indicativo",
    "Via (digipeaters)": "Vía (digipetidores)",
    "Radio port": "Puerto de radio",
    "Setup": "Ajustes",
    "My callsign": "Mi indicativo",
    "Link type": "Tipo de enlace",
    "Node host": "Equipo del nodo",
    "TCP port": "Puerto TCP",
    "User": "Usuario",
    "Password": "Contraseña",
    "Monitor at start": "Monitor al arrancar",
    "agw or telnet": "agw o telnet",
    "yes or no": "sí o no",
    "yes": "sí",
    "no": "no",
    "AGWPE 8000 · Telnet 8010": "AGWPE 8000 · Telnet 8010",
    "Only if the node asks for it": "Solo si el nodo lo pide",
    "Save": "Guardar",
    "LinBPQ Telnet port": "Puerto Telnet LinBPQ",
    "LinBPQ user": "Usuario LinBPQ",
    "LinBPQ password": "Contraseña LinBPQ",
    "for /c bpq:CALL": "para /c bpq:IND",
    "Set the LinBPQ user and password with F9": "Pon el usuario y la contraseña de LinBPQ en F9",
    "Cancel (Esc)": "Cancelar (Esc)",
    "Yes (Y)": "Sí (S)",
    "No (Esc)": "No (Esc)",
    "Tab next field · Enter or Ctrl+S save · Esc cancel":
        "Tab campo siguiente · Enter o Ctrl+S guarda · Esc cancela",
    "←→ choose · Enter confirms · Y yes · N or Esc no":
        "←→ elige · Enter confirma · S sí · N o Esc no",
    "Still connected to {call}. Disconnect and quit?": "Sigues conectado con {call}. ¿Desconectar y salir?",
    "The link type must be agw or telnet": "El tipo de enlace debe ser agw o telnet",
    "The TCP port must be a number": "El puerto TCP debe ser un número",
    "The radio port must be a number from 1": "El puerto de radio debe ser un número desde 1",
    "The callsign is required": "Falta el indicativo",
}


def _pick_catalog() -> dict[str, str]:
    for var in ("HAMRPKT_LANG", "LC_ALL", "LC_MESSAGES", "LANG"):
        value = os.environ.get(var, "")
        if value:
            return ES if value.lower().startswith("es") else {}
    return {}


_CATALOG = _pick_catalog()


def _(message: str) -> str:
    """Translate ``message`` into the user's language when a catalog exists."""
    return _CATALOG.get(message, message)


def tr(message: str, **values: object) -> str:
    """Translate a template, then fill it in, so catalogs see the template."""
    return _(message).format(**values)
