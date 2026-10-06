# hamrpkt

Terminal de packet radio en modo texto, solo teclado, con el mismo aspecto que
[hamrlog](https://github.com/manuel-alcocer/hamrlog): línea de estado arriba,
un marco central, la línea de órdenes y el pie con reloj UTC y contadores.

Se ejecuta en el PC y habla por la red con el nodo que maneja la radio (LinBPQ
en la Raspberry Pi). La radio, el módem o el TNC se quedan en la Pi: cambiar la
Icom por la Kenwood TM-241E, o LinBPQ por Direwolf, no cambia nada aquí
mientras el nodo ofrezca el mismo interfaz.

```
 OP EA7KLX-4 · ENLACE AGWPE wpsd.alcocer.net:8000 · PUERTO 1 · MON ON · SESIÓN EA1ABC
╭ Terminal ─────────────────────────────────────────────────────────────────────╮
│ *** Conectado con EA1ABC                                                      │
│ hola                                                                          │
│ EA1ABC BBS>                                                                   │
╰───────────────────────────────────────────────────────────────────────────────╯
 EA1ABC ▏                                                                       
  Enter envía · /c IND conecta · /d desconecta · ↑↓ histórico · F4 conectar …
 2026-10-06 18:42:10 UTC   RX 1.2k   TX 221   tramas 34   oídas 5   00:03:12
```

## Instalación

```bash
cd ~/Documents/hamrpkt
uv tool install -e .        # deja el comando «hamrpkt» en el PATH
# o, sin instalar:
uv run hamrpkt
```

Al arrancar por primera vez abre los ajustes (F9): indicativo, tipo de enlace,
equipo del nodo y puertos. Se guardan en `~/.config/hamrpkt/config.toml`
(permisos 600, porque puede llevar contraseña). Las opciones de la línea de
órdenes los sustituyen solo para esa ejecución:

```bash
hamrpkt --host wpsd.alcocer.net --link agw --mycall EA7KLX-4
hamrpkt --link telnet --user manuel --password ****
```

## Los dos enlaces

**AGWPE (recomendado, puerto 8000).** Sesiones AX.25 propias con tu
indicativo, monitor de tramas y lista de estaciones oídas. En wpsd lo sirve
**Direwolf**, el módem de la tarjeta de sonido de la radio (canal 1, «first
soundcard mono»). Direwolf, LinBPQ y SoundModem hablan el mismo AGWPE, así
que hamrpkt funciona con cualquiera de ellos. Si algún día se lo pides a
LinBPQ (`AGWPORT=` en `bpq32.cfg`) y rechaza conexiones de otro equipo,
pon en F9 un usuario de los `USER=` del puerto Telnet.

**Telnet.** La consola del nodo (puerto `TCPPORT`, normalmente 8010): entras
como usuario y todo lo que escribes va al nodo (`NODES`, `MHEARD`, `BBS`,
`C 1 EA1ABC`…). `/c` se traduce a la orden `C` del nodo. No hay monitor.

## Las estaciones del propio nodo: `bpq:`

Direwolf no puede conectar con el LinBPQ que cuelga de él mismo, porque la
radio no se oye a sí misma. Para entrar en la BBS, el chat o el nodo se usa la
misma notación que LinPac en la Pi:

```
/c bpq:EA7KLX-1     BBS
/c bpq:EA7KLX-2     chat
/c bpq:EA7KLX-7     nodo
```

hamrpkt abre el Telnet de LinBPQ, se identifica con el usuario de F9 («Usuario
LinBPQ») y escribe la orden que corresponde a ese indicativo, según
`[bpq.apps]` en la configuración. Un indicativo que no esté ahí se alcanza
con `C IND`. Nada sale por radio. Al desconectar (F5 o `/d`), vuelve solo a
Direwolf.

## Teclas

| Tecla | Acción |
|---|---|
| F1 / F2 / F3 | Terminal / Monitor / Estaciones oídas |
| F4 | Conectar (formulario: indicativo, digis, puerto) |
| F5 | Desconectar |
| F6 | Rehacer el enlace con el nodo |
| F9 | Ajustes |
| F10 | Monitor sí/no |
| ↑ ↓ | Histórico de líneas; en F3, mover por la lista |
| Enter | Enviar; en F3 con la línea vacía, conectar con la estación elegida |
| RePág / AvPág | Desplazar la vista |
| Ctrl+L | Limpiar la vista |
| Esc | Vaciar la línea y volver al terminal |
| Ctrl+Q | Salir (pide confirmación si hay sesión) |

## Órdenes

```
/c [puerto] IND [v DIGI …]   conectar
/d                           desconectar
/ui DEST texto               trama UI sin conexión
/port N                      puerto de radio por defecto
/mon                         monitor sí/no
/clear                       limpiar la vista
/reconnect                   rehacer el enlace con el nodo
/quit                        salir
//texto                      enviar una línea que empieza por /
```

Cada sesión queda registrada en `~/.local/share/hamrpkt/sessions/`.

La interfaz sale en español si `LANG` empieza por `es`; `HAMRPKT_LANG=en` la
fuerza en inglés.

## Desarrollo

```bash
uv pip install -e '.[dev]'
.venv/bin/pytest          # incluye una sesión completa contra un nodo AGWPE simulado
.venv/bin/ruff check src tests
```
