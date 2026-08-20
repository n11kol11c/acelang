from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KeywordInfo:
    name: str
    description: str = ""
    value_type: str = "string"
    default: str = ""
    category: str = ""


class Keywords:
    CVARS: frozenset[str] = frozenset({
        "add_ace",
        "add_principal",
        "block_net_game_event",
        "con_channelFilters",
        "con_addChannelFilter",
        "con_removeChannelFilter",
        "endpoint_add_tcp",
        "endpoint_add_udp",
        "exec",
        "gamename",
        "gametype",
        "increase_pool_size",
        "load_server_icon",
        "mapname",
        "netPort",
        "net_tcpConnLimit",
        "onesync",
        "onesync_enableInfinity",
        "onesync_enableBeyond",
        "onesync_population",
        "onesync_forceMigration",
        "onesync_distanceCulling",
        "onesync_distanceCullVehicles",
        "onesync_radiusFrequency",
        "onesync_migrateDataTimeout",
        "onesync_compressionDictionarySamples",
        "onesync_mapBoundsMinX",
        "onesync_mapBoundsMinY",
        "onesync_mapBoundsMaxX",
        "onesync_mapBoundsMaxY",
        "onesync_mapCellAreaSize",
        "rcon_password",
        "remove_ace",
        "remove_principal",
        "replay_start",
        "replay_stop",
        "set",
        "setr",
        "sets",
        "sv_hostname",
        "sv_maxClients",
        "sv_maxclients",
        "sv_licenseKey",
        "sv_scriptHookAllowed",
        "sv_endpointPrivacy",
        "sv_enforceGameBuild",
        "sv_master1",
        "sv_authMaxVariance",
        "sv_authMinTrust",
        "sv_requestParanoia",
        "sv_filterRequestControl",
        "sv_filterRequestControlSettleTimer",
        "sv_pureLevel",
        "sv_enableNetworkedSounds",
        "sv_enableNetworkedPhoneExplosions",
        "sv_enableNetworkedScriptEntityStates",
        "sv_experimentalStateBagsHandler",
        "sv_experimentalOnesyncPopulation",
        "sv_experimentalNetGameEventHandler",
        "sv_httpFileServerProxyOnly",
        "sv_stateBagStrictMode",
        "sv_entityLockdown",
        "sv_useAccurateSends",
        "sv_enableNetEventReassembly",
        "sv_netEventReassemblyMaxPendingEvents",
        "sv_netEventReassemblyUnlimitedPendingEvents",
        "sv_forceIndirectListing",
        "sv_listingIpOverride",
        "sv_listingHostOverride",
        "sv_registerMulticastDns",
        "sv_endpoints",
        "sv_tcpConnectionTimeoutSeconds",
        "sv_proxyIPRanges",
        "sv_prometheusBasicAuthUser",
        "sv_prometheusBasicAuthPassword",
        "sv_kvsName",
        "sv_lan",
        "svgui",
        "sv_tebexSecret",
        "steam_webApiKey",
        "steam_webApiDomain",
        "sv_ioThreads",
        "sv_clientConnectingTimeoutMilliseconds",
        "sv_clientConnectedTimeoutMilliseconds",
        "sv_pingIntervalMilliseconds",
        "sv_voiceChat",
        "sv_mumble",
        "sv_devMode",
        "sv_scriptDebugDuplicates",
        "sv_enhancedHostSupport",
        "sv_protectServerEntities",
        "sv_projectName",
        "sv_projectDesc",
        "sv_appearAllowlisted",
        "sv_allowlistInstructions",
        "sync_start_recording",
        "sync_stop_recording",
        "test_ace",
        "unblock_net_game_event",
        "rateLimiter_challenge_rate",
        "rateLimiter_challenge_burst",
        "rateLimiter_handshake_rate",
        "rateLimiter_handshake_burst",
        "rateLimiter_handshakeUDP_rate",
        "rateLimiter_handshakeUDP_burst",
        "rateLimiter_http_dynamic_rate",
        "rateLimiter_http_dynamic_burst",
        "rateLimiter_http_info_rate",
        "rateLimiter_http_info_burst",
        "rateLimiter_http_perf_rate",
        "rateLimiter_http_perf_burst",
        "rateLimiter_http_players_rate",
        "rateLimiter_http_players_burst",
        "rateLimiter_netCommand_rate",
        "rateLimiter_netCommand_burst",
        "rateLimiter_netCommandFlood_rate",
        "rateLimiter_netCommandFlood_burst",
        "rateLimiter_netCommandSize_rate",
        "rateLimiter_netCommandSize_burst",
        "rateLimiter_netEvent_rate",
        "rateLimiter_netEvent_burst",
        "rateLimiter_netEventFlood_rate",
        "rateLimiter_netEventFlood_burst",
        "rateLimiter_rcon_rate",
        "rateLimiter_rcon_burst",
        "rateLimiter_res_http_handler_rate",
        "rateLimiter_res_http_handler_burst",
        "rateLimiter_resourceList_rate",
        "rateLimiter_resourceList_burst",
        "rateLimiter_stateBag_rate",
        "rateLimiter_stateBag_burst",
        "rateLimiter_stateBagFlood_rate",
        "rateLimiter_stateBagFlood_burst",
        "rateLimiter_stateBagSize_rate",
        "rateLimiter_stateBagSize_burst",
    })

    ACTIONS: frozenset[str] = frozenset({
        "ensure",
        "ensure_stop",
        "quit",
        "refresh",
        "restart",
        "say",
        "start",
        "stop",
    })

    PRINCIPALS: frozenset[str] = frozenset({
        "builtin.everyone",
        "builtin.restricted",
        "group.admin",
        "group.moderator",
        "group.owner",
        "group.user",
        "group.support",
        "group.helper",
        "group.god",
        "group.superadmin",
        "group.developer",
        "identifier.steam",
        "identifier.license",
        "identifier.discord",
        "identifier.fivem",
        "identifier.ip",
        "identifier.xbl",
        "resource.mapmanager",
        "resource.chat",
        "resource.spawnmanager",
        "resource.sessionmanager",
        "resource.hardcap",
        "resource.rconlog",
        "resource.baseevents",
        "command",
        "command.kick",
        "command.ban",
        "command.tempban",
        "command.setgroup",
        "command.admin",
        "command.noclip",
        "command.tpm",
        "command.bring",
        "command.revive",
        "command.heal",
        "command.announce",
        "command.car",
        "command.weather",
        "command.time",
        "command.quit",
        "command.add_ace",
        "command.add_principal",
        "txAdmin.kick",
        "txAdmin.ban",
        "txAdmin.warn",
        "txAdmin.players.heal",
        "qbcore.admin",
        "qbx.admin",
        "esx.admin",
        "mapmanager",
        "chat",
        "spawnmanager",
        "sessionmanager",
        "basic-gamemode",
        "hardcap",
        "rconlog",
        "baseevents",
    })

    STATES: frozenset[str] = frozenset({
        "allow",
        "deny",
        "deny_socket",
        "true",
        "false",
        "on",
        "off",
    })

    _PREFIXES: dict[str, str] = {
        "sv_": "sv",
        "onesync_": "onesync",
        "rateLimiter_": "ratelimiter",
        "steam_": "steam",
        "group.": "group",
        "builtin.": "builtin",
        "identifier.": "identifier",
        "resource.": "resource",
        "command.": "command",
        "txAdmin.": "txadmin",
    }

    ALL: frozenset[str] = CVARS | ACTIONS | PRINCIPALS | STATES

    META: dict[str, KeywordInfo] = {
        # ── Server Config ──
        "sv_hostname": KeywordInfo("Server Hostname", "Server name displayed in the browser", "string", "Cfx.re Default Server", "server"),
        "sv_maxClients": KeywordInfo("Max Clients", "Maximum number of players", "number", "48", "server"),
        "sv_maxclients": KeywordInfo("Max Clients (alias)", "Maximum number of players (lowercase alias)", "number", "48", "server"),
        "sv_licenseKey": KeywordInfo("License Key", "FiveM license key for authentication", "string", "", "server"),
        "sv_lan": KeywordInfo("LAN Mode", "Enable LAN mode for local play", "boolean", "false", "server"),
        "sv_projectName": KeywordInfo("Project Name", "Name of the project", "string", "", "server"),
        "sv_projectDesc": KeywordInfo("Project Description", "Description of the project", "string", "", "server"),
        "sv_tebexSecret": KeywordInfo("Tebex Secret", "Tebex store integration secret", "string", "", "server"),
        "sv_kvsName": KeywordInfo("KVS Name", "Key-Value Store name", "string", "", "server"),
        "sv_master1": KeywordInfo("Master Server", "Master server URL", "string", "https://master.fivem.net", "server"),
        "sv_endpoints": KeywordInfo("Endpoints", "Server endpoints", "string", "", "server"),
        "sv_registerMulticastDns": KeywordInfo("Register Multicast DNS", "Register with multicast DNS", "boolean", "false", "server"),

        # ── Network ──
        "netPort": KeywordInfo("Net Port", "Network port for the server", "number", "30120", "network"),
        "net_tcpConnLimit": KeywordInfo("TCP Connection Limit", "Maximum TCP connections", "number", "0", "network"),
        "sv_tcpConnectionTimeoutSeconds": KeywordInfo("TCP Timeout", "TCP connection timeout in seconds", "number", "10", "network"),
        "sv_ioThreads": KeywordInfo("IO Threads", "Number of IO threads", "number", "2", "network"),
        "sv_clientConnectingTimeoutMilliseconds": KeywordInfo("Client Connecting Timeout", "Timeout for connecting clients (ms)", "number", "5000", "network"),
        "sv_clientConnectedTimeoutMilliseconds": KeywordInfo("Client Connected Timeout", "Timeout for connected clients (ms)", "number", "0", "network"),
        "sv_pingIntervalMilliseconds": KeywordInfo("Ping Interval", "Client ping interval (ms)", "number", "5000", "network"),
        "sv_endpointPrivacy": KeywordInfo("Endpoint Privacy", "Hide endpoint information", "boolean", "false", "network"),
        "sv_forceIndirectListing": KeywordInfo("Force Indirect Listing", "Force indirect server listing", "boolean", "false", "network"),
        "sv_listingIpOverride": KeywordInfo("Listing IP Override", "Override server listing IP", "string", "", "network"),
        "sv_listingHostOverride": KeywordInfo("Listing Host Override", "Override server listing host", "string", "", "network"),
        "sv_proxyIPRanges": KeywordInfo("Proxy IP Ranges", "Proxy IP address ranges", "string", "", "network"),
        "sv_enhancedHostSupport": KeywordInfo("Enhanced Host Support", "Enable enhanced host support", "boolean", "false", "network"),

        # ── Security ──
        "rcon_password": KeywordInfo("RCON Password", "Remote console password", "string", "", "security"),
        "sv_scriptHookAllowed": KeywordInfo("Script Hook Allowed", "Allow ScriptHookV", "boolean", "false", "security"),
        "sv_protectServerEntities": KeywordInfo("Protect Server Entities", "Protect server entities from client modification", "boolean", "false", "security"),
        "sv_pureLevel": KeywordInfo("Pure Level", "Server purity level (0-2)", "number", "0", "security"),
        "sv_requestParanoia": KeywordInfo("Request Paranoia", "Request paranoia level (0-3)", "number", "0", "security"),
        "sv_authMaxVariance": KeywordInfo("Auth Max Variance", "Maximum authentication variance", "number", "1000", "security"),
        "sv_authMinTrust": KeywordInfo("Auth Min Trust", "Minimum authentication trust level", "number", "0", "security"),
        "sv_filterRequestControl": KeywordInfo("Filter Request Control", "Filter request control level", "number", "0", "security"),
        "sv_filterRequestControlSettleTimer": KeywordInfo("Filter Request Settle Timer", "Filter request control settle timer", "number", "0", "security"),
        "sv_entityLockdown": KeywordInfo("Entity Lockdown", "Entity lockdown mode", "enum", "inactive", "security"),

        # ── OneSync ──
        "onesync": KeywordInfo("OneSync", "Enable OneSync sync mode", "enum", "off", "onesync"),
        "onesync_enableInfinity": KeywordInfo("Enable Infinity", "Enable OneSync Infinity", "boolean", "false", "onesync"),
        "onesync_enableBeyond": KeywordInfo("Enable Beyond", "Enable OneSync Beyond", "boolean", "false", "onesync"),
        "onesync_population": KeywordInfo("Population", "Enable OneSync population management", "boolean", "false", "onesync"),
        "onesync_forceMigration": KeywordInfo("Force Migration", "Force entity migration between slots", "boolean", "false", "onesync"),
        "onesync_distanceCulling": KeywordInfo("Distance Culling", "Enable distance-based entity culling", "boolean", "false", "onesync"),
        "onesync_distanceCullVehicles": KeywordInfo("Distance Cull Vehicles", "Enable distance culling for vehicles", "boolean", "false", "onesync"),
        "onesync_radiusFrequency": KeywordInfo("Radius Frequency", "Entity update radius frequency", "boolean", "false", "onesync"),
        "onesync_migrateDataTimeout": KeywordInfo("Migrate Data Timeout", "Entity migration data timeout", "number", "5000", "onesync"),
        "onesync_compressionDictionarySamples": KeywordInfo("Compression Dictionary Samples", "Compression dictionary sample count", "number", "256", "onesync"),
        "onesync_mapBoundsMinX": KeywordInfo("Map Bounds Min X", "Minimum X map boundary", "number", "-4000", "onesync"),
        "onesync_mapBoundsMinY": KeywordInfo("Map Bounds Min Y", "Minimum Y map boundary", "number", "-4000", "onesync"),
        "onesync_mapBoundsMaxX": KeywordInfo("Map Bounds Max X", "Maximum X map boundary", "number", "8000", "onesync"),
        "onesync_mapBoundsMaxY": KeywordInfo("Map Bounds Max Y", "Maximum Y map boundary", "number", "8000", "onesync"),
        "onesync_mapCellAreaSize": KeywordInfo("Map Cell Area Size", "Size of map cells for OneSync", "number", "100", "onesync"),

        # ── Features ──
        "sv_enableNetworkedSounds": KeywordInfo("Enable Networked Sounds", "Allow networked sound playback", "boolean", "false", "features"),
        "sv_enableNetworkedPhoneExplosions": KeywordInfo("Enable Networked Phone Explosions", "Allow networked phone explosions", "boolean", "false", "features"),
        "sv_enableNetworkedScriptEntityStates": KeywordInfo("Enable Script Entity States", "Allow networked script entity states", "boolean", "false", "features"),
        "sv_enableNetEventReassembly": KeywordInfo("Enable Net Event Reassembly", "Enable network event reassembly", "boolean", "false", "features"),
        "sv_netEventReassemblyMaxPendingEvents": KeywordInfo("Max Pending Events", "Maximum pending net events", "number", "128", "features"),
        "sv_netEventReassemblyUnlimitedPendingEvents": KeywordInfo("Unlimited Pending Events", "Allow unlimited pending net events", "boolean", "false", "features"),
        "sv_useAccurateSends": KeywordInfo("Use Accurate Sends", "Use accurate network sends", "boolean", "false", "features"),
        "sv_voiceChat": KeywordInfo("Voice Chat", "Enable built-in voice chat", "boolean", "false", "features"),
        "sv_mumble": KeywordInfo("Mumble", "Enable Mumble voice integration", "boolean", "false", "features"),
        "sv_devMode": KeywordInfo("Developer Mode", "Enable developer mode", "boolean", "false", "features"),
        "sv_scriptDebugDuplicates": KeywordInfo("Script Debug Duplicates", "Debug duplicate script events", "boolean", "false", "features"),
        "svgui": KeywordInfo("SVG UI", "Enable SVG-based UI", "boolean", "false", "features"),

        # ── Experimental ──
        "sv_experimentalStateBagsHandler": KeywordInfo("Experimental State Bags", "Use experimental state bags handler", "boolean", "false", "experimental"),
        "sv_experimentalOnesyncPopulation": KeywordInfo("Experimental OneSync Population", "Use experimental OneSync population", "boolean", "false", "experimental"),
        "sv_experimentalNetGameEventHandler": KeywordInfo("Experimental Net Game Event", "Use experimental net game event handler", "boolean", "false", "experimental"),
        "sv_stateBagStrictMode": KeywordInfo("State Bag Strict Mode", "Enable strict state bag mode", "boolean", "false", "experimental"),
        "sv_httpFileServerProxyOnly": KeywordInfo("HTTP File Server Proxy", "HTTP file server proxy mode only", "boolean", "false", "experimental"),

        # ── Auth ──
        "sv_appearAllowlisted": KeywordInfo("Appear Allowlisted", "Show as allowlisted in server browser", "boolean", "false", "auth"),
        "sv_allowlistInstructions": KeywordInfo("Allowlist Instructions", "Instructions for allowlisted players", "string", "", "auth"),

        # ── Debug / Monitoring ──
        "sv_prometheusBasicAuthUser": KeywordInfo("Prometheus Auth User", "Prometheus monitoring basic auth user", "string", "", "monitoring"),
        "sv_prometheusBasicAuthPassword": KeywordInfo("Prometheus Auth Password", "Prometheus monitoring basic auth password", "string", "", "monitoring"),

        # ── Misc ──
        "gamename": KeywordInfo("Game Name", "Game name identifier", "string", "gta5", "misc"),
        "gametype": KeywordInfo("Game Type", "Game type identifier", "string", "gta5", "misc"),
        "mapname": KeywordInfo("Map Name", "Current map name", "string", "gta5", "misc"),
        "load_server_icon": KeywordInfo("Load Server Icon", "Load a server icon file", "string", "", "misc"),
        "exec": KeywordInfo("Execute", "Execute a configuration file", "string", "", "misc"),
        "increase_pool_size": KeywordInfo("Increase Pool Size", "Increase pool size", "string", "", "misc"),

        # ── Actions ──
        "ensure": KeywordInfo("Ensure", "Start a resource and ensure it stays running", "", "", "action"),
        "ensure_stop": KeywordInfo("Ensure Stop", "Stop an ensured resource", "", "", "action"),
        "quit": KeywordInfo("Quit", "Stop the server", "", "", "action"),
        "refresh": KeywordInfo("Refresh", "Refresh server resources", "", "", "action"),
        "restart": KeywordInfo("Restart", "Restart the server", "", "", "action"),
        "say": KeywordInfo("Say", "Send a server message", "", "", "action"),
        "start": KeywordInfo("Start", "Start a resource", "", "", "action"),
        "stop": KeywordInfo("Stop", "Stop a resource", "", "", "action"),

        # ── Commands ──
        "set": KeywordInfo("Set", "Set a convar (not replicated)", "", "", "command"),
        "setr": KeywordInfo("Set Replicated", "Set a replicated convar", "", "", "command"),
        "sets": KeywordInfo("Set Saved", "Set a saved convar", "", "", "command"),
        "add_ace": KeywordInfo("Add ACE", "Add an ACE permission", "", "", "command"),
        "add_principal": KeywordInfo("Add Principal", "Add a principal to another principal", "", "", "command"),
        "remove_ace": KeywordInfo("Remove ACE", "Remove an ACE permission", "", "", "command"),
        "remove_principal": KeywordInfo("Remove Principal", "Remove a principal from another principal", "", "", "command"),
        "block_net_game_event": KeywordInfo("Block Net Game Event", "Block a network game event", "", "", "command"),
        "unblock_net_game_event": KeywordInfo("Unblock Net Game Event", "Unblock a network game event", "", "", "command"),
        "test_ace": KeywordInfo("Test ACE", "Test an ACE permission", "", "", "command"),
        "replay_start": KeywordInfo("Replay Start", "Start recording a replay", "", "", "command"),
        "replay_stop": KeywordInfo("Replay Stop", "Stop recording a replay", "", "", "command"),
        "sync_start_recording": KeywordInfo("Sync Start Recording", "Start synced recording", "", "", "command"),
        "sync_stop_recording": KeywordInfo("Sync Stop Recording", "Stop synced recording", "", "", "command"),
        "con_channelFilters": KeywordInfo("Channel Filters", "Set console channel filters", "", "", "command"),
        "con_addChannelFilter": KeywordInfo("Add Channel Filter", "Add a console channel filter", "", "", "command"),
        "con_removeChannelFilter": KeywordInfo("Remove Channel Filter", "Remove a console channel filter", "", "", "command"),
        "endpoint_add_tcp": KeywordInfo("Add TCP Endpoint", "Add a TCP endpoint", "", "", "command"),
        "endpoint_add_udp": KeywordInfo("Add UDP Endpoint", "Add a UDP endpoint", "", "", "command"),
    }


def get_identifier(identifier: str | None, /) -> str | None:
    return str(identifier) if identifier else None


def is_valid_keyword(token: str, /) -> bool:
    return token in Keywords.ALL


def is_valid_cvar(token: str, /) -> bool:
    return token in Keywords.CVARS


def is_valid_action(token: str, /) -> bool:
    return token in Keywords.ACTIONS


def is_valid_principal(token: str, /) -> bool:
    return token in Keywords.PRINCIPALS


def is_valid_state(token: str, /) -> bool:
    return token in Keywords.STATES


def get_token_type(token: str, /) -> str | None:
    if token in Keywords.CVARS:
        return "cvar"
    if token in Keywords.ACTIONS:
        return "action"
    if token in Keywords.PRINCIPALS:
        return "principal"
    if token in Keywords.STATES:
        return "state"
    return None


def get_token_prefix(token: str, /) -> str | None:
    for prefix, name in Keywords._PREFIXES.items():
        if token.startswith(prefix):
            return name
    return None


def get_keyword_info(token: str, /) -> KeywordInfo | None:
    return Keywords.META.get(token)


def get_keyword_name(token: str, /) -> str:
    info = Keywords.META.get(token)
    return info.name if info else token


def get_keyword_desc(token: str, /) -> str:
    info = Keywords.META.get(token)
    return info.description if info else ""


def get_keyword_type(token: str, /) -> str:
    info = Keywords.META.get(token)
    return info.value_type if info else "string"


def get_keyword_default(token: str, /) -> str:
    info = Keywords.META.get(token)
    return info.default if info else ""


def get_keyword_category(token: str, /) -> str:
    info = Keywords.META.get(token)
    return info.category if info else ""


def find_by_category(category: str, /) -> frozenset[str]:
    return frozenset(k for k, v in Keywords.META.items() if v.category == category)


def find_by_value_type(value_type: str, /) -> frozenset[str]:
    return frozenset(k for k, v in Keywords.META.items() if v.value_type == value_type)


def find_by_name(name: str, /) -> list[str]:
    lower = name.lower()
    return sorted(k for k, v in Keywords.META.items() if lower in v.name.lower())


def search_keywords(query: str, /) -> list[str]:
    lower = query.lower()
    return sorted(k for k, v in Keywords.META.items()
                  if lower in k.lower() or lower in v.name.lower() or lower in v.description.lower())


def get_all_categories() -> frozenset[str]:
    return frozenset(v.category for v in Keywords.META.values() if v.category)


def get_category_stats() -> dict[str, int]:
    stats: dict[str, int] = {}
    for info in Keywords.META.values():
        if info.category:
            stats[info.category] = stats.get(info.category, 0) + 1
    return dict(sorted(stats.items()))


def get_value_type_stats() -> dict[str, int]:
    stats: dict[str, int] = {}
    for info in Keywords.META.values():
        stats[info.value_type] = stats.get(info.value_type, 0) + 1
    return dict(sorted(stats.items()))


def resolve_identifier_type(identifier: str, /) -> str | None:
    prefix = identifier.split(".")[0] if "." in identifier else None
    if prefix == "identifier":
        parts = identifier.split(":", 1)
        if len(parts) == 2:
            return parts[0].split(".")[-1]
    return prefix


def split_identifier(identifier: str, /) -> tuple[str, str] | None:
    if ":" in identifier:
        parts = identifier.split(":", 1)
        return (parts[0], parts[1])
    return None


def format_identifier(prefix: str, sep: str, value: str, /) -> str:
    return f"{prefix}{sep}{value}"


def get_sv_convars() -> frozenset[str]:
    return frozenset(c for c in Keywords.CVARS if c.startswith("sv_"))


def get_onesync_convars() -> frozenset[str]:
    return frozenset(c for c in Keywords.CVARS if c.startswith("onesync_"))


def get_ratelimiter_convars() -> frozenset[str]:
    return frozenset(c for c in Keywords.CVARS if c.startswith("rateLimiter_"))


def get_ratelimiter_pairs() -> list[tuple[str, str]]:
    pairs = []
    for cvar in Keywords.CVARS:
        if cvar.startswith("rateLimiter_") and cvar.endswith("_rate"):
            burst = cvar.replace("_rate", "_burst")
            if burst in Keywords.CVARS:
                pairs.append((cvar, burst))
    return sorted(pairs)


def get_group_principals() -> frozenset[str]:
    return frozenset(p for p in Keywords.PRINCIPALS if p.startswith("group."))


def get_identifier_principals() -> frozenset[str]:
    return frozenset(p for p in Keywords.PRINCIPALS if p.startswith("identifier."))


def get_resource_principals() -> frozenset[str]:
    return frozenset(p for p in Keywords.PRINCIPALS if p.startswith("resource.") or p in {
        "mapmanager", "chat", "spawnmanager", "sessionmanager",
        "basic-gamemode", "hardcap", "rconlog", "baseevents",
    })


def get_command_permissions() -> frozenset[str]:
    return frozenset(p for p in Keywords.PRINCIPALS if p.startswith("command."))


def get_txadmin_permissions() -> frozenset[str]:
    return frozenset(p for p in Keywords.PRINCIPALS if p.startswith("txAdmin."))


def get_framework_permissions() -> frozenset[str]:
    return frozenset(p for p in Keywords.PRINCIPALS if p.startswith(("qbcore.", "qbx.", "esx.")))


def validate_convar_value(cvar: str, value: str, /) -> bool:
    validators: dict[str, frozenset[str]] = {
        "sv_entityLockdown": frozenset({"full", "strict", "relaxed", "inactive"}),
        "sv_pureLevel": frozenset({"0", "1", "2"}),
        "sv_requestParanoia": frozenset({"0", "1", "2", "3"}),
        "onesync": frozenset({"on", "off", "legacy"}),
    }
    allowed = validators.get(cvar)
    if allowed is not None:
        return value in allowed
    if cvar == "sv_enforceGameBuild":
        return value.isdigit()
    return True


def get_keyword_suggestions(prefix: str, /) -> list[str]:
    keywords = sorted(Keywords.ALL)
    if not prefix:
        return keywords
    return [k for k in keywords if k.startswith(prefix)]


def parse_line(line: str, /) -> tuple[str, list[str]]:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return ("", [])
    parts = stripped.split()
    return (parts[0], parts[1:]) if parts else ("", [])


def build_line(cmd: str, *args: str) -> str:
    return " ".join([cmd, *args])


def parse_value(raw: str, /) -> str:
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        return raw[1:-1]
    return raw


def format_value(value: str, /) -> str:
    if " " in value or "\t" in value:
        return f'"{value}"'
    return value


def find_by_prefix(prefix: str, /) -> frozenset[str]:
    return frozenset(k for k in Keywords.ALL if k.startswith(prefix))


def find_by_suffix(suffix: str, /) -> frozenset[str]:
    return frozenset(k for k in Keywords.ALL if k.endswith(suffix))


def find_by_pattern(pattern: str, /) -> list[str]:
    return sorted(k for k in Keywords.ALL if pattern in k)


def get_related(token: str, /) -> frozenset[str]:
    prefix = get_token_prefix(token)
    if prefix:
        return frozenset(k for k in Keywords.ALL if k.startswith(prefix + "_") or k.startswith(prefix + "."))
    if "." in token:
        base = token.split(".")[0]
        return frozenset(k for k in Keywords.ALL if k.startswith(base + "."))
    return frozenset()


def get_rate_pair(cvar: str, /) -> tuple[str, str] | None:
    if cvar.endswith("_rate"):
        burst = cvar.replace("_rate", "_burst")
        if burst in Keywords.CVARS:
            return (cvar, burst)
    if cvar.endswith("_burst"):
        rate = cvar.replace("_burst", "_rate")
        if rate in Keywords.CVARS:
            return (rate, cvar)
    return None


def get_enabled_only() -> frozenset[str]:
    return frozenset(k for k in Keywords.CVARS if k in {
        "sv_lan", "sv_voiceChat", "sv_devMode", "sv_mumble",
        "sv_endpointPrivacy", "sv_useAccurateSends", "sv_registerMulticastDns",
        "sv_enableNetworkedSounds", "sv_enableNetworkedPhoneExplosions",
        "sv_enableNetworkedScriptEntityStates", "sv_enableNetEventReassembly",
        "sv_netEventReassemblyUnlimitedPendingEvents", "sv_forceIndirectListing",
        "sv_httpFileServerProxyOnly", "sv_stateBagStrictMode",
        "sv_scriptHookAllowed", "sv_scriptDebugDuplicates",
        "onesync_enableInfinity", "onesync_population", "onesync_forceMigration",
        "onesync_distanceCulling", "onesync_distanceCullVehicles", "onesync_radiusFrequency",
        "onesync_compressionDictionarySamples", "sv_prometheusBasicAuthUser",
    })


def get_numeric_only() -> frozenset[str]:
    return frozenset(k for k in Keywords.CVARS if k in {
        "sv_maxClients", "sv_maxclients", "sv_enforceGameBuild", "sv_pureLevel",
        "sv_requestParanoia", "sv_filterRequestControl", "sv_filterRequestControlSettleTimer",
        "sv_authMaxVariance", "sv_authMinTrust", "netPort", "net_tcpConnLimit",
        "sv_tcpConnectionTimeoutSeconds", "sv_ioThreads",
        "sv_clientConnectingTimeoutMilliseconds", "sv_clientConnectedTimeoutMilliseconds",
        "sv_pingIntervalMilliseconds", "sv_netEventReassemblyMaxPendingEvents",
        "onesync_migrateDataTimeout", "onesync_mapBoundsMinX", "onesync_mapBoundsMinY",
        "onesync_mapBoundsMaxX", "onesync_mapBoundsMaxY", "onesync_mapCellAreaSize",
    })


def get_string_only() -> frozenset[str]:
    return frozenset(k for k in Keywords.CVARS if k in {
        "sv_hostname", "sv_licenseKey", "sv_master1", "sv_tebexSecret",
        "steam_webApiKey", "steam_webApiDomain", "sv_listingIpOverride",
        "sv_listingHostOverride", "sv_endpoints", "sv_proxyIPRanges",
        "sv_kvsName", "sv_prometheusBasicAuthPassword", "sv_projectName",
        "sv_projectDesc", "sv_allowlistInstructions", "rcon_password",
        "gametype", "gamename", "mapname", "load_server_icon",
    })


def get_ace_args(principal: str, object_name: str, perm: str, /) -> list[str]:
    return [principal, object_name, perm]


def get_principal_args(child: str, parent: str, /) -> list[str]:
    return [child, parent]


def build_ace_line(principal: str, object_name: str, perm: str, /) -> str:
    return build_line("add_ace", principal, object_name, perm)


def build_principal_line(child: str, parent: str, /) -> str:
    return build_line("add_principal", child, parent)


def build_resource_line(action: str, resource: str, /) -> str:
    return build_line(action, resource)


def build_convar_line(mode: str, name: str, value: str, /) -> str:
    return build_line(mode, name, format_value(value))


def build_set_line(name: str, value: str, /) -> str:
    return build_convar_line("set", name, value)


def build_setr_line(name: str, value: str, /) -> str:
    return build_convar_line("setr", name, value)


def build_sets_line(name: str, value: str, /) -> str:
    return build_convar_line("sets", name, value)


def get_all_lines() -> list[str]:
    lines = []
    for cvar in sorted(Keywords.CVARS):
        lines.append(f"# {cvar}")
    return lines


def get_stats() -> dict[str, int]:
    return {
        "cvars": len(Keywords.CVARS),
        "actions": len(Keywords.ACTIONS),
        "principals": len(Keywords.PRINCIPALS),
        "states": len(Keywords.STATES),
        "total": len(Keywords.ALL),
        "sv_convars": len(get_sv_convars()),
        "onesync_convars": len(get_onesync_convars()),
        "ratelimiter_convars": len(get_ratelimiter_convars()),
        "groups": len(get_group_principals()),
        "identifiers": len(get_identifier_principals()),
        "resources": len(get_resource_principals()),
        "commands": len(get_command_permissions()),
        "txadmin": len(get_txadmin_permissions()),
        "frameworks": len(get_framework_permissions()),
    }

