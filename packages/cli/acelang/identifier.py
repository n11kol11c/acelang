from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ParamInfo:
    name: str
    type: str = "str"
    required: bool = True
    default: str = ""
    description: str = ""


@dataclass(frozen=True, slots=True)
class KeywordInfo:
    name: str
    description: str = ""
    value_type: str = "string"
    default: str = ""
    category: str = ""
    params: tuple[ParamInfo, ...] = ()
    valid_values: tuple[str, ...] = ()
    min_value: str = ""
    max_value: str = ""
    min_length: int = 0
    max_length: int = 0
    usage: str = ""
    related: tuple[str, ...] = ()
    aliases: tuple[str, ...] = ()
    since: str = ""


class Keywords:
    CVARS: frozenset[str] = frozenset({
        "add_ace", "add_principal", "block_net_game_event",
        "con_channelFilters", "con_addChannelFilter", "con_removeChannelFilter",
        "endpoint_add_tcp", "endpoint_add_udp", "exec", "gamename", "gametype",
        "increase_pool_size", "load_server_icon", "mapname", "netPort",
        "net_tcpConnLimit", "onesync", "onesync_enableInfinity", "onesync_enableBeyond",
        "onesync_population", "onesync_forceMigration", "onesync_distanceCulling",
        "onesync_distanceCullVehicles", "onesync_radiusFrequency",
        "onesync_migrateDataTimeout", "onesync_compressionDictionarySamples",
        "onesync_mapBoundsMinX", "onesync_mapBoundsMinY", "onesync_mapBoundsMaxX",
        "onesync_mapBoundsMaxY", "onesync_mapCellAreaSize", "rcon_password",
        "remove_ace", "remove_principal", "replay_start", "replay_stop",
        "set", "setr", "sets", "sv_hostname", "sv_maxClients", "sv_maxclients",
        "sv_licenseKey", "sv_scriptHookAllowed", "sv_endpointPrivacy",
        "sv_enforceGameBuild", "sv_master1", "sv_authMaxVariance", "sv_authMinTrust",
        "sv_requestParanoia", "sv_filterRequestControl",
        "sv_filterRequestControlSettleTimer", "sv_pureLevel",
        "sv_enableNetworkedSounds", "sv_enableNetworkedPhoneExplosions",
        "sv_enableNetworkedScriptEntityStates", "sv_experimentalStateBagsHandler",
        "sv_experimentalOnesyncPopulation", "sv_experimentalNetGameEventHandler",
        "sv_httpFileServerProxyOnly", "sv_stateBagStrictMode", "sv_entityLockdown",
        "sv_useAccurateSends", "sv_enableNetEventReassembly",
        "sv_netEventReassemblyMaxPendingEvents",
        "sv_netEventReassemblyUnlimitedPendingEvents", "sv_forceIndirectListing",
        "sv_listingIpOverride", "sv_listingHostOverride", "sv_registerMulticastDns",
        "sv_endpoints", "sv_tcpConnectionTimeoutSeconds", "sv_proxyIPRanges",
        "sv_prometheusBasicAuthUser", "sv_prometheusBasicAuthPassword", "sv_kvsName",
        "sv_lan", "svgui", "sv_tebexSecret", "steam_webApiKey", "steam_webApiDomain",
        "sv_ioThreads", "sv_clientConnectingTimeoutMilliseconds",
        "sv_clientConnectedTimeoutMilliseconds", "sv_pingIntervalMilliseconds",
        "sv_voiceChat", "sv_mumble", "sv_devMode", "sv_scriptDebugDuplicates",
        "sv_enhancedHostSupport", "sv_protectServerEntities", "sv_projectName",
        "sv_projectDesc", "sv_appearAllowlisted", "sv_allowlistInstructions",
        "sync_start_recording", "sync_stop_recording", "test_ace",
        "unblock_net_game_event",
        "rateLimiter_challenge_rate", "rateLimiter_challenge_burst",
        "rateLimiter_handshake_rate", "rateLimiter_handshake_burst",
        "rateLimiter_handshakeUDP_rate", "rateLimiter_handshakeUDP_burst",
        "rateLimiter_http_dynamic_rate", "rateLimiter_http_dynamic_burst",
        "rateLimiter_http_info_rate", "rateLimiter_http_info_burst",
        "rateLimiter_http_perf_rate", "rateLimiter_http_perf_burst",
        "rateLimiter_http_players_rate", "rateLimiter_http_players_burst",
        "rateLimiter_netCommand_rate", "rateLimiter_netCommand_burst",
        "rateLimiter_netCommandFlood_rate", "rateLimiter_netCommandFlood_burst",
        "rateLimiter_netCommandSize_rate", "rateLimiter_netCommandSize_burst",
        "rateLimiter_netEvent_rate", "rateLimiter_netEvent_burst",
        "rateLimiter_netEventFlood_rate", "rateLimiter_netEventFlood_burst",
        "rateLimiter_rcon_rate", "rateLimiter_rcon_burst",
        "rateLimiter_res_http_handler_rate", "rateLimiter_res_http_handler_burst",
        "rateLimiter_resourceList_rate", "rateLimiter_resourceList_burst",
        "rateLimiter_stateBag_rate", "rateLimiter_stateBag_burst",
        "rateLimiter_stateBagFlood_rate", "rateLimiter_stateBagFlood_burst",
        "rateLimiter_stateBagSize_rate", "rateLimiter_stateBagSize_burst",
    })

    ACTIONS: frozenset[str] = frozenset({
        "ensure", "ensure_stop", "quit", "refresh", "restart", "say", "start", "stop",
    })

    PRINCIPALS: frozenset[str] = frozenset({
        "builtin.everyone", "builtin.restricted",
        "group.admin", "group.moderator", "group.owner", "group.user",
        "group.support", "group.helper", "group.god", "group.superadmin", "group.developer",
        "identifier.steam", "identifier.license", "identifier.discord",
        "identifier.fivem", "identifier.ip", "identifier.xbl",
        "resource.mapmanager", "resource.chat", "resource.spawnmanager",
        "resource.sessionmanager", "resource.hardcap", "resource.rconlog", "resource.baseevents",
        "command", "command.kick", "command.ban", "command.tempban", "command.setgroup",
        "command.admin", "command.noclip", "command.tpm", "command.bring",
        "command.revive", "command.heal", "command.announce", "command.car",
        "command.weather", "command.time", "command.quit",
        "command.add_ace", "command.add_principal",
        "txAdmin.kick", "txAdmin.ban", "txAdmin.warn", "txAdmin.players.heal",
        "qbcore.admin", "qbx.admin", "esx.admin",
        "mapmanager", "chat", "spawnmanager", "sessionmanager",
        "basic-gamemode", "hardcap", "rconlog", "baseevents",
    })

    STATES: frozenset[str] = frozenset({
        "allow", "deny", "deny_socket", "true", "false", "on", "off",
    })

    _PREFIXES: dict[str, str] = {
        "sv_": "sv", "onesync_": "onesync", "rateLimiter_": "ratelimiter",
        "steam_": "steam", "group.": "group", "builtin.": "builtin",
        "identifier.": "identifier", "resource.": "resource",
        "command.": "command", "txAdmin.": "txadmin",
    }

    ALL: frozenset[str] = CVARS | ACTIONS | PRINCIPALS | STATES

    META: dict[str, KeywordInfo] = {
        "sv_hostname": KeywordInfo("Server Hostname", "Server name displayed in the browser", "string", "Cfx.re Default Server", "server", max_length=128, usage='set sv_hostname "My Server"', related=("sv_projectName",)),
        "sv_maxClients": KeywordInfo("Max Clients", "Maximum players allowed", "number", "48", "server", min_value="1", max_value="1024", usage="set sv_maxClients 64", related=("sv_maxclients",)),
        "sv_maxclients": KeywordInfo("Max Clients (lowercase)", "Maximum players (alias)", "number", "48", "server", min_value="1", max_value="1024", usage="set sv_maxclients 64", aliases=("sv_maxClients",)),
        "sv_licenseKey": KeywordInfo("License Key", "FiveM license key", "string", "", "server", min_length=1, usage="set sv_licenseKey YOUR_KEY"),
        "sv_lan": KeywordInfo("LAN Mode", "Enable LAN mode", "boolean", "false", "server", valid_values=("true", "false"), usage="set sv_lan true"),
        "sv_projectName": KeywordInfo("Project Name", "Project name for txAdmin", "string", "", "server", max_length=64, usage='set sv_projectName "My Project"'),
        "sv_projectDesc": KeywordInfo("Project Description", "Project description for txAdmin", "string", "", "server", max_length=256, usage='set sv_projectDesc "Cool server"'),
        "sv_tebexSecret": KeywordInfo("Tebex Secret", "Tebex store secret key", "string", "", "server", usage="set sv_tebexSecret YOUR_SECRET"),
        "sv_kvsName": KeywordInfo("KVS Name", "Key-Value Store name", "string", "", "server", usage="set sv_kvsName my-server"),
        "sv_master1": KeywordInfo("Master Server", "Master server URL", "string", "https://master.fivem.net", "server", usage="set sv_master1 https://master.fivem.net"),
        "sv_endpoints": KeywordInfo("Endpoints", "Server endpoints", "string", "", "server", usage="set sv_endpoints endpoint_add_tcp 0.0.0.0:30120"),
        "sv_registerMulticastDns": KeywordInfo("Multicast DNS", "Register with multicast DNS", "boolean", "false", "server", valid_values=("true", "false"), usage="set sv_registerMulticastDns true"),
        "sv_appearAllowlisted": KeywordInfo("Appear Allowlisted", "Show as allowlisted", "boolean", "false", "server", valid_values=("true", "false"), usage="set sv_appearAllowlisted true"),
        "sv_allowlistInstructions": KeywordInfo("Allowlist Instructions", "Instructions for non-allowlisted players", "string", "", "server", usage='set sv_allowlistInstructions "Contact admin"'),
        "sv_enforceGameBuild": KeywordInfo("Enforce Game Build", "Force GTA V build number", "number", "0", "server", min_value="0", max_value="9999", usage="set sv_enforceGameBuild 2802"),
        "netPort": KeywordInfo("Network Port", "Server listening port", "number", "30120", "network", min_value="1", max_value="65535", usage="set netPort 30120"),
        "net_tcpConnLimit": KeywordInfo("TCP Connection Limit", "Max TCP connections (0=unlimited)", "number", "0", "network", min_value="0", max_value="65535", usage="set net_tcpConnLimit 0"),
        "sv_tcpConnectionTimeoutSeconds": KeywordInfo("TCP Timeout", "TCP connection timeout (seconds)", "number", "10", "network", min_value="1", max_value="300", usage="set sv_tcpConnectionTimeoutSeconds 10"),
        "sv_ioThreads": KeywordInfo("IO Threads", "Number of IO threads", "number", "2", "network", min_value="1", max_value="16", usage="set sv_ioThreads 2"),
        "sv_clientConnectingTimeoutMilliseconds": KeywordInfo("Client Connecting Timeout", "Timeout for connecting clients (ms)", "number", "5000", "network", min_value="1000", max_value="60000", usage="set sv_clientConnectingTimeoutMilliseconds 5000"),
        "sv_clientConnectedTimeoutMilliseconds": KeywordInfo("Client Connected Timeout", "Timeout for connected clients (ms, 0=off)", "number", "0", "network", min_value="0", max_value="60000", usage="set sv_clientConnectedTimeoutMilliseconds 0"),
        "sv_pingIntervalMilliseconds": KeywordInfo("Ping Interval", "Client ping interval (ms)", "number", "5000", "network", min_value="1000", max_value="30000", usage="set sv_pingIntervalMilliseconds 5000"),
        "sv_endpointPrivacy": KeywordInfo("Endpoint Privacy", "Hide endpoint information", "boolean", "false", "network", valid_values=("true", "false"), usage="set sv_endpointPrivacy true"),
        "sv_forceIndirectListing": KeywordInfo("Force Indirect Listing", "Force indirect server listing", "boolean", "false", "network", valid_values=("true", "false"), usage="set sv_forceIndirectListing true"),
        "sv_listingIpOverride": KeywordInfo("Listing IP Override", "Override listing IP", "string", "", "network", usage="set sv_listingIpOverride 1.2.3.4"),
        "sv_listingHostOverride": KeywordInfo("Listing Host Override", "Override listing host", "string", "", "network", usage="set sv_listingHostOverride my.server.com"),
        "sv_proxyIPRanges": KeywordInfo("Proxy IP Ranges", "Proxy IP ranges (comma-separated)", "string", "", "network", usage='set sv_proxyIPRanges "10.0.0.0/8"'),
        "sv_enhancedHostSupport": KeywordInfo("Enhanced Host Support", "Enable enhanced hosting", "boolean", "false", "network", valid_values=("true", "false"), usage="set sv_enhancedHostSupport true"),
        "rcon_password": KeywordInfo("RCON Password", "Remote console password", "string", "", "security", min_length=1, usage="set rcon_password mypass"),
        "sv_scriptHookAllowed": KeywordInfo("Script Hook Allowed", "Allow ScriptHookV", "boolean", "false", "security", valid_values=("true", "false"), usage="set sv_scriptHookAllowed false"),
        "sv_protectServerEntities": KeywordInfo("Protect Server Entities", "Protect entities from client modification", "boolean", "false", "security", valid_values=("true", "false"), usage="set sv_protectServerEntities true"),
        "sv_pureLevel": KeywordInfo("Pure Level", "Server purity (0=off, 1=limited, 2=strict)", "number", "0", "security", valid_values=("0", "1", "2"), usage="set sv_pureLevel 0"),
        "sv_requestParanoia": KeywordInfo("Request Paranoia", "Request validation level (0-3)", "number", "0", "security", valid_values=("0", "1", "2", "3"), usage="set sv_requestParanoia 1"),
        "sv_authMaxVariance": KeywordInfo("Auth Max Variance", "Max authentication variance", "number", "1000", "security", min_value="0", max_value="10000", usage="set sv_authMaxVariance 1000"),
        "sv_authMinTrust": KeywordInfo("Auth Min Trust", "Min authentication trust", "number", "0", "security", min_value="0", max_value="100", usage="set sv_authMinTrust 0"),
        "sv_filterRequestControl": KeywordInfo("Filter Request Control", "Request filter level (0=off)", "number", "0", "security", min_value="0", max_value="5", usage="set sv_filterRequestControl 0"),
        "sv_filterRequestControlSettleTimer": KeywordInfo("Filter Request Settle Timer", "Request filter settle timer (ms)", "number", "0", "security", min_value="0", max_value="10000", usage="set sv_filterRequestControlSettleTimer 0"),
        "sv_entityLockdown": KeywordInfo("Entity Lockdown", "Entity lockdown mode", "enum", "inactive", "security", valid_values=("full", "strict", "relaxed", "inactive"), usage="set sv_entityLockdown relaxed"),
        "sv_useAccurateSends": KeywordInfo("Use Accurate Sends", "Use accurate network sends", "boolean", "false", "security", valid_values=("true", "false"), usage="set sv_useAccurateSends false"),
        "onesync": KeywordInfo("OneSync", "Enable OneSync sync mode", "enum", "off", "onesync", valid_values=("on", "off", "legacy"), usage="set onesync on", related=("onesync_enableInfinity",)),
        "onesync_enableInfinity": KeywordInfo("Enable Infinity", "Enable OneSync Infinity", "boolean", "false", "onesync", valid_values=("true", "false"), usage="set onesync_enableInfinity true", related=("onesync",)),
        "onesync_enableBeyond": KeywordInfo("Enable Beyond", "Enable OneSync Beyond", "boolean", "false", "onesync", valid_values=("true", "false"), usage="set onesync_enableBeyond true", related=("onesync",)),
        "onesync_population": KeywordInfo("Population", "Enable population management", "boolean", "false", "onesync", valid_values=("true", "false"), usage="set onesync_population true"),
        "onesync_forceMigration": KeywordInfo("Force Migration", "Force entity migration", "boolean", "false", "onesync", valid_values=("true", "false"), usage="set onesync_forceMigration true"),
        "onesync_distanceCulling": KeywordInfo("Distance Culling", "Enable distance-based culling", "boolean", "false", "onesync", valid_values=("true", "false"), usage="set onesync_distanceCulling true"),
        "onesync_distanceCullVehicles": KeywordInfo("Distance Cull Vehicles", "Distance culling for vehicles", "boolean", "false", "onesync", valid_values=("true", "false"), usage="set onesync_distanceCullVehicles true"),
        "onesync_radiusFrequency": KeywordInfo("Radius Frequency", "Radius-based update frequency", "boolean", "false", "onesync", valid_values=("true", "false"), usage="set onesync_radiusFrequency true"),
        "onesync_migrateDataTimeout": KeywordInfo("Migrate Data Timeout", "Migration data timeout (ms)", "number", "5000", "onesync", min_value="1000", max_value="30000", usage="set onesync_migrateDataTimeout 5000"),
        "onesync_compressionDictionarySamples": KeywordInfo("Compression Dictionary Samples", "Compression dictionary samples", "number", "256", "onesync", min_value="0", max_value="1024", usage="set onesync_compressionDictionarySamples 256"),
        "onesync_mapBoundsMinX": KeywordInfo("Map Bounds Min X", "Min X map boundary", "number", "-4000", "onesync", min_value="-10000", max_value="0", usage="set onesync_mapBoundsMinX -4000"),
        "onesync_mapBoundsMinY": KeywordInfo("Map Bounds Min Y", "Min Y map boundary", "number", "-4000", "onesync", min_value="-10000", max_value="0", usage="set onesync_mapBoundsMinY -4000"),
        "onesync_mapBoundsMaxX": KeywordInfo("Map Bounds Max X", "Max X map boundary", "number", "8000", "onesync", min_value="0", max_value="10000", usage="set onesync_mapBoundsMaxX 8000"),
        "onesync_mapBoundsMaxY": KeywordInfo("Map Bounds Max Y", "Max Y map boundary", "number", "8000", "onesync", min_value="0", max_value="10000", usage="set onesync_mapBoundsMaxY 8000"),
        "onesync_mapCellAreaSize": KeywordInfo("Map Cell Area Size", "Map cell size for spatial partitioning", "number", "100", "onesync", min_value="10", max_value="1000", usage="set onesync_mapCellAreaSize 100"),
        "sv_enableNetworkedSounds": KeywordInfo("Enable Networked Sounds", "Allow networked sounds", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_enableNetworkedSounds true"),
        "sv_enableNetworkedPhoneExplosions": KeywordInfo("Enable Networked Phone Explosions", "Allow networked phone explosions", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_enableNetworkedPhoneExplosions true"),
        "sv_enableNetworkedScriptEntityStates": KeywordInfo("Enable Script Entity States", "Allow script entity state sync", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_enableNetworkedScriptEntityStates true"),
        "sv_enableNetEventReassembly": KeywordInfo("Enable Net Event Reassembly", "Enable event reassembly", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_enableNetEventReassembly true"),
        "sv_netEventReassemblyMaxPendingEvents": KeywordInfo("Max Pending Events", "Max pending events for reassembly", "number", "128", "features", min_value="1", max_value="1024", usage="set sv_netEventReassemblyMaxPendingEvents 128"),
        "sv_netEventReassemblyUnlimitedPendingEvents": KeywordInfo("Unlimited Pending Events", "Allow unlimited pending events", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_netEventReassemblyUnlimitedPendingEvents false"),
        "sv_voiceChat": KeywordInfo("Voice Chat", "Enable built-in voice chat", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_voiceChat true", related=("sv_mumble",)),
        "sv_mumble": KeywordInfo("Mumble Integration", "Enable Mumble voice integration", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_mumble true", related=("sv_voiceChat",)),
        "sv_devMode": KeywordInfo("Developer Mode", "Enable developer mode", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_devMode false"),
        "sv_scriptDebugDuplicates": KeywordInfo("Script Debug Duplicates", "Debug duplicate script events", "boolean", "false", "features", valid_values=("true", "false"), usage="set sv_scriptDebugDuplicates false"),
        "svgui": KeywordInfo("SVG UI", "Enable SVG-based UI", "boolean", "false", "features", valid_values=("true", "false"), usage="set svgui false"),
        "sv_experimentalStateBagsHandler": KeywordInfo("Experimental State Bags", "Use experimental state bags handler", "boolean", "false", "experimental", valid_values=("true", "false"), usage="set sv_experimentalStateBagsHandler false"),
        "sv_experimentalOnesyncPopulation": KeywordInfo("Experimental OneSync Population", "Use experimental OneSync population", "boolean", "false", "experimental", valid_values=("true", "false"), usage="set sv_experimentalOnesyncPopulation false"),
        "sv_experimentalNetGameEventHandler": KeywordInfo("Experimental Net Game Event", "Use experimental net event handler", "boolean", "false", "experimental", valid_values=("true", "false"), usage="set sv_experimentalNetGameEventHandler false"),
        "sv_stateBagStrictMode": KeywordInfo("State Bag Strict Mode", "Enable strict state bag mode", "boolean", "false", "experimental", valid_values=("true", "false"), usage="set sv_stateBagStrictMode false"),
        "sv_httpFileServerProxyOnly": KeywordInfo("HTTP File Server Proxy", "HTTP file server proxy mode", "boolean", "false", "experimental", valid_values=("true", "false"), usage="set sv_httpFileServerProxyOnly false"),
        "sv_prometheusBasicAuthUser": KeywordInfo("Prometheus Auth User", "Prometheus monitoring user", "string", "", "monitoring", usage="set sv_prometheusBasicAuthUser admin"),
        "sv_prometheusBasicAuthPassword": KeywordInfo("Prometheus Auth Password", "Prometheus monitoring password", "string", "", "monitoring", usage="set sv_prometheusBasicAuthPassword secret"),
        "steam_webApiKey": KeywordInfo("Steam Web API Key", "Steam Web API key", "string", "", "steam", min_length=32, max_length=32, usage="set steam_webApiKey YOUR_KEY"),
        "steam_webApiDomain": KeywordInfo("Steam Web API Domain", "Steam Web API domain", "string", "api.steampowered.com", "steam", usage="set steam_webApiDomain api.steampowered.com"),
        "gamename": KeywordInfo("Game Name", "Game name identifier", "string", "gta5", "misc", usage="set gamename gta5"),
        "gametype": KeywordInfo("Game Type", "Game type identifier", "string", "gta5", "misc", usage="set gametype gta5"),
        "mapname": KeywordInfo("Map Name", "Current map name", "string", "gta5", "misc", usage="set mapname gta5"),
        "load_server_icon": KeywordInfo("Load Server Icon", "Load server icon file", "string", "", "misc", usage="load_server_icon icon.png"),
        "exec": KeywordInfo("Execute Config", "Execute a config file", "string", "", "misc", usage="exec server_private.cfg"),
        "increase_pool_size": KeywordInfo("Increase Pool Size", "Increase memory pool size", "string", "", "misc", usage="increase_pool_size 10"),
        "rateLimiter_challenge_rate": KeywordInfo("Challenge Rate", "Rate limit for challenge requests", "number", "10", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_challenge_rate 10", related=("rateLimiter_challenge_burst",)),
        "rateLimiter_challenge_burst": KeywordInfo("Challenge Burst", "Burst limit for challenge requests", "number", "50", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_challenge_burst 50", related=("rateLimiter_challenge_rate",)),
        "rateLimiter_handshake_rate": KeywordInfo("Handshake Rate", "Rate limit for TCP handshake", "number", "5", "ratelimiter", min_value="0", max_value="1000", usage="set rateLimiter_handshake_rate 5", related=("rateLimiter_handshake_burst",)),
        "rateLimiter_handshake_burst": KeywordInfo("Handshake Burst", "Burst limit for TCP handshake", "number", "10", "ratelimiter", min_value="0", max_value="1000", usage="set rateLimiter_handshake_burst 10", related=("rateLimiter_handshake_rate",)),
        "rateLimiter_handshakeUDP_rate": KeywordInfo("Handshake UDP Rate", "Rate limit for UDP handshake", "number", "50", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_handshakeUDP_rate 50", related=("rateLimiter_handshakeUDP_burst",)),
        "rateLimiter_handshakeUDP_burst": KeywordInfo("Handshake UDP Burst", "Burst limit for UDP handshake", "number", "100", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_handshakeUDP_burst 100", related=("rateLimiter_handshakeUDP_rate",)),
        "rateLimiter_http_dynamic_rate": KeywordInfo("HTTP Dynamic Rate", "Rate limit for dynamic HTTP", "number", "20", "ratelimiter", min_value="0", max_value="1000", usage="set rateLimiter_http_dynamic_rate 20", related=("rateLimiter_http_dynamic_burst",)),
        "rateLimiter_http_dynamic_burst": KeywordInfo("HTTP Dynamic Burst", "Burst limit for dynamic HTTP", "number", "40", "ratelimiter", min_value="0", max_value="1000", usage="set rateLimiter_http_dynamic_burst 40", related=("rateLimiter_http_dynamic_rate",)),
        "rateLimiter_http_info_rate": KeywordInfo("HTTP Info Rate", "Rate limit for /info", "number", "20", "ratelimiter", min_value="0", max_value="1000", usage="set rateLimiter_http_info_rate 20", related=("rateLimiter_http_info_burst",)),
        "rateLimiter_http_info_burst": KeywordInfo("HTTP Info Burst", "Burst limit for /info", "number", "40", "ratelimiter", min_value="0", max_value="1000", usage="set rateLimiter_http_info_burst 40", related=("rateLimiter_http_info_rate",)),
        "rateLimiter_http_perf_rate": KeywordInfo("HTTP Perf Rate", "Rate limit for /perf", "number", "2", "ratelimiter", min_value="0", max_value="100", usage="set rateLimiter_http_perf_rate 2", related=("rateLimiter_http_perf_burst",)),
        "rateLimiter_http_perf_burst": KeywordInfo("HTTP Perf Burst", "Burst limit for /perf", "number", "4", "ratelimiter", min_value="0", max_value="100", usage="set rateLimiter_http_perf_burst 4", related=("rateLimiter_http_perf_rate",)),
        "rateLimiter_http_players_rate": KeywordInfo("HTTP Players Rate", "Rate limit for /players", "number", "5", "ratelimiter", min_value="0", max_value="100", usage="set rateLimiter_http_players_rate 5", related=("rateLimiter_http_players_burst",)),
        "rateLimiter_http_players_burst": KeywordInfo("HTTP Players Burst", "Burst limit for /players", "number", "10", "ratelimiter", min_value="0", max_value="100", usage="set rateLimiter_http_players_burst 10", related=("rateLimiter_http_players_rate",)),
        "rateLimiter_netCommand_rate": KeywordInfo("Net Command Rate", "Rate limit for net commands", "number", "400", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_netCommand_rate 400", related=("rateLimiter_netCommand_burst",)),
        "rateLimiter_netCommand_burst": KeywordInfo("Net Command Burst", "Burst limit for net commands", "number", "800", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_netCommand_burst 800", related=("rateLimiter_netCommand_rate",)),
        "rateLimiter_netCommandFlood_rate": KeywordInfo("Net Command Flood Rate", "Rate limit for command flood", "number", "200", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_netCommandFlood_rate 200", related=("rateLimiter_netCommandFlood_burst",)),
        "rateLimiter_netCommandFlood_burst": KeywordInfo("Net Command Flood Burst", "Burst limit for command flood", "number", "400", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_netCommandFlood_burst 400", related=("rateLimiter_netCommandFlood_rate",)),
        "rateLimiter_netCommandSize_rate": KeywordInfo("Net Command Size Rate", "Rate limit for command size", "number", "8000", "ratelimiter", min_value="0", max_value="100000", usage="set rateLimiter_netCommandSize_rate 8000", related=("rateLimiter_netCommandSize_burst",)),
        "rateLimiter_netCommandSize_burst": KeywordInfo("Net Command Size Burst", "Burst limit for command size", "number", "16000", "ratelimiter", min_value="0", max_value="100000", usage="set rateLimiter_netCommandSize_burst 16000", related=("rateLimiter_netCommandSize_rate",)),
        "rateLimiter_netEvent_rate": KeywordInfo("Net Event Rate", "Rate limit for net events", "number", "400", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_netEvent_rate 400", related=("rateLimiter_netEvent_burst",)),
        "rateLimiter_netEvent_burst": KeywordInfo("Net Event Burst", "Burst limit for net events", "number", "800", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_netEvent_burst 800", related=("rateLimiter_netEvent_rate",)),
        "rateLimiter_netEventFlood_rate": KeywordInfo("Net Event Flood Rate", "Rate limit for event flood", "number", "200", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_netEventFlood_rate 200", related=("rateLimiter_netEventFlood_burst",)),
        "rateLimiter_netEventFlood_burst": KeywordInfo("Net Event Flood Burst", "Burst limit for event flood", "number", "400", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_netEventFlood_burst 400", related=("rateLimiter_netEventFlood_rate",)),
        "rateLimiter_rcon_rate": KeywordInfo("RCON Rate", "Rate limit for RCON", "number", "4", "ratelimiter", min_value="0", max_value="100", usage="set rateLimiter_rcon_rate 4", related=("rateLimiter_rcon_burst",)),
        "rateLimiter_rcon_burst": KeywordInfo("RCON Burst", "Burst limit for RCON", "number", "8", "ratelimiter", min_value="0", max_value="100", usage="set rateLimiter_rcon_burst 8", related=("rateLimiter_rcon_rate",)),
        "rateLimiter_res_http_handler_rate": KeywordInfo("Resource HTTP Rate", "Rate limit for resource HTTP", "number", "20", "ratelimiter", min_value="0", max_value="1000", usage="set rateLimiter_res_http_handler_rate 20", related=("rateLimiter_res_http_handler_burst",)),
        "rateLimiter_res_http_handler_burst": KeywordInfo("Resource HTTP Burst", "Burst limit for resource HTTP", "number", "40", "ratelimiter", min_value="0", max_value="1000", usage="set rateLimiter_res_http_handler_burst 40", related=("rateLimiter_res_http_handler_rate",)),
        "rateLimiter_resourceList_rate": KeywordInfo("Resource List Rate", "Rate limit for resource list", "number", "2", "ratelimiter", min_value="0", max_value="100", usage="set rateLimiter_resourceList_rate 2", related=("rateLimiter_resourceList_burst",)),
        "rateLimiter_resourceList_burst": KeywordInfo("Resource List Burst", "Burst limit for resource list", "number", "4", "ratelimiter", min_value="0", max_value="100", usage="set rateLimiter_resourceList_burst 4", related=("rateLimiter_resourceList_rate",)),
        "rateLimiter_stateBag_rate": KeywordInfo("State Bag Rate", "Rate limit for state bags", "number", "512", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_stateBag_rate 512", related=("rateLimiter_stateBag_burst",)),
        "rateLimiter_stateBag_burst": KeywordInfo("State Bag Burst", "Burst limit for state bags", "number", "1024", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_stateBag_burst 1024", related=("rateLimiter_stateBag_rate",)),
        "rateLimiter_stateBagFlood_rate": KeywordInfo("State Bag Flood Rate", "Rate limit for state bag flood", "number", "256", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_stateBagFlood_rate 256", related=("rateLimiter_stateBagFlood_burst",)),
        "rateLimiter_stateBagFlood_burst": KeywordInfo("State Bag Flood Burst", "Burst limit for state bag flood", "number", "512", "ratelimiter", min_value="0", max_value="10000", usage="set rateLimiter_stateBagFlood_burst 512", related=("rateLimiter_stateBagFlood_rate",)),
        "rateLimiter_stateBagSize_rate": KeywordInfo("State Bag Size Rate", "Rate limit for state bag size", "number", "524288", "ratelimiter", min_value="0", max_value="10000000", usage="set rateLimiter_stateBagSize_rate 524288", related=("rateLimiter_stateBagSize_burst",)),
        "rateLimiter_stateBagSize_burst": KeywordInfo("State Bag Size Burst", "Burst limit for state bag size", "number", "1048576", "ratelimiter", min_value="0", max_value="10000000", usage="set rateLimiter_stateBagSize_burst 1048576", related=("rateLimiter_stateBagSize_rate",)),
        "ensure": KeywordInfo("Ensure Resource", "Start resource and keep it running", "action", "", "action", params=(ParamInfo("resource", "str", True, description="Resource name"),), usage="ensure es_extended", related=("ensure_stop", "start", "stop")),
        "ensure_stop": KeywordInfo("Stop Ensured", "Stop an ensured resource", "action", "", "action", params=(ParamInfo("resource", "str", True, description="Resource name"),), usage="ensure_stop es_extended", related=("ensure",)),
        "quit": KeywordInfo("Quit Server", "Shut down the server", "action", "", "action", usage="quit", related=("restart",)),
        "refresh": KeywordInfo("Refresh Resources", "Refresh available resources", "action", "", "action", usage="refresh", related=("start", "stop")),
        "restart": KeywordInfo("Restart Server", "Restart the server", "action", "", "action", usage="restart", related=("quit",)),
        "say": KeywordInfo("Say Message", "Send server message", "action", "", "action", params=(ParamInfo("message", "str", True, description="Message"),), usage="say Hello!"),
        "start": KeywordInfo("Start Resource", "Start a resource", "action", "", "action", params=(ParamInfo("resource", "str", True, description="Resource name"),), usage="start es_extended", related=("stop", "ensure")),
        "stop": KeywordInfo("Stop Resource", "Stop a resource", "action", "", "action", params=(ParamInfo("resource", "str", True, description="Resource name"),), usage="stop es_extended", related=("start", "ensure")),
        "set": KeywordInfo("Set Convar", "Set a config variable (not replicated)", "command", "", "command", params=(ParamInfo("name", "str", True, description="Convar name"), ParamInfo("value", "str", True, description="Value")), usage="set sv_lan true", related=("setr", "sets")),
        "setr": KeywordInfo("Set Replicated", "Set a replicated config variable", "command", "", "command", params=(ParamInfo("name", "str", True, description="Convar name"), ParamInfo("value", "str", True, description="Value")), usage="setr sv_hostname My Server", related=("set", "sets")),
        "sets": KeywordInfo("Set Saved", "Set a saved config variable", "command", "", "command", params=(ParamInfo("name", "str", True, description="Convar name"), ParamInfo("value", "str", True, description="Value")), usage="sets sv_projectName My Project", related=("set", "setr")),
        "add_ace": KeywordInfo("Add ACE Permission", "Add ACE permission for principal", "command", "", "command", params=(ParamInfo("principal", "str", True, description="Principal"), ParamInfo("object", "str", True, description="Permission object"), ParamInfo("permission", "str", True, "allow", "allow/deny")), usage="add_ace group.admin command allow", related=("remove_ace", "add_principal")),
        "add_principal": KeywordInfo("Add Principal", "Add child principal to parent", "command", "", "command", params=(ParamInfo("child", "str", True, description="Child principal"), ParamInfo("parent", "str", True, description="Parent principal")), usage="add_principal identifier.license:abc group.admin", related=("remove_principal",)),
        "remove_ace": KeywordInfo("Remove ACE Permission", "Remove ACE permission", "command", "", "command", params=(ParamInfo("principal", "str", True, description="Principal"), ParamInfo("object", "str", True, description="Permission object"), ParamInfo("permission", "str", True, "allow", "Permission level")), usage="remove_ace group.admin command allow", related=("add_ace",)),
        "remove_principal": KeywordInfo("Remove Principal", "Remove child from parent", "command", "", "command", params=(ParamInfo("child", "str", True, description="Child principal"), ParamInfo("parent", "str", True, description="Parent principal")), usage="remove_principal identifier.license:abc group.admin", related=("add_principal",)),
        "block_net_game_event": KeywordInfo("Block Net Game Event", "Block a network game event", "command", "", "command", params=(ParamInfo("event_name", "str", True, description="Event name"),), usage="block_net_game_event someEvent", related=("unblock_net_game_event",)),
        "unblock_net_game_event": KeywordInfo("Unblock Net Game Event", "Unblock a network game event", "command", "", "command", params=(ParamInfo("event_name", "str", True, description="Event name"),), usage="unblock_net_game_event someEvent", related=("block_net_game_event",)),
        "test_ace": KeywordInfo("Test ACE", "Test ACE permission", "command", "", "command", params=(ParamInfo("principal", "str", True, description="Principal"), ParamInfo("object", "str", True, description="Object"), ParamInfo("permission", "str", True, "allow", "Permission level")), usage="test_ace group.admin command allow", related=("add_ace",)),
        "replay_start": KeywordInfo("Start Replay", "Start recording replay", "command", "", "command", usage="replay_start", related=("replay_stop",)),
        "replay_stop": KeywordInfo("Stop Replay", "Stop recording replay", "command", "", "command", usage="replay_stop", related=("replay_start",)),
        "sync_start_recording": KeywordInfo("Start Sync Recording", "Start synced recording", "command", "", "command", usage="sync_start_recording", related=("sync_stop_recording",)),
        "sync_stop_recording": KeywordInfo("Stop Sync Recording", "Stop synced recording", "command", "", "command", usage="sync_stop_recording", related=("sync_start_recording",)),
        "con_channelFilters": KeywordInfo("Set Channel Filters", "Set console channel filters", "command", "", "command", usage="con_channelFilters value"),
        "con_addChannelFilter": KeywordInfo("Add Channel Filter", "Add console channel filter", "command", "", "command", params=(ParamInfo("filter", "str", True, description="Filter value"),), usage="con_addChannelFilter value", related=("con_removeChannelFilter",)),
        "con_removeChannelFilter": KeywordInfo("Remove Channel Filter", "Remove console channel filter", "command", "", "command", params=(ParamInfo("filter", "str", True, description="Filter value"),), usage="con_removeChannelFilter value", related=("con_addChannelFilter",)),
        "endpoint_add_tcp": KeywordInfo("Add TCP Endpoint", "Add a TCP endpoint", "command", "", "command", params=(ParamInfo("endpoint", "str", True, description="Endpoint (ip:port)"),), usage="endpoint_add_tcp 0.0.0.0:30120", related=("endpoint_add_udp",)),
        "endpoint_add_udp": KeywordInfo("Add UDP Endpoint", "Add a UDP endpoint", "command", "", "command", params=(ParamInfo("endpoint", "str", True, description="Endpoint (ip:port)"),), usage="endpoint_add_udp 0.0.0.0:30121", related=("endpoint_add_tcp",)),
        "builtin.everyone": KeywordInfo("Everyone", "All players", "principal", "", "principal", usage="add_ace builtin.everyone command allow"),
        "builtin.restricted": KeywordInfo("Restricted", "Restricted players", "principal", "", "principal", usage="add_ace builtin.restricted command allow"),
        "group.admin": KeywordInfo("Admin Group", "Administrators", "principal", "", "principal", related=("group.moderator", "group.owner")),
        "group.moderator": KeywordInfo("Moderator Group", "Moderators", "principal", "", "principal", related=("group.admin",)),
        "group.owner": KeywordInfo("Owner Group", "Server owner", "principal", "", "principal", related=("group.admin",)),
        "group.user": KeywordInfo("User Group", "Regular users", "principal", "", "principal"),
        "group.support": KeywordInfo("Support Group", "Support staff", "principal", "", "principal"),
        "group.helper": KeywordInfo("Helper Group", "Helpers", "principal", "", "principal"),
        "group.god": KeywordInfo("God Group", "God-level permissions", "principal", "", "principal"),
        "group.superadmin": KeywordInfo("Superadmin Group", "Super administrators", "principal", "", "principal", related=("group.admin",)),
        "group.developer": KeywordInfo("Developer Group", "Developers", "principal", "", "principal"),
        "identifier.steam": KeywordInfo("Steam Identifier", "Steam platform identifier", "principal", "", "principal", usage="add_principal identifier.steam:12345 group.admin"),
        "identifier.license": KeywordInfo("License Identifier", "FiveM license identifier", "principal", "", "principal", usage="add_principal identifier.license:abc123 group.admin"),
        "identifier.discord": KeywordInfo("Discord Identifier", "Discord identifier", "principal", "", "principal", usage="add_principal identifier.discord:123456789 group.admin"),
        "identifier.fivem": KeywordInfo("FiveM Identifier", "FiveM platform identifier", "principal", "", "principal"),
        "identifier.ip": KeywordInfo("IP Identifier", "IP address identifier", "principal", "", "principal"),
        "identifier.xbl": KeywordInfo("Xbox Live Identifier", "Xbox Live identifier", "principal", "", "principal"),
        "resource.mapmanager": KeywordInfo("Map Manager", "mapmanager resource", "principal", "", "principal"),
        "resource.chat": KeywordInfo("Chat Resource", "chat resource", "principal", "", "principal"),
        "resource.spawnmanager": KeywordInfo("Spawn Manager", "spawnmanager resource", "principal", "", "principal"),
        "resource.sessionmanager": KeywordInfo("Session Manager", "sessionmanager resource", "principal", "", "principal"),
        "resource.hardcap": KeywordInfo("Hardcap", "hardcap resource", "principal", "", "principal"),
        "resource.rconlog": KeywordInfo("RCON Log", "rconlog resource", "principal", "", "principal"),
        "resource.baseevents": KeywordInfo("Base Events", "baseevents resource", "principal", "", "principal"),
        "command": KeywordInfo("Command Base", "All commands", "principal", "", "principal", related=("command.kick", "command.ban")),
        "command.kick": KeywordInfo("Kick Command", "Kick players", "principal", "", "principal", related=("command.ban",)),
        "command.ban": KeywordInfo("Ban Command", "Ban players", "principal", "", "principal", related=("command.kick",)),
        "command.tempban": KeywordInfo("Tempban Command", "Temporarily ban players", "principal", "", "principal", related=("command.ban",)),
        "command.setgroup": KeywordInfo("Setgroup Command", "Set player groups", "principal", "", "principal"),
        "command.admin": KeywordInfo("Admin Command", "Admin commands", "principal", "", "principal"),
        "command.noclip": KeywordInfo("Noclip Command", "Toggle noclip", "principal", "", "principal"),
        "command.tpm": KeywordInfo("TPM Command", "Teleport to marker", "principal", "", "principal"),
        "command.bring": KeywordInfo("Bring Command", "Bring player to you", "principal", "", "principal"),
        "command.revive": KeywordInfo("Revive Command", "Revive player", "principal", "", "principal"),
        "command.heal": KeywordInfo("Heal Command", "Heal player", "principal", "", "principal"),
        "command.announce": KeywordInfo("Announce Command", "Server announcements", "principal", "", "principal"),
        "command.car": KeywordInfo("Car Command", "Spawn vehicles", "principal", "", "principal"),
        "command.weather": KeywordInfo("Weather Command", "Change weather", "principal", "", "principal"),
        "command.time": KeywordInfo("Time Command", "Change time", "principal", "", "principal"),
        "command.quit": KeywordInfo("Quit Command", "Quit the server", "principal", "", "principal"),
        "command.add_ace": KeywordInfo("Add ACE Command", "add_ace command permission", "principal", "", "principal"),
        "command.add_principal": KeywordInfo("Add Principal Command", "add_principal command permission", "principal", "", "principal"),
        "txAdmin.kick": KeywordInfo("TXAdmin Kick", "txAdmin kick permission", "principal", "", "principal"),
        "txAdmin.ban": KeywordInfo("TXAdmin Ban", "txAdmin ban permission", "principal", "", "principal"),
        "txAdmin.warn": KeywordInfo("TXAdmin Warn", "txAdmin warn permission", "principal", "", "principal"),
        "txAdmin.players.heal": KeywordInfo("TXAdmin Heal", "txAdmin heal permission", "principal", "", "principal"),
        "qbcore.admin": KeywordInfo("QBCore Admin", "QBCore admin permissions", "principal", "", "principal"),
        "qbx.admin": KeywordInfo("QBx Admin", "QBx admin permissions", "principal", "", "principal"),
        "esx.admin": KeywordInfo("ESX Admin", "ESX admin permissions", "principal", "", "principal"),
        "mapmanager": KeywordInfo("Map Manager (bare)", "mapmanager permission", "principal", "", "principal"),
        "chat": KeywordInfo("Chat (bare)", "chat permission", "principal", "", "principal"),
        "spawnmanager": KeywordInfo("Spawn Manager (bare)", "spawnmanager permission", "principal", "", "principal"),
        "sessionmanager": KeywordInfo("Session Manager (bare)", "sessionmanager permission", "principal", "", "principal"),
        "basic-gamemode": KeywordInfo("Basic Gamemode", "basic-gamemode permission", "principal", "", "principal"),
        "hardcap": KeywordInfo("Hardcap (bare)", "hardcap permission", "principal", "", "principal"),
        "rconlog": KeywordInfo("RCON Log (bare)", "rconlog permission", "principal", "", "principal"),
        "baseevents": KeywordInfo("Base Events (bare)", "baseevents permission", "principal", "", "principal"),
        "allow": KeywordInfo("Allow", "Grant permission", "state", "", "state", usage="add_ace group.admin command allow", related=("deny",)),
        "deny": KeywordInfo("Deny", "Deny permission", "state", "", "state", usage="add_ace group.user command deny", related=("allow",)),
        "deny_socket": KeywordInfo("Deny Socket", "Deny socket access", "state", "", "state", usage="add_ace group.user endpoint deny_socket"),
        "true": KeywordInfo("True", "Boolean true", "state", "", "state", related=("false",)),
        "false": KeywordInfo("False", "Boolean false", "state", "", "state", related=("true",)),
        "on": KeywordInfo("On", "Enable feature", "state", "", "state", related=("off",)),
        "off": KeywordInfo("Off", "Disable feature", "state", "", "state", related=("on",)),
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
