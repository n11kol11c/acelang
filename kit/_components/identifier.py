from __future__ import annotations
from dataclasses import dataclass, field


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
    deprecated: bool = False
    startup_only: bool = False
    warning: str = ""
    since: str = ""


class _G:
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
        "sv_replaceExeToSwitchBuilds", "sv_showBusySpinnerOnLoadingScreen",
        "sv_endpointurl", "sv_kick_players_cnl", "sv_exposePlayerIdentifiersInHttpEndpoint",
        "txAdmin-menuEnabled", "txAdmin-menuAlignRight", "txAdmin-menuPageKey",
        "txAdmin-hideDefaultAnnouncement", "txAdmin-hideDefaultDirectMessage",
        "txAdmin-hideDefaultWarning", "txAdmin-hideDefaultScheduledRestartWarning",
        "txAdmin-debugMode", "txAdmin-menuPlayerIdDistance", "txAdmin-menuDrunkDuration",
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
        "status", "clientkick", "moo",
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
        # ═══════════════════════════════════════════════════════════
        # SERVER CONFIGURATION
        # ═══════════════════════════════════════════════════════════
        "sv_hostname": KeywordInfo("Server Hostname", "Server name shown in the browser", "string", "Cfx.re Default Server", "server", max_length=128, usage='sv_hostname "My Awesome Server"', related=("sv_projectName", "sv_projectDesc")),
        "sv_maxClients": KeywordInfo("Max Clients", "Maximum player slots (1-2048, 32+ needs onesync)", "number", "48", "server", min_value="1", max_value="2048", usage="sv_maxClients 48", related=("sv_maxclients",)),
        "sv_maxclients": KeywordInfo("Max Clients (lowercase)", "Maximum player slots (lowercase alias)", "number", "48", "server", min_value="1", max_value="2048", usage="sv_maxclients 48", aliases=("sv_maxClients",)),
        "sv_licenseKey": KeywordInfo("License Key", "FiveM license key from portal.cfx.re (required)", "string", "", "server", min_length=1, usage='sv_licenseKey "your_license_key_here"', warning="Required for non-LAN servers"),
        "sv_lan": KeywordInfo("LAN Mode", "LAN-only mode (skips license key check)", "boolean", "false", "server", valid_values=("true", "false"), usage="sv_lan false"),
        "sv_projectName": KeywordInfo("Project Name", "Project name shown in txAdmin", "string", "My FXServer Project", "server", max_length=64, usage='sv_projectName "My FXServer Project"'),
        "sv_projectDesc": KeywordInfo("Project Description", "Project description shown in txAdmin", "string", "Default FXServer requiring configuration", "server", max_length=256, usage='sv_projectDesc "Default FXServer requiring configuration"'),
        "sv_appearAllowlisted": KeywordInfo("Appear Allowlisted", "Show server as allowlisted in browser", "boolean", "false", "server", valid_values=("true", "false"), usage="sets sv_appearAllowlisted false"),
        "sv_allowlistInstructions": KeywordInfo("Allowlist Instructions", "Instructions for non-allowlisted players", "string", "", "server", usage='sets sv_allowlistInstructions "Contact us on Discord"'),
        "sv_enforceGameBuild": KeywordInfo("Enforce Game Build", "Force a specific GTA V game build number", "number", "0", "server", min_value="0", max_value="9999", usage="sv_enforceGameBuild 2944"),
        "sv_master1": KeywordInfo("Master Server", "Master server URL (empty = private server)", "string", "", "server", usage='sv_master1 ""'),
        "sv_tebexSecret": KeywordInfo("Tebex Secret", "Tebex store integration secret key", "string", "", "server", usage='sv_tebexSecret "your_secret_here"'),
        "sv_kvsName": KeywordInfo("KVS Name", "Key-Value Store database file name (startup only)", "string", "default", "server", startup_only=True, usage='sv_kvsName "default"'),
        "sv_endpoints": KeywordInfo("Endpoints", "Space-separated list of client UDP endpoints", "string", "", "server", usage='sv_endpoints "1.2.3.4:30120"'),
        "sv_registerMulticastDns": KeywordInfo("Multicast DNS", "Register via mDNS for LAN discovery", "boolean", "true", "server", valid_values=("true", "false"), usage="sv_registerMulticastDns true"),

        # ═══════════════════════════════════════════════════════════
        # NETWORK
        # ═══════════════════════════════════════════════════════════
        "netPort": KeywordInfo("Network Port", "Primary server port", "number", "30120", "network", min_value="1", max_value="65535", usage="netPort 30120"),
        "net_tcpConnLimit": KeywordInfo("TCP Connection Limit", "Concurrent connection limit per IP", "number", "16", "network", min_value="0", max_value="65535", usage="net_tcpConnLimit 32"),
        "sv_tcpConnectionTimeoutSeconds": KeywordInfo("TCP Timeout", "TCP connection idle timeout in seconds", "number", "5", "network", min_value="1", max_value="300", usage="sv_tcpConnectionTimeoutSeconds 5"),
        "sv_ioThreads": KeywordInfo("IO Threads", "Network IO threads (0 = CPU core count)", "number", "0", "network", min_value="0", max_value="16", usage="sv_ioThreads 0"),
        "sv_clientConnectingTimeoutMilliseconds": KeywordInfo("Client Connecting Timeout", "Timeout for clients during connection (ms)", "number", "60000", "network", min_value="1000", max_value="120000", usage="sv_clientConnectingTimeoutMilliseconds 60000"),
        "sv_clientConnectedTimeoutMilliseconds": KeywordInfo("Client Connected Timeout", "Timeout for connected clients (ms)", "number", "120000", "network", min_value="0", max_value="600000", usage="sv_clientConnectedTimeoutMilliseconds 120000"),
        "sv_pingIntervalMilliseconds": KeywordInfo("Ping Interval", "Client ping check interval (ms)", "number", "5000", "network", min_value="1000", max_value="30000", usage="sv_pingIntervalMilliseconds 5000"),
        "sv_endpointPrivacy": KeywordInfo("Endpoint Privacy", "Hide player IPs from public reports", "boolean", "true", "network", valid_values=("true", "false"), usage="sv_endpointPrivacy true"),
        "sv_forceIndirectListing": KeywordInfo("Force Indirect Listing", "Prevent server from using real IP for listing", "boolean", "false", "network", valid_values=("true", "false"), usage="sv_forceIndirectListing false"),
        "sv_listingIpOverride": KeywordInfo("Listing IP Override", "Override IP sent to master server", "string", "", "network", usage='sv_listingIpOverride "1.2.3.4"'),
        "sv_listingHostOverride": KeywordInfo("Listing Host Override", "Override hostname sent to master server", "string", "", "network", usage='sv_listingHostOverride "myserver.example.com"'),
        "sv_proxyIPRanges": KeywordInfo("Proxy IP Ranges", "Proxy IP ranges in CIDR notation (space-separated)", "string", "", "network", usage='sv_proxyIPRanges "10.0.0.0/8 127.0.0.0/8 192.168.0.0/16 172.16.0.0/12"'),
        "sv_enhancedHostSupport": KeywordInfo("Enhanced Host Support", "Enable enhanced hosting features (deprecated)", "boolean", "false", "network", valid_values=("true", "false"), deprecated=True, warning="Not used anymore"),

        # ═══════════════════════════════════════════════════════════
        # SECURITY & AUTHENTICATION
        # ═══════════════════════════════════════════════════════════
        "rcon_password": KeywordInfo("RCON Password", "UDP remote console password", "string", "", "security", min_length=1, usage='rcon_password "your_password_here"', warning="Never use setr for this!"),
        "sv_scriptHookAllowed": KeywordInfo("Script Hook Allowed", "Allow ScriptHookV (0=disallow, 1=allow)", "boolean", "0", "security", valid_values=("0", "1"), usage="sv_scriptHookAllowed 0"),
        "sv_enforceGameBuild": KeywordInfo("Enforce Game Build", "Force clients to use specific GTA V build", "number", "0", "server", min_value="0", max_value="9999", usage="sv_enforceGameBuild 2944"),
        "sv_authMaxVariance": KeywordInfo("Auth Max Variance", "Steam authentication variance (1-5)", "number", "1", "security", min_value="1", max_value="5", usage="sv_authMaxVariance 1"),
        "sv_authMinTrust": KeywordInfo("Auth Min Trust", "Steam authentication min trust (1-5)", "number", "5", "security", min_value="1", max_value="5", usage="sv_authMinTrust 5"),
        "sv_requestParanoia": KeywordInfo("Request Paranoia", "Anti-DDoS proxy flood protection (0-3)", "number", "0", "security", valid_values=("0", "1", "2", "3"), usage="sv_requestParanoia 0"),
        "sv_filterRequestControl": KeywordInfo("Filter Request Control", "Block REQUEST_CONTROL_EVENT routing (-1 to 4)", "number", "0", "security", min_value="-1", max_value="4", usage="sv_filterRequestControl 0"),
        "sv_filterRequestControlSettleTimer": KeywordInfo("Filter Request Settle Timer", "Settle timer for filter request control (ms)", "number", "30000", "security", min_value="0", max_value="60000", usage="sv_filterRequestControlSettleTimer 30000"),
        "sv_pureLevel": KeywordInfo("Pure Level", "Prevent modified client files (0=off, 1=block modified, 2=block all)", "number", "0", "security", valid_values=("0", "1", "2"), usage="sv_pureLevel 0"),
        "sv_entityLockdown": KeywordInfo("Entity Lockdown", "Entity creation lockdown mode", "enum", "inactive", "security", valid_values=("full", "strict", "relaxed", "inactive"), usage="sv_entityLockdown inactive"),
        "sv_useAccurateSends": KeywordInfo("Use Accurate Sends", "Enable/disable accurate entity sends", "boolean", "true", "security", valid_values=("true", "false"), usage="sv_useAccurateSends true"),
        "sv_protectServerEntities": KeywordInfo("Protect Server Entities", "Protect server entities from client modification (deprecated)", "boolean", "false", "security", valid_values=("true", "false"), deprecated=True, warning="Not implemented, use sv_entityLockdown"),

        # ═══════════════════════════════════════════════════════════
        # ONESYNC
        # ═══════════════════════════════════════════════════════════
        "onesync": KeywordInfo("OneSync", "Enable OneSync (required for 32+ players)", "enum", "off", "onesync", valid_values=("on", "off", "legacy"), usage="onesync on", related=("onesync_enableInfinity", "onesync_population")),
        "onesync_enableInfinity": KeywordInfo("Enable Infinity", "Enable Infinity system for large player counts", "boolean", "true", "onesync", valid_values=("true", "false"), usage="onesync_enableInfinity true", related=("onesync",)),
        "onesync_enableBeyond": KeywordInfo("Enable Beyond", "Enable OneSync Beyond (deprecated, not necessary anymore)", "boolean", "false", "onesync", valid_values=("true", "false"), deprecated=True, warning="Not necessary anymore"),
        "onesync_population": KeywordInfo("Population", "Enable population spawning/NPCs", "boolean", "true", "onesync", valid_values=("true", "false"), usage="onesync_population true"),
        "onesync_forceMigration": KeywordInfo("Force Migration", "Force entity migration when owner disconnects", "boolean", "true", "onesync", valid_values=("true", "false"), usage="onesync_forceMigration true"),
        "onesync_distanceCulling": KeywordInfo("Distance Culling", "Remove entities beyond distance", "boolean", "true", "onesync", valid_values=("true", "false"), usage="onesync_distanceCulling true", related=("onesync_distanceCullVehicles",)),
        "onesync_distanceCullVehicles": KeywordInfo("Distance Cull Vehicles", "Apply distance culling to vehicles", "boolean", "false", "onesync", valid_values=("true", "false"), usage="onesync_distanceCullVehicles false", related=("onesync_distanceCulling",)),
        "onesync_radiusFrequency": KeywordInfo("Radius Frequency", "Adjust update frequency by distance", "boolean", "true", "onesync", valid_values=("true", "false"), usage="onesync_radiusFrequency true"),
        "onesync_migrateDataTimeout": KeywordInfo("Migrate Data Timeout", "Migration data timeout in ms", "number", "10000", "onesync", min_value="1000", max_value="60000", usage="onesync_migrateDataTimeout 10000"),
        "onesync_compressionDictionarySamples": KeywordInfo("Compression Dictionary Samples", "Compression dictionary samples", "boolean", "false", "onesync", valid_values=("true", "false"), usage="onesync_compressionDictionarySamples false"),
        "onesync_mapBoundsMinX": KeywordInfo("Map Bounds Min X", "Min X map boundary (startup only)", "number", "-10000", "onesync", min_value="-100000", max_value="0", startup_only=True, usage="onesync_mapBoundsMinX -10000"),
        "onesync_mapBoundsMinY": KeywordInfo("Map Bounds Min Y", "Min Y map boundary (startup only)", "number", "-10000", "onesync", min_value="-100000", max_value="0", startup_only=True, usage="onesync_mapBoundsMinY -10000"),
        "onesync_mapBoundsMaxX": KeywordInfo("Map Bounds Max X", "Max X map boundary (startup only)", "number", "65536", "onesync", min_value="0", max_value="100000", startup_only=True, usage="onesync_mapBoundsMaxX 65536"),
        "onesync_mapBoundsMaxY": KeywordInfo("Map Bounds Max Y", "Max Y map boundary (startup only)", "number", "65536", "onesync", min_value="0", max_value="100000", startup_only=True, usage="onesync_mapBoundsMaxY 65536"),
        "onesync_mapCellAreaSize": KeywordInfo("Map Cell Area Size", "Cell area size for spatial partitioning (startup only)", "number", "100", "onesync", min_value="10", max_value="1000", startup_only=True, usage="onesync_mapCellAreaSize 100"),

        # ═══════════════════════════════════════════════════════════
        # FEATURES
        # ═══════════════════════════════════════════════════════════
        "sv_enableNetworkedSounds": KeywordInfo("Enable Networked Sounds", "Prevent networked sounds exploitation", "boolean", "true", "features", valid_values=("true", "false"), usage="sv_enableNetworkedSounds true"),
        "sv_enableNetworkedPhoneExplosions": KeywordInfo("Enable Networked Phone Explosions", "Prevent phone explosions exploitation", "boolean", "false", "features", valid_values=("true", "false"), usage="sv_enableNetworkedPhoneExplosions false"),
        "sv_enableNetworkedScriptEntityStates": KeywordInfo("Enable Script Entity States", "Prevent script entity state exploitation", "boolean", "true", "features", valid_values=("true", "false"), usage="sv_enableNetworkedScriptEntityStates true"),
        "sv_enableNetEventReassembly": KeywordInfo("Enable Net Event Reassembly", "Enable reassembly of large network events", "boolean", "true", "features", valid_values=("true", "false"), usage="sv_enableNetEventReassembly true", related=("sv_netEventReassemblyMaxPendingEvents",)),
        "sv_netEventReassemblyMaxPendingEvents": KeywordInfo("Max Pending Events", "Max pending reassembled events per client", "number", "100", "features", min_value="1", max_value="1024", usage="sv_netEventReassemblyMaxPendingEvents 100", related=("sv_enableNetEventReassembly",)),
        "sv_netEventReassemblyUnlimitedPendingEvents": KeywordInfo("Unlimited Pending Events", "Allow unlimited pending events", "boolean", "false", "features", valid_values=("true", "false"), usage="sv_netEventReassemblyUnlimitedPendingEvents false"),
        "sv_voiceChat": KeywordInfo("Voice Chat", "Enable built-in voice chat", "boolean", "false", "features", valid_values=("true", "false"), usage="sv_voiceChat false", related=("sv_mumble",)),
        "sv_mumble": KeywordInfo("Mumble Integration", "Enable legacy Mumble API (deprecated)", "boolean", "false", "features", valid_values=("true", "false"), usage="sv_mumble false", related=("sv_voiceChat",), deprecated=True, warning="Deprecated, use sv_voiceChat"),
        "sv_devMode": KeywordInfo("Developer Mode", "Enable dev mode (DO NOT use in production)", "boolean", "false", "features", valid_values=("true", "false"), usage="sv_devMode false", warning="DO NOT use in production"),
        "svgui": KeywordInfo("SVG UI", "Debug GUI toggle", "boolean", "", "features", valid_values=("true", "false"), usage="svgui"),
        "sv_scriptDebugDuplicates": KeywordInfo("Script Debug Duplicates", "Debug duplicate script events", "boolean", "false", "features", valid_values=("true", "false"), usage="sv_scriptDebugDuplicates false"),

        # ═══════════════════════════════════════════════════════════
        # EXPERIMENTAL
        # ═══════════════════════════════════════════════════════════
        "sv_experimentalStateBagsHandler": KeywordInfo("Experimental State Bags", "Faster state bags handler", "boolean", "true", "experimental", valid_values=("true", "false"), usage="sv_experimentalStateBagsHandler true"),
        "sv_experimentalOnesyncPopulation": KeywordInfo("Experimental OneSync Population", "Fix entity ID limit with onesync_population false", "boolean", "true", "experimental", valid_values=("true", "false"), usage="sv_experimentalOnesyncPopulation true"),
        "sv_experimentalNetGameEventHandler": KeywordInfo("Experimental Net Game Event", "Faster game events handler", "boolean", "true", "experimental", valid_values=("true", "false"), usage="sv_experimentalNetGameEventHandler true"),
        "sv_stateBagStrictMode": KeywordInfo("State Bag Strict Mode", "Only server can modify state bags", "boolean", "false", "experimental", valid_values=("true", "false"), usage='setr sv_stateBagStrictMode false'),
        "sv_httpFileServerProxyOnly": KeywordInfo("HTTP File Server Proxy", "Restrict file server to proxy IPs only", "boolean", "false", "experimental", valid_values=("true", "false"), usage="sv_httpFileServerProxyOnly false"),
        "sv_replaceExeToSwitchBuilds": KeywordInfo("Replace Exe To Switch Builds", "Controls how older game builds are run (true=old exe, false=latest exe with DLC)", "boolean", "true", "network", valid_values=("true", "false"), usage="sv_replaceExeToSwitchBuilds true"),
        "sv_showBusySpinnerOnLoadingScreen": KeywordInfo("Show Busy Spinner", "Show busy spinner on loading screen", "boolean", "false", "features", valid_values=("true", "false"), usage="sv_showBusySpinnerOnLoadingScreen false"),
        "sv_endpointurl": KeywordInfo("Endpoint URL", "Custom URL for server endpoint instead of IP", "string", "", "network", usage='sv_endpointurl "https://myserver.example.com"'),
        "sv_kick_players_cnl": KeywordInfo("Kick Players CNL", "Fix Connection CNL timed out error", "boolean", "false", "network", valid_values=("true", "false"), usage="set sv_kick_players_cnl 0"),
        "sv_exposePlayerIdentifiersInHttpEndpoint": KeywordInfo("Expose Player Identifiers", "Retain player identifiers in players.json endpoint", "boolean", "false", "network", valid_values=("true", "false"), usage="sv_exposePlayerIdentifiersInHttpEndpoint false"),
        "txAdmin-menuEnabled": KeywordInfo("TXAdmin Menu Enabled", "Enable txAdmin menu (requires restart)", "boolean", "true", "txadmin", valid_values=("true", "false"), usage="txAdmin-menuEnabled true"),
        "txAdmin-menuAlignRight": KeywordInfo("TXAdmin Menu Align Right", "Align txAdmin menu to right side of screen", "boolean", "false", "txadmin", valid_values=("true", "false"), usage="txAdmin-menuAlignRight false"),
        "txAdmin-menuPageKey": KeywordInfo("TXAdmin Menu Page Key", "Key for changing txAdmin menu pages", "string", "Tab", "txadmin", usage="txAdmin-menuPageKey Tab"),
        "txAdmin-hideDefaultAnnouncement": KeywordInfo("TXAdmin Hide Announcement", "Suppress default announcements", "boolean", "false", "txadmin", valid_values=("true", "false"), usage="txAdmin-hideDefaultAnnouncement false"),
        "txAdmin-hideDefaultDirectMessage": KeywordInfo("TXAdmin Hide DM", "Suppress default direct messages", "boolean", "false", "txadmin", valid_values=("true", "false"), usage="txAdmin-hideDefaultDirectMessage false"),
        "txAdmin-hideDefaultWarning": KeywordInfo("TXAdmin Hide Warning", "Suppress default warnings", "boolean", "false", "txadmin", valid_values=("true", "false"), usage="txAdmin-hideDefaultWarning false"),
        "txAdmin-hideDefaultScheduledRestartWarning": KeywordInfo("TXAdmin Hide Restart Warning", "Suppress restart warnings", "boolean", "false", "txadmin", valid_values=("true", "false"), usage="txAdmin-hideDefaultScheduledRestartWarning false"),
        "txAdmin-debugMode": KeywordInfo("TXAdmin Debug Mode", "Toggle txAdmin debug printing", "boolean", "false", "txadmin", valid_values=("true", "false"), usage="+setr txAdmin-debugMode true"),
        "txAdmin-menuPlayerIdDistance": KeywordInfo("TXAdmin Player ID Distance", "Distance for Player ID visibility in txAdmin menu", "number", "150", "txadmin", min_value="0", max_value="300", usage="+setr txAdmin-menuPlayerIdDistance 100"),
        "txAdmin-menuDrunkDuration": KeywordInfo("TXAdmin Drunk Duration", "Duration of drunk effect in txAdmin menu (seconds)", "number", "0", "txadmin", min_value="0", max_value="300", usage="+setr txAdmin-menuDrunkDuration 120"),

        # ═══════════════════════════════════════════════════════════
        # MONITORING
        # ═══════════════════════════════════════════════════════════
        "sv_prometheusBasicAuthUser": KeywordInfo("Prometheus Auth User", "Prometheus monitoring basic auth user", "string", "", "monitoring", usage='sv_prometheusBasicAuthUser ""'),
        "sv_prometheusBasicAuthPassword": KeywordInfo("Prometheus Auth Password", "Prometheus monitoring basic auth password", "string", "", "monitoring", usage='sv_prometheusBasicAuthPassword ""'),

        # ═══════════════════════════════════════════════════════════
        # STEAM
        # ═══════════════════════════════════════════════════════════
        "steam_webApiKey": KeywordInfo("Steam Web API Key", "Steam Web API key (required for Steam identifiers)", "string", "", "steam", min_length=32, max_length=32, usage='steam_webApiKey "your_key_here"'),
        "steam_webApiDomain": KeywordInfo("Steam Web API Domain", "Steam Web API domain", "string", "api.steampowered.com", "steam", usage='steam_webApiDomain "api.steampowered.com"'),

        # ═══════════════════════════════════════════════════════════
        # MISC
        # ═══════════════════════════════════════════════════════════
        "gamename": KeywordInfo("Game Name", "Game to run (gta5 or rdr3)", "string", "gta5", "misc", valid_values=("gta5", "rdr3"), usage="gamename gta5"),
        "gametype": KeywordInfo("Game Type", "Game type shown in server browser", "string", "", "misc", usage='gametype "Roleplay"'),
        "mapname": KeywordInfo("Map Name", "Map name shown in server browser", "string", "Los Santos", "misc", usage='mapname "Los Santos"'),
        "load_server_icon": KeywordInfo("Load Server Icon", "Load a server icon (96x96 PNG)", "string", "", "misc", usage='load_server_icon "my-server.png"'),
        "exec": KeywordInfo("Execute Config", "Execute another config file", "string", "", "misc", usage="exec server_internal.cfg"),
        "increase_pool_size": KeywordInfo("Increase Pool Size", "Increase streaming asset pool size", "string", "", "misc", params=(ParamInfo("pool_name", "str", True, description="Pool name (TxdStore, CMoveObject, etc.)"), ParamInfo("increase", "int", True, description="Amount to increase")), usage='increase_pool_size "TxdStore" 6000'),
        # ═══════════════════════════════════════════════════════════
        # RATE LIMITER (each has _rate and _burst)
        # ═══════════════════════════════════════════════════════════
        "rateLimiter_challenge_rate": KeywordInfo("Challenge Rate", "Rate limit for client authentication challenge", "number", "4", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_challenge_rate 4", related=("rateLimiter_challenge_burst",)),
        "rateLimiter_challenge_burst": KeywordInfo("Challenge Burst", "Burst limit for client authentication challenge", "number", "10", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_challenge_burst 10", related=("rateLimiter_challenge_rate",)),
        "rateLimiter_handshake_rate": KeywordInfo("Handshake Rate", "Rate limit for TCP connection handshake", "number", "4", "ratelimiter", min_value="0", max_value="1000", usage="rateLimiter_handshake_rate 4", related=("rateLimiter_handshake_burst",)),
        "rateLimiter_handshake_burst": KeywordInfo("Handshake Burst", "Burst limit for TCP connection handshake", "number", "10", "ratelimiter", min_value="0", max_value="1000", usage="rateLimiter_handshake_burst 10", related=("rateLimiter_handshake_rate",)),
        "rateLimiter_handshakeUDP_rate": KeywordInfo("Handshake UDP Rate", "Rate limit for UDP connection handshake", "number", "1", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_handshakeUDP_rate 1", related=("rateLimiter_handshakeUDP_burst",)),
        "rateLimiter_handshakeUDP_burst": KeywordInfo("Handshake UDP Burst", "Burst limit for UDP connection handshake", "number", "5", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_handshakeUDP_burst 5", related=("rateLimiter_handshakeUDP_rate",)),
        "rateLimiter_http_dynamic_rate": KeywordInfo("HTTP Dynamic Rate", "Rate limit for dynamic HTTP endpoints", "number", "4", "ratelimiter", min_value="0", max_value="1000", usage="rateLimiter_http_dynamic_rate 4", related=("rateLimiter_http_dynamic_burst",)),
        "rateLimiter_http_dynamic_burst": KeywordInfo("HTTP Dynamic Burst", "Burst limit for dynamic HTTP endpoints", "number", "10", "ratelimiter", min_value="0", max_value="1000", usage="rateLimiter_http_dynamic_burst 10", related=("rateLimiter_http_dynamic_rate",)),
        "rateLimiter_http_info_rate": KeywordInfo("HTTP Info Rate", "Rate limit for server info endpoint", "number", "4", "ratelimiter", min_value="0", max_value="1000", usage="rateLimiter_http_info_rate 4", related=("rateLimiter_http_info_burst",)),
        "rateLimiter_http_info_burst": KeywordInfo("HTTP Info Burst", "Burst limit for server info endpoint", "number", "10", "ratelimiter", min_value="0", max_value="1000", usage="rateLimiter_http_info_burst 10", related=("rateLimiter_http_info_rate",)),
        "rateLimiter_http_perf_rate": KeywordInfo("HTTP Perf Rate", "Rate limit for performance endpoint", "number", "2", "ratelimiter", min_value="0", max_value="100", usage="rateLimiter_http_perf_rate 2", related=("rateLimiter_http_perf_burst",)),
        "rateLimiter_http_perf_burst": KeywordInfo("HTTP Perf Burst", "Burst limit for performance endpoint", "number", "5", "ratelimiter", min_value="0", max_value="100", usage="rateLimiter_http_perf_burst 5", related=("rateLimiter_http_perf_rate",)),
        "rateLimiter_http_players_rate": KeywordInfo("HTTP Players Rate", "Rate limit for player list endpoint", "number", "4", "ratelimiter", min_value="0", max_value="100", usage="rateLimiter_http_players_rate 4", related=("rateLimiter_http_players_burst",)),
        "rateLimiter_http_players_burst": KeywordInfo("HTTP Players Burst", "Burst limit for player list endpoint", "number", "10", "ratelimiter", min_value="0", max_value="100", usage="rateLimiter_http_players_burst 10", related=("rateLimiter_http_players_rate",)),
        "rateLimiter_netCommand_rate": KeywordInfo("Net Command Rate", "Rate limit for client commands", "number", "7", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_netCommand_rate 7", related=("rateLimiter_netCommand_burst",)),
        "rateLimiter_netCommand_burst": KeywordInfo("Net Command Burst", "Burst limit for client commands", "number", "14", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_netCommand_burst 14", related=("rateLimiter_netCommand_rate",)),
        "rateLimiter_netCommandFlood_rate": KeywordInfo("Net Command Flood Rate", "Rate limit for command flood protection", "number", "25", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_netCommandFlood_rate 25", related=("rateLimiter_netCommandFlood_burst",)),
        "rateLimiter_netCommandFlood_burst": KeywordInfo("Net Command Flood Burst", "Burst limit for command flood protection", "number", "45", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_netCommandFlood_burst 45", related=("rateLimiter_netCommandFlood_rate",)),
        "rateLimiter_netCommandSize_rate": KeywordInfo("Net Command Size Rate", "Rate limit for command payload size", "number", "1024", "ratelimiter", min_value="0", max_value="100000", usage="rateLimiter_netCommandSize_rate 1024", related=("rateLimiter_netCommandSize_burst",)),
        "rateLimiter_netCommandSize_burst": KeywordInfo("Net Command Size Burst", "Burst limit for command payload size", "number", "8192", "ratelimiter", min_value="0", max_value="100000", usage="rateLimiter_netCommandSize_burst 8192", related=("rateLimiter_netCommandSize_rate",)),
        "rateLimiter_netEvent_rate": KeywordInfo("Net Event Rate", "Rate limit for game events", "number", "50", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_netEvent_rate 50", related=("rateLimiter_netEvent_burst",)),
        "rateLimiter_netEvent_burst": KeywordInfo("Net Event Burst", "Burst limit for game events", "number", "200", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_netEvent_burst 200", related=("rateLimiter_netEvent_rate",)),
        "rateLimiter_netEventFlood_rate": KeywordInfo("Net Event Flood Rate", "Rate limit for event flood protection", "number", "75", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_netEventFlood_rate 75", related=("rateLimiter_netEventFlood_burst",)),
        "rateLimiter_netEventFlood_burst": KeywordInfo("Net Event Flood Burst", "Burst limit for event flood protection", "number", "300", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_netEventFlood_burst 300", related=("rateLimiter_netEventFlood_rate",)),
        "rateLimiter_rcon_rate": KeywordInfo("RCON Rate", "Rate limit for remote console", "number", "2", "ratelimiter", min_value="0", max_value="100", usage="rateLimiter_rcon_rate 2", related=("rateLimiter_rcon_burst",)),
        "rateLimiter_rcon_burst": KeywordInfo("RCON Burst", "Burst limit for remote console", "number", "5", "ratelimiter", min_value="0", max_value="100", usage="rateLimiter_rcon_burst 5", related=("rateLimiter_rcon_rate",)),
        "rateLimiter_res_http_handler_rate": KeywordInfo("Resource HTTP Rate", "Rate limit for resource HTTP endpoints", "number", "10", "ratelimiter", min_value="0", max_value="1000", usage="rateLimiter_res_http_handler_rate 10", related=("rateLimiter_res_http_handler_burst",)),
        "rateLimiter_res_http_handler_burst": KeywordInfo("Resource HTTP Burst", "Burst limit for resource HTTP endpoints", "number", "25", "ratelimiter", min_value="0", max_value="1000", usage="rateLimiter_res_http_handler_burst 25", related=("rateLimiter_res_http_handler_rate",)),
        "rateLimiter_resourceList_rate": KeywordInfo("Resource List Rate", "Rate limit for resource listing", "number", "10", "ratelimiter", min_value="0", max_value="100", usage="rateLimiter_resourceList_rate 10", related=("rateLimiter_resourceList_burst",)),
        "rateLimiter_resourceList_burst": KeywordInfo("Resource List Burst", "Burst limit for resource listing", "number", "25", "ratelimiter", min_value="0", max_value="100", usage="rateLimiter_resourceList_burst 25", related=("rateLimiter_resourceList_rate",)),
        "rateLimiter_stateBag_rate": KeywordInfo("State Bag Rate", "Rate limit for state bag updates", "number", "75", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_stateBag_rate 75", related=("rateLimiter_stateBag_burst",)),
        "rateLimiter_stateBag_burst": KeywordInfo("State Bag Burst", "Burst limit for state bag updates", "number", "125", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_stateBag_burst 125", related=("rateLimiter_stateBag_rate",)),
        "rateLimiter_stateBagFlood_rate": KeywordInfo("State Bag Flood Rate", "Rate limit for state bag flood protection", "number", "150", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_stateBagFlood_rate 150", related=("rateLimiter_stateBagFlood_burst",)),
        "rateLimiter_stateBagFlood_burst": KeywordInfo("State Bag Flood Burst", "Burst limit for state bag flood protection", "number", "175", "ratelimiter", min_value="0", max_value="10000", usage="rateLimiter_stateBagFlood_burst 175", related=("rateLimiter_stateBagFlood_rate",)),
        "rateLimiter_stateBagSize_rate": KeywordInfo("State Bag Size Rate", "Rate limit for state bag payload size", "number", "131072", "ratelimiter", min_value="0", max_value="10000000", usage="rateLimiter_stateBagSize_rate 131072", related=("rateLimiter_stateBagSize_burst",)),
        "rateLimiter_stateBagSize_burst": KeywordInfo("State Bag Size Burst", "Burst limit for state bag payload size", "number", "262144", "ratelimiter", min_value="0", max_value="10000000", usage="rateLimiter_stateBagSize_burst 262144", related=("rateLimiter_stateBagSize_rate",)),
        # ═══════════════════════════════════════════════════════════
        # ACTIONS (console commands)
        # ═══════════════════════════════════════════════════════════
        "ensure": KeywordInfo("Ensure Resource", "Start resource and keep it running (restarts if stopped)", "action", "", "action", params=(ParamInfo("resource", "str", True, description="Resource folder name"),), usage="ensure mapmanager", related=("ensure_stop", "start", "stop")),
        "ensure_stop": KeywordInfo("Stop Ensured", "Stop an ensured resource", "action", "", "action", params=(ParamInfo("resource", "str", True, description="Resource folder name"),), usage="ensure_stop mapmanager", related=("ensure",)),
        "quit": KeywordInfo("Quit Server", "Shut down the server with optional reason", "action", "", "action", params=(ParamInfo("reason", "str", False, description="Shutdown reason"),), usage='quit "Restarting - will be back soon!"', related=("restart",)),
        "refresh": KeywordInfo("Refresh Resources", "Refresh resources folder", "action", "", "action", usage="refresh", related=("start", "stop")),
        "restart": KeywordInfo("Restart Server", "Restart the server", "action", "", "action", usage="restart", related=("quit",)),
        "say": KeywordInfo("Say Message", "Send a chat message as console", "action", "", "action", params=(ParamInfo("message", "str", True, description="Message to send"),), usage='say "Hello everyone!"'),
        "status": KeywordInfo("Status", "Show connected players with IDs and ping (provided by rconlog)", "action", "", "action", usage="status"),
        "clientkick": KeywordInfo("Client Kick", "Kick a client by server ID (provided by rconlog)", "action", "", "action", params=(ParamInfo("id", "int", True, description="Server ID"), ParamInfo("reason", "str", False, description="Kick reason")), usage="clientkick 43 You're a superstitious idiot!"),
        "moo": KeywordInfo("Moo", "Set to 31337 to bypass pool size validation for local dev", "boolean", "0", "experimental", valid_values=("0", "31337"), usage="set moo 31337", warning="Development only, never use in production"),
        "start": KeywordInfo("Start Resource", "Start a resource", "action", "", "action", params=(ParamInfo("resource", "str", True, description="Resource folder name"),), usage="start mapmanager", related=("stop", "ensure")),
        "stop": KeywordInfo("Stop Resource", "Stop a running resource", "action", "", "action", params=(ParamInfo("resource", "str", True, description="Resource folder name"),), usage="stop mapmanager", related=("start", "ensure")),
        # ═══════════════════════════════════════════════════════════
        # COMMANDS
        # ═══════════════════════════════════════════════════════════
        "set": KeywordInfo("Set Convar", "Set a server-only convar (NOT sent to clients, safe for secrets)", "command", "", "command", params=(ParamInfo("name", "str", True, description="Convar name"), ParamInfo("value", "str", True, description="Convar value")), usage='set mysql_connection_string "mysql://user:pass@host/db"', related=("setr", "sets"), warning="NOT sent to clients, safe for secrets"),
        "setr": KeywordInfo("Set Replicated", "Set a replicated convar (sent to ALL clients)", "command", "", "command", params=(ParamInfo("name", "str", True, description="Convar name"), ParamInfo("value", "str", True, description="Convar value")), usage="setr myscript_debug true", related=("set", "sets"), warning="Sent to ALL clients, NOT for secrets!"),
        "sets": KeywordInfo("Set Saved", "Set a server-info convar (PUBLIC, shown in browser)", "command", "", "command", params=(ParamInfo("name", "str", True, description="Convar name"), ParamInfo("value", "str", True, description="Convar value")), usage='sets sv_projectName "My FXServer Project"', related=("set", "setr"), warning="PUBLIC, shown in server browser"),
        "add_ace": KeywordInfo("Add ACE Permission", "Add an ACE permission to a principal", "command", "", "command", params=(ParamInfo("principal", "str", True, description="Principal to grant permission to"), ParamInfo("object", "str", True, description="Permission object name"), ParamInfo("permission", "str", True, "allow", "allow or deny")), usage="add_ace group.admin command allow", related=("remove_ace", "add_principal")),
        "add_principal": KeywordInfo("Add Principal", "Add a child principal to a parent principal", "command", "", "command", params=(ParamInfo("child", "str", True, description="Child principal (player or group)"), ParamInfo("parent", "str", True, description="Parent principal (group)")), usage="add_principal identifier.license:abc123 group.admin", related=("remove_principal",)),
        "remove_ace": KeywordInfo("Remove ACE Permission", "Remove an ACE permission from a principal", "command", "", "command", params=(ParamInfo("principal", "str", True, description="Principal to remove permission from"), ParamInfo("object", "str", True, description="Permission object name")), usage="remove_ace group.admin command", related=("add_ace",)),
        "remove_principal": KeywordInfo("Remove Principal", "Remove a child principal from a parent principal", "command", "", "command", params=(ParamInfo("child", "str", True, description="Child principal"), ParamInfo("parent", "str", True, description="Parent principal")), usage="remove_principal identifier.license:abc123 group.admin", related=("add_principal",)),
        "block_net_game_event": KeywordInfo("Block Net Game Event", "Block a net game event (anti-cheat)", "command", "", "command", params=(ParamInfo("event_name", "str", True, description="Event name to block")), usage='block_net_game_event "FIRE_EVENT"', related=("unblock_net_game_event",)),
        "unblock_net_game_event": KeywordInfo("Unblock Net Game Event", "Unblock a previously blocked net game event", "command", "", "command", params=(ParamInfo("event_name", "str", True, description="Event name to unblock")), usage='unblock_net_game_event "FIRE_EVENT"', related=("block_net_game_event",)),
        "test_ace": KeywordInfo("Test ACE", "Test if a principal has a specific ACE permission", "command", "", "command", params=(ParamInfo("principal", "str", True, description="Principal to test"), ParamInfo("object", "str", True, description="Permission object")), usage="test_ace group.admin command", related=("add_ace",)),
        "replay_start": KeywordInfo("Start Replay", "Start recording a replay (Enhanced only)", "command", "", "command", params=(ParamInfo("file_name", "str", True, description="File name"), ParamInfo("mode", "str", True, description="Recording mode")), usage="replay_start fileName mode", related=("replay_stop",)),
        "replay_stop": KeywordInfo("Stop Replay", "Stop recording a replay (Enhanced only)", "command", "", "command", params=(ParamInfo("replay_id", "str", True, description="Replay ID")), usage="replay_stop replayId", related=("replay_start",)),
        "sync_start_recording": KeywordInfo("Start Sync Recording", "Start synchronized recording", "command", "", "command", params=(ParamInfo("net_id", "str", True, description="Network ID"), ParamInfo("compressed", "str", False, description="Compress recording")), usage="sync_start_recording netId compressed", related=("sync_stop_recording",)),
        "sync_stop_recording": KeywordInfo("Stop Sync Recording", "Stop synchronized recording", "command", "", "command", params=(ParamInfo("net_id", "str", True, description="Network ID")), usage="sync_stop_recording netId", related=("sync_start_recording",)),
        "con_channelFilters": KeywordInfo("Set Channel Filters", "Set console channel filter masks", "command", "", "command", usage="con_channelFilters value"),
        "con_addChannelFilter": KeywordInfo("Add Channel Filter", "Add a console channel filter", "command", "", "command", params=(ParamInfo("filter", "str", True, description="Filter value"), ParamInfo("action", "str", True, description="Action")), usage="con_addChannelFilter filter action", related=("con_removeChannelFilter",)),
        "con_removeChannelFilter": KeywordInfo("Remove Channel Filter", "Remove a console channel filter", "command", "", "command", params=(ParamInfo("filter", "str", True, description="Filter value"), ParamInfo("action", "str", True, description="Action")), usage="con_removeChannelFilter filter action", related=("con_addChannelFilter",)),
        "endpoint_add_tcp": KeywordInfo("Add TCP Endpoint", "Add a TCP endpoint for client connections", "command", "", "command", params=(ParamInfo("endpoint", "str", True, description="Endpoint in ip:port format")), usage='endpoint_add_tcp "0.0.0.0:30120"', related=("endpoint_add_udp",)),
        "endpoint_add_udp": KeywordInfo("Add UDP Endpoint", "Add a UDP endpoint for game traffic", "command", "", "command", params=(ParamInfo("endpoint", "str", True, description="Endpoint in ip:port format")), usage='endpoint_add_udp "0.0.0.0:30120"', related=("endpoint_add_tcp",)),
        # ═══════════════════════════════════════════════════════════
        # PRINCIPALS
        # ═══════════════════════════════════════════════════════════
        "builtin.everyone": KeywordInfo("Everyone", "All players (built-in)", "principal", "", "principal", usage="add_ace builtin.everyone command allow"),
        "builtin.restricted": KeywordInfo("Restricted", "Restricted players (built-in)", "principal", "", "principal", usage="add_ace builtin.restricted command allow"),
        "group.admin": KeywordInfo("Admin Group", "Administrators group", "principal", "", "principal", related=("group.moderator", "group.owner", "group.superadmin")),
        "group.moderator": KeywordInfo("Moderator Group", "Moderators group", "principal", "", "principal", related=("group.admin",)),
        "group.owner": KeywordInfo("Owner Group", "Server owner group", "principal", "", "principal", related=("group.admin",)),
        "group.user": KeywordInfo("User Group", "Regular users group", "principal", "", "principal"),
        "group.support": KeywordInfo("Support Group", "Support staff group", "principal", "", "principal"),
        "group.helper": KeywordInfo("Helper Group", "Helpers group", "principal", "", "principal"),
        "group.god": KeywordInfo("God Group", "God-level permissions group", "principal", "", "principal"),
        "group.superadmin": KeywordInfo("Superadmin Group", "Super administrators group", "principal", "", "principal", related=("group.admin",)),
        "group.developer": KeywordInfo("Developer Group", "Developers group", "principal", "", "principal"),
        "identifier.steam": KeywordInfo("Steam Identifier", "Steam platform identifier", "principal", "", "principal", usage="add_principal identifier.license:abc123 group.admin"),
        "identifier.license": KeywordInfo("License Identifier", "FiveM license identifier", "principal", "", "principal", usage="add_principal identifier.license:abc123 group.admin"),
        "identifier.discord": KeywordInfo("Discord Identifier", "Discord identifier", "principal", "", "principal", usage="add_principal identifier.discord:123456789012345678 group.admin"),
        "identifier.fivem": KeywordInfo("FiveM Identifier", "FiveM platform identifier", "principal", "", "principal"),
        "identifier.ip": KeywordInfo("IP Identifier", "IP address identifier", "principal", "", "principal"),
        "identifier.xbl": KeywordInfo("Xbox Live Identifier", "Xbox Live identifier", "principal", "", "principal"),
        "resource.mapmanager": KeywordInfo("Map Manager", "mapmanager resource principal", "principal", "", "principal"),
        "resource.chat": KeywordInfo("Chat Resource", "chat resource principal", "principal", "", "principal"),
        "resource.spawnmanager": KeywordInfo("Spawn Manager", "spawnmanager resource principal", "principal", "", "principal"),
        "resource.sessionmanager": KeywordInfo("Session Manager", "sessionmanager resource principal", "principal", "", "principal"),
        "resource.hardcap": KeywordInfo("Hardcap", "hardcap resource principal", "principal", "", "principal"),
        "resource.rconlog": KeywordInfo("RCON Log", "rconlog resource principal", "principal", "", "principal"),
        "resource.baseevents": KeywordInfo("Base Events", "baseevents resource principal", "principal", "", "principal"),
        "command": KeywordInfo("Command Base", "All commands permission", "principal", "", "principal", related=("command.kick", "command.ban")),
        "command.kick": KeywordInfo("Kick Command", "Kick players permission", "principal", "", "principal", related=("command.ban",)),
        "command.ban": KeywordInfo("Ban Command", "Ban players permission", "principal", "", "principal", related=("command.kick",)),
        "command.tempban": KeywordInfo("Tempban Command", "Temporarily ban players permission", "principal", "", "principal", related=("command.ban",)),
        "command.setgroup": KeywordInfo("Setgroup Command", "Set player groups permission", "principal", "", "principal"),
        "command.admin": KeywordInfo("Admin Command", "Admin commands permission", "principal", "", "principal"),
        "command.noclip": KeywordInfo("Noclip Command", "Toggle noclip permission", "principal", "", "principal"),
        "command.tpm": KeywordInfo("TPM Command", "Teleport to marker permission", "principal", "", "principal"),
        "command.bring": KeywordInfo("Bring Command", "Bring player to you permission", "principal", "", "principal"),
        "command.revive": KeywordInfo("Revive Command", "Revive player permission", "principal", "", "principal"),
        "command.heal": KeywordInfo("Heal Command", "Heal player permission", "principal", "", "principal"),
        "command.announce": KeywordInfo("Announce Command", "Server announcements permission", "principal", "", "principal"),
        "command.car": KeywordInfo("Car Command", "Spawn vehicles permission", "principal", "", "principal"),
        "command.weather": KeywordInfo("Weather Command", "Change weather permission", "principal", "", "principal"),
        "command.time": KeywordInfo("Time Command", "Change time permission", "principal", "", "principal"),
        "command.quit": KeywordInfo("Quit Command", "Quit the server permission", "principal", "", "principal"),
        "command.add_ace": KeywordInfo("Add ACE Command", "add_ace command permission", "principal", "", "principal"),
        "command.add_principal": KeywordInfo("Add Principal Command", "add_principal command permission", "principal", "", "principal"),
        "txAdmin.kick": KeywordInfo("TXAdmin Kick", "txAdmin kick permission", "principal", "", "principal"),
        "txAdmin.ban": KeywordInfo("TXAdmin Ban", "txAdmin ban permission", "principal", "", "principal"),
        "txAdmin.warn": KeywordInfo("TXAdmin Warn", "txAdmin warn permission", "principal", "", "principal"),
        "txAdmin.players.heal": KeywordInfo("TXAdmin Heal", "txAdmin heal permission", "principal", "", "principal"),
        "qbcore.admin": KeywordInfo("QBCore Admin", "QBCore admin permissions", "principal", "", "principal"),
        "qbx.admin": KeywordInfo("QBx Admin", "QBx admin permissions", "principal", "", "principal"),
        "esx.admin": KeywordInfo("ESX Admin", "ESX admin permissions", "principal", "", "principal"),
        "mapmanager": KeywordInfo("Map Manager (bare)", "mapmanager bare permission", "principal", "", "principal"),
        "chat": KeywordInfo("Chat (bare)", "chat bare permission", "principal", "", "principal"),
        "spawnmanager": KeywordInfo("Spawn Manager (bare)", "spawnmanager bare permission", "principal", "", "principal"),
        "sessionmanager": KeywordInfo("Session Manager (bare)", "sessionmanager bare permission", "principal", "", "principal"),
        "basic-gamemode": KeywordInfo("Basic Gamemode", "basic-gamemode bare permission", "principal", "", "principal"),
        "hardcap": KeywordInfo("Hardcap (bare)", "hardcap bare permission", "principal", "", "principal"),
        "rconlog": KeywordInfo("RCON Log (bare)", "rconlog bare permission", "principal", "", "principal"),
        "baseevents": KeywordInfo("Base Events (bare)", "baseevents bare permission", "principal", "", "principal"),
        # ═══════════════════════════════════════════════════════════
        # STATES
        # ═══════════════════════════════════════════════════════════
        "allow": KeywordInfo("Allow", "Grant permission", "state", "", "state", usage="add_ace group.admin command allow", related=("deny",)),
        "deny": KeywordInfo("Deny", "Deny permission", "state", "", "state", usage="add_ace group.user command deny", related=("allow",)),
        "deny_socket": KeywordInfo("Deny Socket", "Deny socket access", "state", "", "state", usage="add_ace group.user endpoint deny_socket"),
        "true": KeywordInfo("True", "Boolean true value", "state", "", "state", related=("false",)),
        "false": KeywordInfo("False", "Boolean false value", "state", "", "state", related=("true",)),
        "on": KeywordInfo("On", "Enable feature", "state", "", "state", related=("off",)),
        "off": KeywordInfo("Off", "Disable feature", "state", "", "state", related=("on",)),
    }


# ═══════════════════════════════════════════════════════════════════════════
# LOOKUP FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def get_identifier(identifier: str | None, /) -> str | None:
    return str(identifier) if identifier else None


def is_valid_keyword(token: str, /) -> bool:
    return token in _G.ALL


def is_valid_cvar(token: str, /) -> bool:
    return token in _G.CVARS


def is_valid_action(token: str, /) -> bool:
    return token in _G.ACTIONS


def is_valid_principal(token: str, /) -> bool:
    return token in _G.PRINCIPALS


def is_valid_state(token: str, /) -> bool:
    return token in _G.STATES


def get_token_type(token: str, /) -> str | None:
    if token in _G.CVARS:
        return "cvar"
    if token in _G.ACTIONS:
        return "action"
    if token in _G.PRINCIPALS:
        return "principal"
    if token in _G.STATES:
        return "state"
    return None


def get_token_prefix(token: str, /) -> str | None:
    for prefix, name in _G._PREFIXES.items():
        if token.startswith(prefix):
            return name
    return None


def get_keyword_info(token: str, /) -> KeywordInfo | None:
    return _G.META.get(token)


def get_keyword_name(token: str, /) -> str:
    info = _G.META.get(token)
    return info.name if info else token


def get_keyword_desc(token: str, /) -> str:
    info = _G.META.get(token)
    return info.description if info else ""


def get_keyword_type(token: str, /) -> str:
    info = _G.META.get(token)
    return info.value_type if info else "string"


def get_keyword_default(token: str, /) -> str:
    info = _G.META.get(token)
    return info.default if info else ""


def get_keyword_category(token: str, /) -> str:
    info = _G.META.get(token)
    return info.category if info else ""


def get_keyword_params(token: str, /) -> tuple[ParamInfo, ...]:
    info = _G.META.get(token)
    return info.params if info else ()


def get_keyword_usage(token: str, /) -> str:
    info = _G.META.get(token)
    return info.usage if info else ""


def get_keyword_related(token: str, /) -> tuple[str, ...]:
    info = _G.META.get(token)
    return info.related if info else ()


def get_keyword_warning(token: str, /) -> str:
    info = _G.META.get(token)
    return info.warning if info else ""


def is_deprecated(token: str, /) -> bool:
    info = _G.META.get(token)
    return info.deprecated if info else False


def is_startup_only(token: str, /) -> bool:
    info = _G.META.get(token)
    return info.startup_only if info else False


def find_by_category(category: str, /) -> frozenset[str]:
    return frozenset(k for k, v in _G.META.items() if v.category == category)


def find_by_value_type(value_type: str, /) -> frozenset[str]:
    return frozenset(k for k, v in _G.META.items() if v.value_type == value_type)


def find_by_name(name: str, /) -> list[str]:
    lower = name.lower()
    return sorted(k for k, v in _G.META.items() if lower in v.name.lower())


def find_deprecated() -> frozenset[str]:
    return frozenset(k for k, v in _G.META.items() if v.deprecated)


def find_startup_only() -> frozenset[str]:
    return frozenset(k for k, v in _G.META.items() if v.startup_only)


def find_with_warnings() -> dict[str, str]:
    return {k: v.warning for k, v in _G.META.items() if v.warning}


def search_keywords(query: str, /) -> list[str]:
    lower = query.lower()
    return sorted(k for k, v in _G.META.items()
                  if lower in k.lower() or lower in v.name.lower() or lower in v.description.lower())


def get_all_categories() -> frozenset[str]:
    return frozenset(v.category for v in _G.META.values() if v.category)


def get_category_stats() -> dict[str, int]:
    stats: dict[str, int] = {}
    for info in _G.META.values():
        if info.category:
            stats[info.category] = stats.get(info.category, 0) + 1
    return dict(sorted(stats.items()))


def get_value_type_stats() -> dict[str, int]:
    stats: dict[str, int] = {}
    for info in _G.META.values():
        stats[info.value_type] = stats.get(info.value_type, 0) + 1
    return dict(sorted(stats.items()))


# ═══════════════════════════════════════════════════════════════════════════
# IDENTIFIER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

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


def make_steam_id(steam64: str, /) -> str:
    return f"identifier.steam:{steam64}"


def make_license_id(license: str, /) -> str:
    return f"identifier.license:{license}"


def make_discord_id(discord_id: str, /) -> str:
    return f"identifier.discord:{discord_id}"


def make_fivem_id(fivem_id: str, /) -> str:
    return f"identifier.fivem:{fivem_id}"


def make_ip_id(ip: str, /) -> str:
    return f"identifier.ip:{ip}"


def make_xbl_id(xbl_id: str, /) -> str:
    return f"identifier.xbl:{xbl_id}"


# ═══════════════════════════════════════════════════════════════════════════
# FILTER / GROUP FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def get_sv_convars() -> frozenset[str]:
    return frozenset(c for c in _G.CVARS if c.startswith("sv_"))


def get_onesync_convars() -> frozenset[str]:
    return frozenset(c for c in _G.CVARS if c.startswith("onesync_"))


def get_ratelimiter_convars() -> frozenset[str]:
    return frozenset(c for c in _G.CVARS if c.startswith("rateLimiter_"))


def get_ratelimiter_pairs() -> list[tuple[str, str]]:
    pairs = []
    for cvar in _G.CVARS:
        if cvar.startswith("rateLimiter_") and cvar.endswith("_rate"):
            burst = cvar.replace("_rate", "_burst")
            if burst in _G.CVARS:
                pairs.append((cvar, burst))
    return sorted(pairs)


def get_group_principals() -> frozenset[str]:
    return frozenset(p for p in _G.PRINCIPALS if p.startswith("group."))


def get_identifier_principals() -> frozenset[str]:
    return frozenset(p for p in _G.PRINCIPALS if p.startswith("identifier."))


def get_resource_principals() -> frozenset[str]:
    return frozenset(p for p in _G.PRINCIPALS if p.startswith("resource.") or p in {
        "mapmanager", "chat", "spawnmanager", "sessionmanager",
        "basic-gamemode", "hardcap", "rconlog", "baseevents",
    })


def get_command_permissions() -> frozenset[str]:
    return frozenset(p for p in _G.PRINCIPALS if p.startswith("command."))


def get_txadmin_permissions() -> frozenset[str]:
    return frozenset(p for p in _G.PRINCIPALS if p.startswith("txAdmin."))


def get_framework_permissions() -> frozenset[str]:
    return frozenset(p for p in _G.PRINCIPALS if p.startswith(("qbcore.", "qbx.", "esx.")))


def validate_convar_value(cvar: str, value: str, /) -> bool:
    validators: dict[str, frozenset[str]] = {
        "sv_entityLockdown": frozenset({"full", "strict", "relaxed", "inactive"}),
        "sv_pureLevel": frozenset({"0", "1", "2"}),
        "sv_requestParanoia": frozenset({"0", "1", "2", "3"}),
        "onesync": frozenset({"on", "off", "legacy"}),
        "sv_scriptHookAllowed": frozenset({"0", "1"}),
    }
    allowed = validators.get(cvar)
    if allowed is not None:
        return value in allowed
    if cvar == "sv_enforceGameBuild":
        return value.isdigit()
    return True


def get_keyword_suggestions(prefix: str, /) -> list[str]:
    keywords = sorted(_G.ALL)
    if not prefix:
        return keywords
    return [k for k in keywords if k.startswith(prefix)]


# ═══════════════════════════════════════════════════════════════════════════
# PARSING / FORMATTING
# ═══════════════════════════════════════════════════════════════════════════

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
    return frozenset(k for k in _G.ALL if k.startswith(prefix))


def find_by_suffix(suffix: str, /) -> frozenset[str]:
    return frozenset(k for k in _G.ALL if k.endswith(suffix))


def find_by_pattern(pattern: str, /) -> list[str]:
    return sorted(k for k in _G.ALL if pattern in k)


def get_related(token: str, /) -> frozenset[str]:
    prefix = get_token_prefix(token)
    if prefix:
        return frozenset(k for k in _G.ALL if k.startswith(prefix + "_") or k.startswith(prefix + "."))
    if "." in token:
        base = token.split(".")[0]
        return frozenset(k for k in _G.ALL if k.startswith(base + "."))
    return frozenset()


def get_rate_pair(cvar: str, /) -> tuple[str, str] | None:
    if cvar.endswith("_rate"):
        burst = cvar.replace("_rate", "_burst")
        if burst in _G.CVARS:
            return (cvar, burst)
    if cvar.endswith("_burst"):
        rate = cvar.replace("_burst", "_rate")
        if rate in _G.CVARS:
            return (rate, cvar)
    return None


def get_enabled_only() -> frozenset[str]:
    return frozenset(k for k in _G.CVARS if k in {
        "sv_lan", "sv_voiceChat", "sv_devMode", "sv_mumble",
        "sv_endpointPrivacy", "sv_useAccurateSends", "sv_registerMulticastDns",
        "sv_enableNetworkedSounds", "sv_enableNetworkedPhoneExplosions",
        "sv_enableNetworkedScriptEntityStates", "sv_enableNetEventReassembly",
        "sv_netEventReassemblyUnlimitedPendingEvents", "sv_forceIndirectListing",
        "sv_httpFileServerProxyOnly", "sv_stateBagStrictMode",
        "sv_scriptHookAllowed", "sv_scriptDebugDuplicates",
        "onesync_enableInfinity", "onesync_population", "onesync_forceMigration",
        "onesync_distanceCulling", "onesync_distanceCullVehicles", "onesync_radiusFrequency",
    })


def get_numeric_only() -> frozenset[str]:
    return frozenset(k for k in _G.CVARS if k in {
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
    return frozenset(k for k in _G.CVARS if k in {
        "sv_hostname", "sv_licenseKey", "sv_master1", "sv_tebexSecret",
        "steam_webApiKey", "steam_webApiDomain", "sv_listingIpOverride",
        "sv_listingHostOverride", "sv_endpoints", "sv_proxyIPRanges",
        "sv_kvsName", "sv_prometheusBasicAuthPassword", "sv_projectName",
        "sv_projectDesc", "sv_allowlistInstructions", "rcon_password",
        "gametype", "gamename", "mapname", "load_server_icon",
    })


# ═══════════════════════════════════════════════════════════════════════════
# BUILDER FUNCTIONS — generate cfg lines for every keyword
# Function names match the actual FiveM keyword names
# int → str, bool → "true"/"false" or "allow"/"deny", str → str
# ═══════════════════════════════════════════════════════════════════════════

def _set(name: str, value: str, /, *, use_set: bool = True) -> str:
    if use_set:
        return build_line("set", name, format_value(value))
    return build_line(name, format_value(value))


def _setr(name: str, value: str, /, *, use_set: bool = True) -> str:
    if use_set:
        return build_line("setr", name, format_value(value))
    return build_line(name, format_value(value))


def _sets(name: str, value: str, /, *, use_set: bool = True) -> str:
    if use_set:
        return build_line("sets", name, format_value(value))
    return build_line(name, format_value(value))


# ── Access Control Commands ──

def add_ace(principal: str, obj: str, perm: str = "allow", /) -> str:
    return build_line("add_ace", principal, obj, perm)


def remove_ace(principal: str, obj: str, /) -> str:
    return build_line("remove_ace", principal, obj)


def add_principal(child: str, parent: str, /) -> str:
    return build_line("add_principal", child, parent)


def remove_principal(child: str, parent: str, /) -> str:
    return build_line("remove_principal", child, parent)


def test_ace(principal: str, obj: str, /) -> str:
    return build_line("test_ace", principal, obj)


def block_net_game_event(event: str, /) -> str:
    return build_line("block_net_game_event", format_value(event))


def unblock_net_game_event(event: str, /) -> str:
    return build_line("unblock_net_game_event", format_value(event))


# ── Resource Commands ──

def ensure(resource: str, /) -> str:
    return build_line("ensure", resource)


def ensure_stop(resource: str, /) -> str:
    return build_line("ensure_stop", resource)


def start(resource: str, /) -> str:
    return build_line("start", resource)


def stop(resource: str, /) -> str:
    return build_line("stop", resource)


def restart(resource: str, /) -> str:
    return build_line("restart", resource)


def quit(reason: str = "", /) -> str:
    return build_line("quit", format_value(reason)) if reason else "quit"


def refresh() -> str:
    return "refresh"


def say(message: str, /) -> str:
    return build_line("say", format_value(message))


def exec(path: str, /) -> str:
    return build_line("exec", path)


def status() -> str:
    return "status"


def clientkick(player_id: int, reason: str = "", /) -> str:
    args = [str(player_id)]
    if reason:
        args.append(format_value(reason))
    return build_line("clientkick", *args)


def moo(value: int = 31337, /, *, use_set: bool = True) -> str:
    return _set("moo", str(value), use_set=use_set)


# ── Console Channel Filters ──

def con_channelFilters() -> str:
    return "con_channelFilters"


def con_addChannelFilter(filter_val: str, action: str, /) -> str:
    return build_line("con_addChannelFilter", filter_val, action)


def con_removeChannelFilter(filter_val: str, action: str, /) -> str:
    return build_line("con_removeChannelFilter", filter_val, action)


# ── Endpoint Commands ──

def endpoint_add_tcp(endpoint: str, /) -> str:
    return build_line("endpoint_add_tcp", format_value(endpoint))


def endpoint_add_udp(endpoint: str, /) -> str:
    return build_line("endpoint_add_udp", format_value(endpoint))


# ── Pool Size ──

def increase_pool_size(pool: str, amount: int, /) -> str:
    return build_line("increase_pool_size", format_value(pool), str(amount))


# ── Server Icon ──

def load_server_icon(path: str, /) -> str:
    return build_line("load_server_icon", format_value(path))


# ── Replay / Recording ──

def replay_start(file_name: str, mode: str, /) -> str:
    return build_line("replay_start", file_name, mode)


def replay_stop(replay_id: str, /) -> str:
    return build_line("replay_stop", replay_id)


def sync_start_recording(net_id: str, compressed: str = "", /) -> str:
    args = [net_id]
    if compressed:
        args.append(compressed)
    return build_line("sync_start_recording", *args)


def sync_stop_recording(net_id: str, /) -> str:
    return build_line("sync_stop_recording", net_id)


# ═══════════════════════════════════════════════════════════════════════════
# SERVER CONFIGURATION (sv_* convars)
# ═══════════════════════════════════════════════════════════════════════════

def sv_hostname(name: str, /, *, use_set: bool = True) -> str:
    return _set("sv_hostname", name, use_set=use_set)


def sv_maxClients(n: int, /, *, use_set: bool = True) -> str:
    return _set("sv_maxClients", str(n), use_set=use_set)


def sv_licenseKey(key: str, /, *, use_set: bool = True) -> str:
    return _set("sv_licenseKey", key, use_set=use_set)


def sv_lan(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_lan", "true" if enabled else "false", use_set=use_set)


def sv_projectName(name: str, /, *, use_set: bool = True) -> str:
    return _sets("sv_projectName", name, use_set=use_set)


def sv_projectDesc(desc: str, /, *, use_set: bool = True) -> str:
    return _sets("sv_projectDesc", desc, use_set=use_set)


def sv_appearAllowlisted(enabled: bool, /, *, use_set: bool = True) -> str:
    return _sets("sv_appearAllowlisted", "true" if enabled else "false", use_set=use_set)


def sv_allowlistInstructions(text: str, /, *, use_set: bool = True) -> str:
    return _sets("sv_allowlistInstructions", text, use_set=use_set)


def sv_tebexSecret(secret: str, /, *, use_set: bool = True) -> str:
    return _set("sv_tebexSecret", secret, use_set=use_set)


def sv_enforceGameBuild(build_num: int, /, *, use_set: bool = True) -> str:
    return _set("sv_enforceGameBuild", str(build_num), use_set=use_set)


def sv_replaceExeToSwitchBuilds(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_replaceExeToSwitchBuilds", "true" if enabled else "false", use_set=use_set)


def sv_master1(url: str = "", /, *, use_set: bool = True) -> str:
    return _set("sv_master1", url, use_set=use_set)


def sv_kvsName(name: str = "default", /, *, use_set: bool = True) -> str:
    return _set("sv_kvsName", name, use_set=use_set)


def sv_endpoints(eps: str, /, *, use_set: bool = True) -> str:
    return _set("sv_endpoints", eps, use_set=use_set)


def sv_registerMulticastDns(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_registerMulticastDns", "true" if enabled else "false", use_set=use_set)


def sv_showBusySpinnerOnLoadingScreen(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_showBusySpinnerOnLoadingScreen", "true" if enabled else "false", use_set=use_set)


def sv_endpointurl(url: str, /, *, use_set: bool = True) -> str:
    return _set("sv_endpointurl", url, use_set=use_set)


def sv_kick_players_cnl(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_kick_players_cnl", "1" if enabled else "0", use_set=use_set)


def sv_exposePlayerIdentifiersInHttpEndpoint(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_exposePlayerIdentifiersInHttpEndpoint", "true" if enabled else "false", use_set=use_set)


def sv_scriptDebugDuplicates(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_scriptDebugDuplicates", "true" if enabled else "false", use_set=use_set)


# ── Network ──

def netPort(port: int, /, *, use_set: bool = True) -> str:
    return _set("netPort", str(port), use_set=use_set)


def net_tcpConnLimit(limit: int, /, *, use_set: bool = True) -> str:
    return _set("net_tcpConnLimit", str(limit), use_set=use_set)


def sv_tcpConnectionTimeoutSeconds(seconds: int, /, *, use_set: bool = True) -> str:
    return _set("sv_tcpConnectionTimeoutSeconds", str(seconds), use_set=use_set)


def sv_ioThreads(n: int, /, *, use_set: bool = True) -> str:
    return _set("sv_ioThreads", str(n), use_set=use_set)


def sv_clientConnectingTimeoutMilliseconds(ms: int, /, *, use_set: bool = True) -> str:
    return _set("sv_clientConnectingTimeoutMilliseconds", str(ms), use_set=use_set)


def sv_clientConnectedTimeoutMilliseconds(ms: int, /, *, use_set: bool = True) -> str:
    return _set("sv_clientConnectedTimeoutMilliseconds", str(ms), use_set=use_set)


def sv_pingIntervalMilliseconds(ms: int, /, *, use_set: bool = True) -> str:
    return _set("sv_pingIntervalMilliseconds", str(ms), use_set=use_set)


def sv_endpointPrivacy(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_endpointPrivacy", "true" if enabled else "false", use_set=use_set)


def sv_forceIndirectListing(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_forceIndirectListing", "true" if enabled else "false", use_set=use_set)


def sv_listingIpOverride(ip: str, /, *, use_set: bool = True) -> str:
    return _set("sv_listingIpOverride", ip, use_set=use_set)


def sv_listingHostOverride(host: str, /, *, use_set: bool = True) -> str:
    return _set("sv_listingHostOverride", host, use_set=use_set)


def sv_proxyIPRanges(ranges: str, /, *, use_set: bool = True) -> str:
    return _set("sv_proxyIPRanges", ranges, use_set=use_set)


def sv_enhancedHostSupport(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_enhancedHostSupport", "true" if enabled else "false", use_set=use_set)


# ── Security & Authentication ──

def rcon_password(pw: str, /) -> str:
    return build_line("rcon_password", format_value(pw))


def sv_scriptHookAllowed(allowed: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_scriptHookAllowed", "1" if allowed else "0", use_set=use_set)


def sv_authMaxVariance(var: int, /, *, use_set: bool = True) -> str:
    return _set("sv_authMaxVariance", str(var), use_set=use_set)


def sv_authMinTrust(trust: int, /, *, use_set: bool = True) -> str:
    return _set("sv_authMinTrust", str(trust), use_set=use_set)


def sv_requestParanoia(level: int, /, *, use_set: bool = True) -> str:
    return _set("sv_requestParanoia", str(level), use_set=use_set)


def sv_filterRequestControl(mode: int, /, *, use_set: bool = True) -> str:
    return _set("sv_filterRequestControl", str(mode), use_set=use_set)


def sv_filterRequestControlSettleTimer(ms: int, /, *, use_set: bool = True) -> str:
    return _set("sv_filterRequestControlSettleTimer", str(ms), use_set=use_set)


def sv_pureLevel(level: int, /, *, use_set: bool = True) -> str:
    return _set("sv_pureLevel", str(level), use_set=use_set)


def sv_entityLockdown(mode: str, /, *, use_set: bool = True) -> str:
    return _set("sv_entityLockdown", mode, use_set=use_set)


def sv_useAccurateSends(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_useAccurateSends", "true" if enabled else "false", use_set=use_set)


def sv_protectServerEntities(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_protectServerEntities", "true" if enabled else "false", use_set=use_set)


# ── OneSync ──

def onesync(mode: str, /) -> str:
    return build_line("onesync", mode)


def onesync_enableInfinity(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("onesync_enableInfinity", "true" if enabled else "false", use_set=use_set)


def onesync_enableBeyond(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("onesync_enableBeyond", "true" if enabled else "false", use_set=use_set)


def onesync_population(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("onesync_population", "true" if enabled else "false", use_set=use_set)


def onesync_forceMigration(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("onesync_forceMigration", "true" if enabled else "false", use_set=use_set)


def onesync_distanceCulling(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("onesync_distanceCulling", "true" if enabled else "false", use_set=use_set)


def onesync_distanceCullVehicles(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("onesync_distanceCullVehicles", "true" if enabled else "false", use_set=use_set)


def onesync_radiusFrequency(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("onesync_radiusFrequency", "true" if enabled else "false", use_set=use_set)


def onesync_migrateDataTimeout(ms: int, /, *, use_set: bool = True) -> str:
    return _set("onesync_migrateDataTimeout", str(ms), use_set=use_set)


def onesync_compressionDictionarySamples(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("onesync_compressionDictionarySamples", "true" if enabled else "false", use_set=use_set)


def onesync_mapBoundsMinX(value: int, /, *, use_set: bool = True) -> str:
    return _set("onesync_mapBoundsMinX", str(value), use_set=use_set)


def onesync_mapBoundsMinY(value: int, /, *, use_set: bool = True) -> str:
    return _set("onesync_mapBoundsMinY", str(value), use_set=use_set)


def onesync_mapBoundsMaxX(value: int, /, *, use_set: bool = True) -> str:
    return _set("onesync_mapBoundsMaxX", str(value), use_set=use_set)


def onesync_mapBoundsMaxY(value: int, /, *, use_set: bool = True) -> str:
    return _set("onesync_mapBoundsMaxY", str(value), use_set=use_set)


def onesync_mapCellAreaSize(size: int, /, *, use_set: bool = True) -> str:
    return _set("onesync_mapCellAreaSize", str(size), use_set=use_set)


# ── Features ──

def sv_enableNetworkedSounds(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_enableNetworkedSounds", "true" if enabled else "false", use_set=use_set)


def sv_enableNetworkedPhoneExplosions(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_enableNetworkedPhoneExplosions", "true" if enabled else "false", use_set=use_set)


def sv_enableNetworkedScriptEntityStates(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_enableNetworkedScriptEntityStates", "true" if enabled else "false", use_set=use_set)


def sv_enableNetEventReassembly(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_enableNetEventReassembly", "true" if enabled else "false", use_set=use_set)


def sv_netEventReassemblyMaxPendingEvents(n: int, /, *, use_set: bool = True) -> str:
    return _set("sv_netEventReassemblyMaxPendingEvents", str(n), use_set=use_set)


def sv_netEventReassemblyUnlimitedPendingEvents(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_netEventReassemblyUnlimitedPendingEvents", "true" if enabled else "false", use_set=use_set)


def sv_voiceChat(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_voiceChat", "true" if enabled else "false", use_set=use_set)


def sv_mumble(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_mumble", "true" if enabled else "false", use_set=use_set)


def sv_devMode(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_devMode", "true" if enabled else "false", use_set=use_set)


def svgui(enabled: bool = True, /) -> str:
    return "svgui" if enabled else "svgui"


# ── Experimental ──

def sv_experimentalStateBagsHandler(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_experimentalStateBagsHandler", "true" if enabled else "false", use_set=use_set)


def sv_experimentalOnesyncPopulation(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_experimentalOnesyncPopulation", "true" if enabled else "false", use_set=use_set)


def sv_experimentalNetGameEventHandler(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_experimentalNetGameEventHandler", "true" if enabled else "false", use_set=use_set)


def sv_stateBagStrictMode(enabled: bool, /, *, use_set: bool = True) -> str:
    return _setr("sv_stateBagStrictMode", "true" if enabled else "false", use_set=use_set)


def sv_httpFileServerProxyOnly(enabled: bool, /, *, use_set: bool = True) -> str:
    return _set("sv_httpFileServerProxyOnly", "true" if enabled else "false", use_set=use_set)


# ── Steam ──

def steam_webApiKey(key: str, /, *, use_set: bool = True) -> str:
    return _set("steam_webApiKey", key, use_set=use_set)


def steam_webApiDomain(domain: str, /, *, use_set: bool = True) -> str:
    return _set("steam_webApiDomain", domain, use_set=use_set)


# ── Monitoring ──

def sv_prometheusBasicAuthUser(user: str, /, *, use_set: bool = True) -> str:
    return _set("sv_prometheusBasicAuthUser", user, use_set=use_set)


def sv_prometheusBasicAuthPassword(pw: str, /, *, use_set: bool = True) -> str:
    return _set("sv_prometheusBasicAuthPassword", pw, use_set=use_set)


# ── Misc ──

def gamename(game: str, /) -> str:
    return build_line("gamename", game)


def gametype(gtype: str, /) -> str:
    return build_line("gametype", format_value(gtype))


def mapname(name: str, /) -> str:
    return build_line("mapname", format_value(name))


# ═══════════════════════════════════════════════════════════════════════════
# RATE LIMITER BUILDERS
# ═══════════════════════════════════════════════════════════════════════════

def _rateLimiter(name: str, rate: int, burst: int, /) -> list[str]:
    return [
        _set(f"rateLimiter_{name}_rate", str(rate)),
        _set(f"rateLimiter_{name}_burst", str(burst)),
    ]


def rateLimiter_challenge(rate: int = 4, burst: int = 10, /) -> list[str]:
    return _rateLimiter("challenge", rate, burst)


def rateLimiter_handshake(rate: int = 4, burst: int = 10, /) -> list[str]:
    return _rateLimiter("handshake", rate, burst)


def rateLimiter_handshakeUDP(rate: int = 1, burst: int = 5, /) -> list[str]:
    return _rateLimiter("handshakeUDP", rate, burst)


def rateLimiter_http_dynamic(rate: int = 4, burst: int = 10, /) -> list[str]:
    return _rateLimiter("http_dynamic", rate, burst)


def rateLimiter_http_info(rate: int = 4, burst: int = 10, /) -> list[str]:
    return _rateLimiter("http_info", rate, burst)


def rateLimiter_http_perf(rate: int = 2, burst: int = 5, /) -> list[str]:
    return _rateLimiter("http_perf", rate, burst)


def rateLimiter_http_players(rate: int = 4, burst: int = 10, /) -> list[str]:
    return _rateLimiter("http_players", rate, burst)


def rateLimiter_netCommand(rate: int = 7, burst: int = 14, /) -> list[str]:
    return _rateLimiter("netCommand", rate, burst)


def rateLimiter_netCommandFlood(rate: int = 25, burst: int = 45, /) -> list[str]:
    return _rateLimiter("netCommandFlood", rate, burst)


def rateLimiter_netCommandSize(rate: int = 1024, burst: int = 8192, /) -> list[str]:
    return _rateLimiter("netCommandSize", rate, burst)


def rateLimiter_netEvent(rate: int = 50, burst: int = 200, /) -> list[str]:
    return _rateLimiter("netEvent", rate, burst)


def rateLimiter_netEventFlood(rate: int = 75, burst: int = 300, /) -> list[str]:
    return _rateLimiter("netEventFlood", rate, burst)


def rateLimiter_rcon(rate: int = 2, burst: int = 5, /) -> list[str]:
    return _rateLimiter("rcon", rate, burst)


def rateLimiter_res_http_handler(rate: int = 10, burst: int = 25, /) -> list[str]:
    return _rateLimiter("res_http_handler", rate, burst)


def rateLimiter_resourceList(rate: int = 10, burst: int = 25, /) -> list[str]:
    return _rateLimiter("resourceList", rate, burst)


def rateLimiter_stateBag(rate: int = 75, burst: int = 125, /) -> list[str]:
    return _rateLimiter("stateBag", rate, burst)


def rateLimiter_stateBagFlood(rate: int = 150, burst: int = 175, /) -> list[str]:
    return _rateLimiter("stateBagFlood", rate, burst)


def rateLimiter_stateBagSize(rate: int = 131072, burst: int = 262144, /) -> list[str]:
    return _rateLimiter("stateBagSize", rate, burst)


def rateLimiter_all(rate: int = 0, burst: int = 0, /) -> list[str]:
    lines: list[str] = []
    for pair in get_ratelimiter_pairs():
        rate_cvar, burst_cvar = pair
        lines.append(_set(rate_cvar, str(rate)))
        lines.append(_set(burst_cvar, str(burst)))
    return lines


# ═══════════════════════════════════════════════════════════════════════════
# BATCH BUILDERS
# ═══════════════════════════════════════════════════════════════════════════

def batch_admin_permissions(groups: list[str] | None = None, /) -> list[str]:
    if groups is None:
        groups = ["group.admin"]
    lines: list[str] = []
    for g in groups:
        lines.append(add_ace(g, "command", "allow"))
        lines.append(add_ace(g, "command.kick", "allow"))
        lines.append(add_ace(g, "command.ban", "allow"))
        lines.append(add_ace(g, "txAdmin.kick", "allow"))
        lines.append(add_ace(g, "txAdmin.ban", "allow"))
        lines.append(add_ace(g, "txAdmin.warn", "allow"))
    return lines


def batch_ensures(*resources: str) -> list[str]:
    return [ensure(r) for r in resources]


def batch_default_ensures() -> list[str]:
    return batch_ensures(
        "mapmanager", "chat", "spawnmanager", "sessionmanager",
        "basic-gamemode", "hardcap", "rconlog", "baseevents",
    )


def batch_identifier_steam(steam64: str, group: str = "group.admin", /) -> list[str]:
    return [add_principal(make_steam_id(steam64), group)]


def batch_identifier_license(license: str, group: str = "group.admin", /) -> list[str]:
    return [add_principal(make_license_id(license), group)]


def batch_identifier_discord(discord_id: str, group: str = "group.admin", /) -> list[str]:
    return [add_principal(make_discord_id(discord_id), group)]


def batch_standard_server_config(hostname: str, max_clients: int = 48, license_key: str = "", /) -> list[str]:
    lines: list[str] = []
    lines.append(sv_hostname(hostname))
    lines.append(sv_maxClients(max_clients))
    if license_key:
        lines.append(sv_licenseKey(license_key))
    lines.append(netPort(30120))
    lines.append(endpoint_add_tcp("0.0.0.0:30120"))
    return lines


def batch_standard_onesync(max_clients: int = 64, /) -> list[str]:
    lines: list[str] = []
    if max_clients > 32:
        lines.append(onesync("on"))
        lines.append(onesync_enableInfinity(True))
    lines.append(onesync_population(True))
    lines.append(onesync_forceMigration(True))
    lines.append(onesync_distanceCulling(True))
    lines.append(onesync_radiusFrequency(True))
    return lines


# ── Backward Compatibility Aliases ──
build_hostname = sv_hostname
build_max_clients = sv_maxClients
build_license_key = sv_licenseKey
build_lan = sv_lan
build_project_name = sv_projectName
build_project_desc = sv_projectDesc
build_tebex_secret = sv_tebexSecret
build_game_build = sv_enforceGameBuild
build_game_name = gamename
build_game_type = gametype
build_map_name = mapname
build_rcon_password = rcon_password
build_net_port = netPort
build_tcp_limit = net_tcpConnLimit
build_script_hook = sv_scriptHookAllowed
build_endpoint_privacy = sv_endpointPrivacy
build_entity_lockdown = sv_entityLockdown
build_pure_level = sv_pureLevel
build_request_paranoia = sv_requestParanoia
build_auth_variance = sv_authMaxVariance
build_auth_trust = sv_authMinTrust
build_filter_request = sv_filterRequestControl
build_filter_settle = sv_filterRequestControlSettleTimer
build_onesync = onesync
build_onesync_infinity = onesync_enableInfinity
build_onesync_population = onesync_population
build_onesync_migration = onesync_forceMigration
build_onesync_culling = onesync_distanceCulling
build_onesync_cull_vehicles = onesync_distanceCullVehicles
build_onesync_radius = onesync_radiusFrequency
build_onesync_migrate_timeout = onesync_migrateDataTimeout
build_onesync_cell_size = onesync_mapCellAreaSize
build_networked_sounds = sv_enableNetworkedSounds
build_networked_phone_explosions = sv_enableNetworkedPhoneExplosions
build_script_entity_states = sv_enableNetworkedScriptEntityStates
build_event_reassembly = sv_enableNetEventReassembly
build_max_pending_events = sv_netEventReassemblyMaxPendingEvents
build_unlimited_pending = sv_netEventReassemblyUnlimitedPendingEvents
build_voice_chat = sv_voiceChat
build_mumble = sv_mumble
build_dev_mode = sv_devMode
build_accurate_sends = sv_useAccurateSends
build_indirect_listing = sv_forceIndirectListing
build_listing_ip = sv_listingIpOverride
build_listing_host = sv_listingHostOverride
build_multicast_dns = sv_registerMulticastDns
build_endpoints = sv_endpoints
build_tcp_timeout = sv_tcpConnectionTimeoutSeconds
build_proxy_ranges = sv_proxyIPRanges
build_io_threads = sv_ioThreads
build_connect_timeout = sv_clientConnectingTimeoutMilliseconds
build_connected_timeout = sv_clientConnectedTimeoutMilliseconds
build_ping_interval = sv_pingIntervalMilliseconds
build_steam_api_key = steam_webApiKey
build_steam_domain = steam_webApiDomain
build_prometheus_user = sv_prometheusBasicAuthUser
build_prometheus_pass = sv_prometheusBasicAuthPassword
build_ratelimiter = _rateLimiter
build_ratelimiter_challenge = rateLimiter_challenge
build_ratelimiter_handshake = rateLimiter_handshake
build_ratelimiter_handshake_udp = rateLimiter_handshakeUDP
build_ratelimiter_http_dynamic = rateLimiter_http_dynamic
build_ratelimiter_http_info = rateLimiter_http_info
build_ratelimiter_http_perf = rateLimiter_http_perf
build_ratelimiter_http_players = rateLimiter_http_players
build_ratelimiter_net_command = rateLimiter_netCommand
build_ratelimiter_net_command_flood = rateLimiter_netCommandFlood
build_ratelimiter_net_command_size = rateLimiter_netCommandSize
build_ratelimiter_net_event = rateLimiter_netEvent
build_ratelimiter_net_event_flood = rateLimiter_netEventFlood
build_ratelimiter_rcon = rateLimiter_rcon
build_ratelimiter_res_http = rateLimiter_res_http_handler
build_ratelimiter_resource_list = rateLimiter_resourceList
build_ratelimiter_state_bag = rateLimiter_stateBag
build_ratelimiter_state_bag_flood = rateLimiter_stateBagFlood
build_ratelimiter_state_bag_size = rateLimiter_stateBagSize
build_all_ratelimiters = rateLimiter_all
build_admin_permissions = batch_admin_permissions
build_resource_ensures = batch_ensures
build_default_ensures = batch_default_ensures
build_identifier_steam = batch_identifier_steam
build_identifier_license = batch_identifier_license
build_identifier_discord = batch_identifier_discord
build_standard_server_config = batch_standard_server_config
build_standard_onesync = batch_standard_onesync


# ═══════════════════════════════════════════════════════════════════════════
# REMAINING KEYWORD BUILDERS (every keyword from META has a function)
# ═══════════════════════════════════════════════════════════════════════════

# ── Set Commands (exposed publicly) ──

def set(name: str, value: str, /, *, use_set: bool = True) -> str:
    return _set(name, value, use_set=use_set)


def setr(name: str, value: str, /, *, use_set: bool = True) -> str:
    return _setr(name, value, use_set=use_set)


def sets(name: str, value: str, /, *, use_set: bool = True) -> str:
    return _sets(name, value, use_set=use_set)


# ── Lowercase Aliases ──

def sv_maxclients(n: int, /) -> str:
    return sv_maxClients(n)


# ── Individual Rate Limiter ConVars ──

def rateLimiter_challenge_rate(value: int = 4, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_challenge_rate", str(value), use_set=use_set)


def rateLimiter_challenge_burst(value: int = 10, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_challenge_burst", str(value), use_set=use_set)


def rateLimiter_handshake_rate(value: int = 4, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_handshake_rate", str(value), use_set=use_set)


def rateLimiter_handshake_burst(value: int = 10, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_handshake_burst", str(value), use_set=use_set)


def rateLimiter_handshakeUDP_rate(value: int = 1, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_handshakeUDP_rate", str(value), use_set=use_set)


def rateLimiter_handshakeUDP_burst(value: int = 5, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_handshakeUDP_burst", str(value), use_set=use_set)


def rateLimiter_http_dynamic_rate(value: int = 4, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_http_dynamic_rate", str(value), use_set=use_set)


def rateLimiter_http_dynamic_burst(value: int = 10, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_http_dynamic_burst", str(value), use_set=use_set)


def rateLimiter_http_info_rate(value: int = 4, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_http_info_rate", str(value), use_set=use_set)


def rateLimiter_http_info_burst(value: int = 10, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_http_info_burst", str(value), use_set=use_set)


def rateLimiter_http_perf_rate(value: int = 2, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_http_perf_rate", str(value), use_set=use_set)


def rateLimiter_http_perf_burst(value: int = 5, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_http_perf_burst", str(value), use_set=use_set)


def rateLimiter_http_players_rate(value: int = 4, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_http_players_rate", str(value), use_set=use_set)


def rateLimiter_http_players_burst(value: int = 10, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_http_players_burst", str(value), use_set=use_set)


def rateLimiter_netCommand_rate(value: int = 7, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netCommand_rate", str(value), use_set=use_set)


def rateLimiter_netCommand_burst(value: int = 14, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netCommand_burst", str(value), use_set=use_set)


def rateLimiter_netCommandFlood_rate(value: int = 25, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netCommandFlood_rate", str(value), use_set=use_set)


def rateLimiter_netCommandFlood_burst(value: int = 45, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netCommandFlood_burst", str(value), use_set=use_set)


def rateLimiter_netCommandSize_rate(value: int = 1024, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netCommandSize_rate", str(value), use_set=use_set)


def rateLimiter_netCommandSize_burst(value: int = 8192, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netCommandSize_burst", str(value), use_set=use_set)


def rateLimiter_netEvent_rate(value: int = 50, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netEvent_rate", str(value), use_set=use_set)


def rateLimiter_netEvent_burst(value: int = 200, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netEvent_burst", str(value), use_set=use_set)


def rateLimiter_netEventFlood_rate(value: int = 75, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netEventFlood_rate", str(value), use_set=use_set)


def rateLimiter_netEventFlood_burst(value: int = 300, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_netEventFlood_burst", str(value), use_set=use_set)


def rateLimiter_rcon_rate(value: int = 2, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_rcon_rate", str(value), use_set=use_set)


def rateLimiter_rcon_burst(value: int = 5, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_rcon_burst", str(value), use_set=use_set)


def rateLimiter_res_http_handler_rate(value: int = 10, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_res_http_handler_rate", str(value), use_set=use_set)


def rateLimiter_res_http_handler_burst(value: int = 25, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_res_http_handler_burst", str(value), use_set=use_set)


def rateLimiter_resourceList_rate(value: int = 10, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_resourceList_rate", str(value), use_set=use_set)


def rateLimiter_resourceList_burst(value: int = 25, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_resourceList_burst", str(value), use_set=use_set)


def rateLimiter_stateBag_rate(value: int = 75, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_stateBag_rate", str(value), use_set=use_set)


def rateLimiter_stateBag_burst(value: int = 125, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_stateBag_burst", str(value), use_set=use_set)


def rateLimiter_stateBagFlood_rate(value: int = 150, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_stateBagFlood_rate", str(value), use_set=use_set)


def rateLimiter_stateBagFlood_burst(value: int = 175, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_stateBagFlood_burst", str(value), use_set=use_set)


def rateLimiter_stateBagSize_rate(value: int = 131072, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_stateBagSize_rate", str(value), use_set=use_set)


def rateLimiter_stateBagSize_burst(value: int = 262144, /, *, use_set: bool = True) -> str:
    return _set("rateLimiter_stateBagSize_burst", str(value), use_set=use_set)


# ── txAdmin ConVars ──

def txAdmin_menuEnabled(enabled: bool = True, /, *, use_set: bool = True) -> str:
    return _set("txAdmin-menuEnabled", "true" if enabled else "false", use_set=use_set)


def txAdmin_menuAlignRight(enabled: bool = False, /, *, use_set: bool = True) -> str:
    return _set("txAdmin-menuAlignRight", "true" if enabled else "false", use_set=use_set)


def txAdmin_menuPageKey(key: str = "Tab", /, *, use_set: bool = True) -> str:
    return _set("txAdmin-menuPageKey", key, use_set=use_set)


def txAdmin_hideDefaultAnnouncement(enabled: bool = False, /, *, use_set: bool = True) -> str:
    return _set("txAdmin-hideDefaultAnnouncement", "true" if enabled else "false", use_set=use_set)


def txAdmin_hideDefaultDirectMessage(enabled: bool = False, /, *, use_set: bool = True) -> str:
    return _set("txAdmin-hideDefaultDirectMessage", "true" if enabled else "false", use_set=use_set)


def txAdmin_hideDefaultWarning(enabled: bool = False, /, *, use_set: bool = True) -> str:
    return _set("txAdmin-hideDefaultWarning", "true" if enabled else "false", use_set=use_set)


def txAdmin_hideDefaultScheduledRestartWarning(enabled: bool = False, /, *, use_set: bool = True) -> str:
    return _set("txAdmin-hideDefaultScheduledRestartWarning", "true" if enabled else "false", use_set=use_set)


def txAdmin_debugMode(enabled: bool = False, /, *, use_set: bool = True) -> str:
    return _setr("txAdmin-debugMode", "true" if enabled else "false", use_set=use_set)


def txAdmin_menuPlayerIdDistance(distance: int = 150, /, *, use_set: bool = True) -> str:
    return _setr("txAdmin-menuPlayerIdDistance", str(distance), use_set=use_set)


def txAdmin_menuDrunkDuration(seconds: int = 0, /, *, use_set: bool = True) -> str:
    return _setr("txAdmin-menuDrunkDuration", str(seconds), use_set=use_set)


# ═══════════════════════════════════════════════════════════════════════════
# PRINCIPAL CONSTANTS (string values for use in add_ace/add_principal)
# ═══════════════════════════════════════════════════════════════════════════

# Built-in
PRINCIPAL_EVERYONE = "builtin.everyone"
PRINCIPAL_RESTRICTED = "builtin.restricted"

# Groups
PRINCIPAL_GROUP_ADMIN = "group.admin"
PRINCIPAL_GROUP_MODERATOR = "group.moderator"
PRINCIPAL_GROUP_OWNER = "group.owner"
PRINCIPAL_GROUP_USER = "group.user"
PRINCIPAL_GROUP_SUPPORT = "group.support"
PRINCIPAL_GROUP_HELPER = "group.helper"
PRINCIPAL_GROUP_GOD = "group.god"
PRINCIPAL_GROUP_SUPERADMIN = "group.superadmin"
PRINCIPAL_GROUP_DEVELOPER = "group.developer"

# Identifiers
PRINCIPAL_IDENTIFIER_STEAM = "identifier.steam"
PRINCIPAL_IDENTIFIER_LICENSE = "identifier.license"
PRINCIPAL_IDENTIFIER_DISCORD = "identifier.discord"
PRINCIPAL_IDENTIFIER_FIVEM = "identifier.fivem"
PRINCIPAL_IDENTIFIER_IP = "identifier.ip"
PRINCIPAL_IDENTIFIER_XBL = "identifier.xbl"

# Resources
PRINCIPAL_RESOURCE_MAPMANAGER = "resource.mapmanager"
PRINCIPAL_RESOURCE_CHAT = "resource.chat"
PRINCIPAL_RESOURCE_SPAWNMANAGER = "resource.spawnmanager"
PRINCIPAL_RESOURCE_SESSIONMANAGER = "resource.sessionmanager"
PRINCIPAL_RESOURCE_HARDCAP = "resource.hardcap"
PRINCIPAL_RESOURCE_RCONLOG = "resource.rconlog"
PRINCIPAL_RESOURCE_BASEEVENTS = "resource.baseevents"

# Bare Resources
PRINCIPAL_MAPMANAGER = "mapmanager"
PRINCIPAL_CHAT = "chat"
PRINCIPAL_SPAWNMANAGER = "spawnmanager"
PRINCIPAL_SESSIONMANAGER = "sessionmanager"
PRINCIPAL_BASIC_GAMEMODE = "basic-gamemode"
PRINCIPAL_HARDCAP = "hardcap"
PRINCIPAL_RCONLOG = "rconlog"
PRINCIPAL_BASEEVENTS = "baseevents"

# Commands
PRINCIPAL_COMMAND = "command"
PRINCIPAL_COMMAND_KICK = "command.kick"
PRINCIPAL_COMMAND_BAN = "command.ban"
PRINCIPAL_COMMAND_TEMPBAN = "command.tempban"
PRINCIPAL_COMMAND_SETGROUP = "command.setgroup"
PRINCIPAL_COMMAND_ADMIN = "command.admin"
PRINCIPAL_COMMAND_NOCLIP = "command.noclip"
PRINCIPAL_COMMAND_TPM = "command.tpm"
PRINCIPAL_COMMAND_BRING = "command.bring"
PRINCIPAL_COMMAND_REVIVE = "command.revive"
PRINCIPAL_COMMAND_HEAL = "command.heal"
PRINCIPAL_COMMAND_ANNOUNCE = "command.announce"
PRINCIPAL_COMMAND_CAR = "command.car"
PRINCIPAL_COMMAND_WEATHER = "command.weather"
PRINCIPAL_COMMAND_TIME = "command.time"
PRINCIPAL_COMMAND_QUIT = "command.quit"
PRINCIPAL_COMMAND_ADD_ACE = "command.add_ace"
PRINCIPAL_COMMAND_ADD_PRINCIPAL = "command.add_principal"

# txAdmin
PRINCIPAL_TXADMIN_KICK = "txAdmin.kick"
PRINCIPAL_TXADMIN_BAN = "txAdmin.ban"
PRINCIPAL_TXADMIN_WARN = "txAdmin.warn"
PRINCIPAL_TXADMIN_PLAYERS_HEAL = "txAdmin.players.heal"

# Frameworks
PRINCIPAL_QBCORE_ADMIN = "qbcore.admin"
PRINCIPAL_QBX_ADMIN = "qbx.admin"
PRINCIPAL_ESX_ADMIN = "esx.admin"


# ═══════════════════════════════════════════════════════════════════════════
# KEYWORD STRING CONSTANTS (exact keyword names for lookup/validation)
# ═══════════════════════════════════════════════════════════════════════════

# Built-in
builtin_everyone = "builtin.everyone"
builtin_restricted = "builtin.restricted"

# Groups
group_admin = "group.admin"
group_moderator = "group.moderator"
group_owner = "group.owner"
group_user = "group.user"
group_support = "group.support"
group_helper = "group.helper"
group_god = "group.god"
group_superadmin = "group.superadmin"
group_developer = "group.developer"

# Identifiers
identifier_steam = "identifier.steam"
identifier_license = "identifier.license"
identifier_discord = "identifier.discord"
identifier_fivem = "identifier.fivem"
identifier_ip = "identifier.ip"
identifier_xbl = "identifier.xbl"

# Resources
resource_mapmanager = "resource.mapmanager"
resource_chat = "resource.chat"
resource_spawnmanager = "resource.spawnmanager"
resource_sessionmanager = "resource.sessionmanager"
resource_hardcap = "resource.hardcap"
resource_rconlog = "resource.rconlog"
resource_baseevents = "resource.baseevents"

# Bare Resources
baseevents = "baseevents"
basic_gamemode = "basic-gamemode"
chat = "chat"
hardcap = "hardcap"
mapmanager = "mapmanager"
rconlog = "rconlog"
sessionmanager = "sessionmanager"
spawnmanager = "spawnmanager"

# Commands
command_str = "command"
command_add_ace = "command.add_ace"
command_add_principal = "command.add_principal"
command_admin = "command.admin"
command_announce = "command.announce"
command_ban = "command.ban"
command_bring = "command.bring"
command_car = "command.car"
command_heal = "command.heal"
command_kick = "command.kick"
command_noclip = "command.noclip"
command_quit = "command.quit"
command_revive = "command.revive"
command_setgroup = "command.setgroup"
command_tempban = "command.tempban"
command_time = "command.time"
command_tpm = "command.tpm"
command_weather = "command.weather"

# txAdmin Permissions
txAdmin_kick = "txAdmin.kick"
txAdmin_ban = "txAdmin.ban"
txAdmin_warn = "txAdmin.warn"
txAdmin_players_heal = "txAdmin.players.heal"

# Frameworks
qbcore_admin = "qbcore.admin"
qbx_admin = "qbx.admin"
esx_admin = "esx.admin"

# txAdmin ConVar keywords (hyphen names)
TXADMIN_MENU_ENABLED = "txAdmin-menuEnabled"
TXADMIN_MENU_ALIGN_RIGHT = "txAdmin-menuAlignRight"
TXADMIN_MENU_PAGE_KEY = "txAdmin-menuPageKey"
TXADMIN_HIDE_DEFAULT_ANNOUNCEMENT = "txAdmin-hideDefaultAnnouncement"
TXADMIN_HIDE_DEFAULT_DIRECT_MESSAGE = "txAdmin-hideDefaultDirectMessage"
TXADMIN_HIDE_DEFAULT_WARNING = "txAdmin-hideDefaultWarning"
TXADMIN_HIDE_DEFAULT_SCHEDULED_RESTART_WARNING = "txAdmin-hideDefaultScheduledRestartWarning"
TXADMIN_DEBUG_MODE = "txAdmin-debugMode"
TXADMIN_MENU_PLAYER_ID_DISTANCE = "txAdmin-menuPlayerIdDistance"
TXADMIN_MENU_DRUNK_DURATION = "txAdmin-menuDrunkDuration"


def get_all_lines() -> list[str]:
    lines = []
    for cvar in sorted(_G.CVARS):
        lines.append(f"# {cvar}")
    return lines


def get_stats() -> dict[str, int]:
    return {
        "cvars": len(_G.CVARS),
        "actions": len(_G.ACTIONS),
        "principals": len(_G.PRINCIPALS),
        "states": len(_G.STATES),
        "total": len(_G.ALL),
        "metadata": len(_G.META),
        "sv_convars": len(get_sv_convars()),
        "onesync_convars": len(get_onesync_convars()),
        "ratelimiter_convars": len(get_ratelimiter_convars()),
        "ratelimiter_pairs": len(get_ratelimiter_pairs()),
        "groups": len(get_group_principals()),
        "identifiers": len(get_identifier_principals()),
        "resources": len(get_resource_principals()),
        "commands": len(get_command_permissions()),
        "txadmin": len(get_txadmin_permissions()),
        "frameworks": len(get_framework_permissions()),
        "deprecated": len(find_deprecated()),
        "startup_only": len(find_startup_only()),
    }
