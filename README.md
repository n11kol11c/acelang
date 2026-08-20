<p align="center">
  <img src="https://img.shields.io/badge/VS%20Code-Extension-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FiveM-Server-orange?style=for-the-badge" alt="FiveM">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome">
  <img src="https://img.shields.io/badge/Keywords-225-blue?style=for-the-badge" alt="Keywords">
  <img src="https://img.shields.io/badge/Exports-521-purple?style=for-the-badge" alt="Exports">
</p>

<h1 align="center">Acelang</h1>

<p align="center">
  <strong>Professional configuration language and tooling for FiveM servers</strong>
</p>

<p align="center">
  Acelang provides a structured, human-readable syntax for managing FiveM server configurations.<br>
  Complete with syntax highlighting, parsing, validation, and a comprehensive Python SDK.
</p>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Syntax Reference](#syntax-reference)
- [Python SDK](#python-sdk)
- [Builder Functions](#builder-functions)
- [Buffer Utilities](#buffer-utilities)
- [VS Code Extension](#vs-code-extension)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Acelang is a configuration language designed specifically for FiveM game servers. It provides a clean, maintainable syntax for server configurations with full tooling support.

### Why Acelang?

- **Structured Syntax** - Clean, readable configuration files
- **225 Keywords** - Complete coverage of FiveM server convars, commands, and resources
- **521 Exports** - Functions, constants, and utilities for programmatic configuration
- **VS Code Extension** - Full syntax highlighting for `.ac` files
- **Python SDK** - Parse, validate, and build configurations programmatically
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Type-Safe** - Python 3.8+ with full type hints
- **Zero Dependencies** - Pure Python, no external packages required

---

## Features

### Language Features

| Feature | Syntax | Description |
|---------|--------|-------------|
| Single-line Comment | `# comment` | Standard hash comments |
| Multi-line Comment | `/; ... ;/` | Block comments for documentation |
| Strings | `"double"` or `'single'` | Quoted string values with escape sequences |
| Numbers | `42`, `3.14` | Integer and float literals |
| Booleans | `true`, `false`, `on`, `off` | Boolean literals |
| Convars | `sv_*`, `onesync_*` | Server configuration variables |
| Resources | `ensure`, `start`, `stop` | Resource lifecycle management |
| Permissions | `add_ace`, `remove_ace` | ACE permission system |
| Principals | `add_principal` | User/group hierarchy |
| Directives | `@include`, `@from` | File inclusion system |
| Flow Control | `if`, `else`, `for`, `while` | Conditional and loop constructs |

### VS Code Extension Features

- **Syntax Highlighting** - Full TextMate grammar for `.ac` files
- **Comment Toggling** - `Ctrl+/` for single-line, `Shift+Alt+A` for block comments
- **Bracket Matching** - Automatic bracket and quote closing
- **Color Customization** - Configurable token colors via `settings.json`

### Python SDK Features

- **225 Keywords** - Complete FiveM keyword coverage
- **151 Builder Functions** - Type-safe configuration builders
- **67 String Constants** - Principal and resource identifiers
- **362 Total Functions** - Including lookup, validation, and utility functions
- **Buffer Utilities** - Byte manipulation and conversion tools
- **Rate Limiter Support** - All 36 rate limiter convars
- **txAdmin Integration** - All txAdmin convars and permissions

---

## Quick Start

### VS Code Extension

Install syntax highlighting for `.ac` files:

```bash
# Clone the repository
git clone https://github.com/n11kol11c/acelang.git
cd acelang/packages/vscode

# Run installer
./install.sh        # macOS / Linux
install.bat         # Windows
```

### Python SDK

Install the Python library for configuration management:

```bash
cd acelang/packages/cli
pip install -e .
```

### Basic Usage

```python
from kit import *

# Build server configuration
config = [
    sv_hostname("My RP Server"),
    sv_maxClients(48),
    sv_licenseKey("your_key_here"),
    sv_lan(False),
    onesync("on"),
    onesync_enableInfinity(True),
    ensure("mapmanager"),
    ensure("chat"),
    ensure("spawnmanager"),
    add_ace("group.admin", "command", "allow"),
    add_principal("identifier.license:abc123", "group.admin"),
]

# Write to file
with open("server.cfg", "w") as f:
    f.write("\n".join(config))
```

---

## Syntax Reference

### Comments

```ac
# This is a single-line comment

/;
This is a multi-line comment.
It can span multiple lines.
;/
```

### Strings

```ac
sv_hostname "My Server"
sv_hostname 'My Server'

# Escape sequences
sv_hostname "Server with \"quotes\""
sv_hostname "Server with\nnewlines"
```

### Numbers

```ac
sv_maxClients 48
sv_enforceGameBuild 2944
sv_pingIntervalMilliseconds 5000
```

### Booleans

```ac
sv_lan true
sv_scriptHookAllowed false
onesync on
```

### Convars (Configuration Variables)

```ac
# Server identity
sv_hostname "My Server"
sv_maxClients 48
sv_licenseKey "your_key_here"
sv_lan false

# Game settings
sv_enforceGameBuild 2944
sv_scriptHookAllowed true
sv_endpointPrivacy true

# Network
netPort 30120
sv_tcpConnectionTimeoutSeconds 30
sv_pingIntervalMilliseconds 5000

# Features
sv_enableNetworkedSounds true
sv_enableNetworkedPhoneExplosions false
sv_voiceChat true
sv_mumble true

# OneSync
onesync on
onesync_enableInfinity true
onesync_population true
onesync_forceMigration true
onesync_distanceCulling true

# Rate Limiters
rateLimiter_challenge_rate 4
rateLimiter_challenge_burst 10
rateLimiter_handshake_rate 4
rateLimiter_handshake_burst 10

# txAdmin
txAdmin-menuEnabled true
txAdmin-menuAlignRight false
txAdmin-menuPageKey Tab
```

### Resource Management

```ac
# Start resources
ensure mapmanager
ensure chat
ensure spawnmanager
ensure baseevents
ensure hardcap
ensure rconlog

# Resource lifecycle
start mapmanager
stop chat
restart chat
```

### Access Control (ACL)

```ac
# Add ACE permissions
add_ace group.admin command allow
add_ace group.admin txAdmin.kick allow
add_ace group.admin txAdmin.ban allow
add_ace group.admin txAdmin.warn allow

# Remove ACE permissions
remove_ace group.admin command

# Add principals
add_principal identifier.license:abc123 group.admin
add_principal identifier.steam:1234567890 group.admin
add_principal identifier.discord:1234567890 group.admin

# Remove principals
remove_principal identifier.license:abc123 group.admin

# Test ACE permissions
test_ace group.admin command
```

### Event Blocking

```ac
# Block net game events
block_net_game_event "eventName"

# Unblock net game events
unblock_net_game_event "eventName"
```

### Network Configuration

```ac
# Endpoints
endpoint_add_tcp "0.0.0.0:30120"
endpoint_add_udp "0.0.0.0:30120"

# Console filters
con_addChannelFilter "channel"
con_removeChannelFilter "channel"

# Server icon
load_server_icon "path/to/icon.png"

# Recording
sync_start_recording "netId"
sync_stop_recording "netId"
replay_start
replay_stop
```

---

## Python SDK

### Core Classes

```python
from kit import Keywords, KeywordInfo, ParamInfo, Buffer, BufferConvert

# Keywords - All 225 FiveM keywords
print(Keywords.ALL)           # All keywords
print(Keywords.CVARS)         # Configuration variables
print(Keywords.ACTIONS)       # Action commands
print(Keywords.PRINCIPALS)    # Principal identifiers
print(Keywords.STATES)        # State values (allow/deny/true/false/on/off)

# KeywordInfo - Detailed keyword metadata
info = get_keyword_info("sv_hostname")
print(info.name)              # "sv_hostname"
print(info.type)              # "cvar"
print(info.category)          # "Server Identity"
print(info.description)       # "Server name displayed in the server list"
print(info.default)           # "CVK Realism"
print(info.warning)           # Deprecation warnings if any
print(info.params)            # Parameter information
print(info.usage)             # Usage examples
print(info.related)           # Related keywords
```

### Lookup Functions

```python
from kit import *

# Validation
is_valid_keyword("sv_hostname")     # True
is_valid_cvar("sv_hostname")        # True
is_valid_action("ensure")           # True
is_valid_principal("group.admin")   # True
is_valid_state("allow")             # True

# Token types
get_token_type("sv_hostname")       # "cvar"
get_token_type("ensure")            # "action"
get_token_type("group.admin")       # "principal"
get_token_type("allow")             # "state"

# Keyword info
get_keyword_name("sv_hostname")     # "sv_hostname"
get_keyword_desc("sv_hostname")     # "Server name displayed in the server list"
get_keyword_type("sv_hostname")     # "string"
get_keyword_default("sv_hostname")  # "CVK Realism"
get_keyword_category("sv_hostname") # "Server Identity"

# Search
search_keywords("hostname")        # ["sv_hostname"]
find_by_prefix("sv_")              # All sv_* convars
find_by_suffix("Rate")             # All *_Rate convars
find_by_category("Server Identity") # Keywords in category
find_deprecated()                   # Deprecated keywords
find_startup_only()                 # Startup-only keywords
```

### Identifier Helpers

```python
from kit import *

# Format identifiers
format_identifier("steam", "1234567890")  # "identifier.steam:1234567890"
format_identifier("license", "abc123")    # "identifier.license:abc123"
format_identifier("discord", "1234567890") # "identifier.discord:1234567890"

# Create identifiers
make_steam_id("76561198000000000")  # "identifier.steam:76561198000000000"
make_license_id("abc123")           # "identifier.license:abc123"
make_discord_id("1234567890")       # "identifier.discord:1234567890"
make_fivem_id("123456")             # "identifier.fivem:123456"
make_ip_id("127.0.0.1")            # "identifier.ip:127.0.0.1"
make_xbl_id("1234567890")          # "identifier.xbl:1234567890"

# Resolve identifier type
resolve_identifier_type("identifier.steam:123")  # "steam"
resolve_identifier_type("identifier.license:abc") # "license"

# Split identifier
split_identifier("identifier.steam:123")  # ("steam", "123")
```

### Category Getters

```python
from kit import *

# Get keyword categories
sv_convars = get_sv_convars()           # All sv_* convars
onesync_convars = get_onesync_convars() # All onesync_* convars
ratelimiter_convars = get_ratelimiter_convars()  # All rateLimiter_* convars

# Get principals
groups = get_group_principals()         # group.admin, group.user, etc.
identifiers = get_identifier_principals() # identifier.steam, etc.
resources = get_resource_principals()   # resource.mapmanager, etc.
commands = get_command_permissions()    # command.kick, etc.
txadmin = get_txadmin_permissions()     # txAdmin.kick, etc.
frameworks = get_framework_permissions() # qbcore.admin, etc.

# Get rate limiter pairs
pairs = get_ratelimiter_pairs()  # [(rate, burst), ...]
```

### Parsing and Building

```python
from kit import *

# Parse a line
parsed = parse_line("sv_hostname \"My Server\"")
# Returns: {"command": "sv_hostname", "args": ["My Server"]}

# Build a line
line = build_line("set", "sv_hostname", "\"My Server\"")
# Returns: "set sv_hostname \"My Server\""

# Parse and format values
parse_value("42")           # 42 (int)
parse_value("3.14")         # 3.14 (float)
parse_value("true")         # True (bool)
parse_value("\"hello\"")    # "hello" (string)

format_value(42)            # "42"
format_value(True)          # "true"
format_value("hello")       # "\"hello\""
```

---

## Builder Functions

Every keyword has a corresponding builder function. Functions use Python naming conventions (underscores instead of camelCase).

### Server Configuration

```python
from kit import *

# Server identity
sv_hostname("My Server")                    # set sv_hostname "My Server"
sv_maxClients(48)                           # set sv_maxClients 48
sv_maxclients(48)                           # set sv_maxClients 48 (lowercase alias)
sv_licenseKey("your_key")                   # set sv_licenseKey "your_key"
sv_lan(False)                               # set sv_lan false
sv_projectName("My Project")               # set sv_projectName "My Project"
sv_projectDesc("Description")              # set sv_projectDesc "Description"
sv_tebexSecret("secret")                   # set sv_tebexSecret "secret"
sv_enforceGameBuild(2944)                   # set sv_enforceGameBuild 2944
sv_scriptHookAllowed(True)                  # set sv_scriptHookAllowed 1
sv_endpointPrivacy(True)                    # set sv_endpointPrivacy true
sv_entityLockdown("none")                   # set sv_entityLockdown none
sv_pureLevel(0)                             # set sv_pureLevel 0

# Network
netPort(30120)                              # set netPort 30120
net_tcpConnLimit(1024)                      # set net_tcpConnLimit 1024
sv_tcpConnectionTimeoutSeconds(30)          # set sv_tcpConnectionTimeoutSeconds 30
sv_ioThreads(4)                             # set sv_ioThreads 4
sv_clientConnectingTimeoutMilliseconds(5000) # set sv_clientConnectingTimeoutMilliseconds 5000
sv_clientConnectedTimeoutMilliseconds(30000) # set sv_clientConnectedTimeoutMilliseconds 30000
sv_pingIntervalMilliseconds(5000)           # set sv_pingIntervalMilliseconds 5000
sv_endpoints("endpoint1,endpoint2")         # set sv_endpoints "endpoint1,endpoint2"
sv_listingIpOverride("1.2.3.4")            # set sv_listingIpOverride "1.2.3.4"
sv_listingHostOverride("my.server.com")    # set sv_listingHostOverride "my.server.com"
sv_registerMulticastDns(True)              # set sv_registerMulticastDns true
sv_proxyIPRanges("192.168.0.0/16")         # set sv_proxyIPRanges "192.168.0.0/16"

# Security
rcon_password("secure_password")            # rcon_password "secure_password"
sv_authMaxVariance(100)                     # set sv_authMaxVariance 100
sv_authMinTrust(50)                         # set sv_authMinTrust 50
sv_requestParanoia(0)                       # set sv_requestParanoia 0
sv_filterRequestControl(0)                  # set sv_filterRequestControl 0
sv_filterRequestControlSettleTimer(500)     # set sv_filterRequestControlSettleTimer 500
steam_webApiKey("your_api_key")            # set steam_webApiKey "your_api_key"
steam_webApiDomain("api.steampowered.com") # set steam_webApiDomain "api.steampowered.com"

# Features
sv_enableNetworkedSounds(True)              # set sv_enableNetworkedSounds true
sv_enableNetworkedPhoneExplosions(False)    # set sv_enableNetworkedPhoneExplosions false
sv_enableNetworkedScriptEntityStates(True)  # set sv_enableNetworkedScriptEntityStates true
sv_enableNetEventReassembly(True)           # set sv_enableNetEventReassembly true
sv_netEventReassemblyMaxPendingEvents(1024) # set sv_netEventReassemblyMaxPendingEvents 1024
sv_voiceChat(True)                          # set sv_voiceChat true
sv_mumble(True)                             # set sv_mumble true
sv_devMode(False)                           # set sv_devMode false
sv_useAccurateSends(True)                   # set sv_useAccurateSends true
sv_protectServerEntities(True)              # set sv_protectServerEntities true
sv_enhancedHostSupport(True)                # set sv_enhancedHostSupport true
sv_stateBagStrictMode(False)                # set sv_stateBagStrictMode false
sv_scriptDebugDuplicates(False)             # set sv_scriptDebugDuplicates false
sv_httpFileServerProxyOnly(False)           # set sv_httpFileServerProxyOnly false
sv_kvsName("default")                       # set sv_kvsName "default"
sv_master1("")                              # set sv_master1 ""
sv_replaceExeToSwitchBuilds(False)          # set sv_replaceExeToSwitchBuilds false
sv_showBusySpinnerOnLoadingScreen(False)    # set sv_showBusySpinnerOnLoadingScreen false
sv_endpointurl("")                          # set sv_endpointurl ""
sv_kick_players_cnl(True)                   # set sv_kick_players_cnl 1
sv_exposePlayerIdentifiersInHttpEndpoint(False) # set sv_exposePlayerIdentifiersInHttpEndpoint false
sv_allowlistInstructions("")                # set sv_allowlistInstructions ""
sv_appearAllowlisted(False)                 # set sv_appearAllowlisted false

# Game info
gamename("gta5")                            # gamename gta5
gametype("fivem")                           # gametype fivem
mapname("gta5")                             # mapname gta5
```

### OneSync Configuration

```python
from kit import *

onesync("on")                               # onesync on
onesync_enableInfinity(True)                # set onesync_enableInfinity true
onesync_enableBeyond(True)                  # set onesync_enableBeyond true
onesync_population(True)                    # set onesync_population true
onesync_forceMigration(True)                # set onesync_forceMigration true
onesync_distanceCulling(True)               # set onesync_distanceCulling true
onesync_distanceCullVehicles(True)          # set onesync_distanceCullVehicles true
onesync_radiusFrequency(True)               # set onesync_radiusFrequency true
onesync_migrateDataTimeout(5000)            # set onesync_migrateDataTimeout 5000
onesync_compressionDictionarySamples(True)  # set onesync_compressionDictionarySamples true
onesync_mapBoundsMinX(-2000)               # set onesync_mapBoundsMinX -2000
onesync_mapBoundsMinY(-2000)               # set onesync_mapBoundsMinY -2000
onesync_mapBoundsMaxX(4500)                # set onesync_mapBoundsMaxX 4500
onesync_mapBoundsMaxY(8000)                # set onesync_mapBoundsMaxY 8000
onesync_mapCellAreaSize(1000)              # set onesync_mapCellAreaSize 1000
```

### Resource Management

```python
from kit import *

ensure("mapmanager")                        # ensure mapmanager
ensure_stop("mapmanager")                   # ensure_stop mapmanager
start("mapmanager")                         # start mapmanager
stop("chat")                                # stop chat
restart("chat")                             # restart chat
quit()                                      # quit
refresh()                                   # refresh
say("Hello from server!")                   # say Hello from server!
exec("path/to/script.lua")                 # exec path/to/script.lua

# Server status
status()                                    # status
clientkick(43, "reason")                   # clientkick 43 reason
moo()                                       # set moo 31337

# Server icon
load_server_icon("path/to/icon.png")       # load_server_icon path/to/icon.png

# Pool management
increase_pool_size("ped", 100)             # increase_pool_size ped 100

# Recording
sync_start_recording("netId", "compressed") # sync_start_recording netId compressed
sync_stop_recording("netId")               # sync_stop_recording netId
replay_start                                # replay_start
replay_stop                                 # replay_stop
```

### Access Control (ACL)

```python
from kit import *

add_ace("group.admin", "command", "allow")           # add_ace group.admin command allow
add_ace("group.admin", "txAdmin.kick", "allow")     # add_ace group.admin txAdmin.kick allow
remove_ace("group.admin", "command")                 # remove_ace group.admin command
test_ace("group.admin", "command")                   # test_ace group.admin command

add_principal("identifier.license:abc123", "group.admin")  # add_principal identifier.license:abc123 group.admin
add_principal("identifier.steam:123", "group.admin")       # add_principal identifier.steam:123 group.admin
remove_principal("identifier.license:abc123", "group.admin") # remove_principal identifier.license:abc123 group.admin

block_net_game_event("eventName")          # block_net_game_event eventName
unblock_net_game_event("eventName")        # unblock_net_game_event eventName
```

### Network Configuration

```python
from kit import *

endpoint_add_tcp("0.0.0.0:30120")          # endpoint_add_tcp 0.0.0.0:30120
endpoint_add_udp("0.0.0.0:30120")          # endpoint_add_udp 0.0.0.0:30120

con_addChannelFilter("channel")            # con_addChannelFilter channel
con_removeChannelFilter("channel")         # con_removeChannelFilter channel
con_channelFilters                          # con_channelFilters
```

### Rate Limiters

```python
from kit import #

# Pair functions (sets both rate and burst)
rateLimiter_challenge(4, 10)               # ['set rateLimiter_challenge_rate 4', 'set rateLimiter_challenge_burst 10']
rateLimiter_handshake(4, 10)               # ['set rateLimiter_handshake_rate 4', 'set rateLimiter_handshake_burst 10']
rateLimiter_handshakeUDP(1, 5)             # ['set rateLimiter_handshakeUDP_rate 1', 'set rateLimiter_handshakeUDP_burst 5']
rateLimiter_http_dynamic(4, 10)            # ['set rateLimiter_http_dynamic_rate 4', 'set rateLimiter_http_dynamic_burst 10']
rateLimiter_http_info(4, 10)               # ['set rateLimiter_http_info_rate 4', 'set rateLimiter_http_info_burst 10']
rateLimiter_http_perf(2, 5)                # ['set rateLimiter_http_perf_rate 2', 'set rateLimiter_http_perf_burst 5']
rateLimiter_http_players(4, 10)            # ['set rateLimiter_http_players_rate 4', 'set rateLimiter_http_players_burst 10']
rateLimiter_netCommand(7, 14)              # ['set rateLimiter_netCommand_rate 7', 'set rateLimiter_netCommand_burst 14']
rateLimiter_netCommandFlood(25, 45)        # ['set rateLimiter_netCommandFlood_rate 25', 'set rateLimiter_netCommandFlood_burst 45']
rateLimiter_netCommandSize(1024, 8192)     # ['set rateLimiter_netCommandSize_rate 1024', 'set rateLimiter_netCommandSize_burst 8192']
rateLimiter_netEvent(50, 200)              # ['set rateLimiter_netEvent_rate 50', 'set rateLimiter_netEvent_burst 200']
rateLimiter_netEventFlood(75, 300)         # ['set rateLimiter_netEventFlood_rate 75', 'set rateLimiter_netEventFlood_burst 300']
rateLimiter_rcon(2, 5)                     # ['set rateLimiter_rcon_rate 2', 'set rateLimiter_rcon_burst 5']
rateLimiter_res_http_handler(10, 25)       # ['set rateLimiter_res_http_handler_rate 10', 'set rateLimiter_res_http_handler_burst 25']
rateLimiter_resourceList(10, 25)           # ['set rateLimiter_resourceList_rate 10', 'set rateLimiter_resourceList_burst 25']
rateLimiter_stateBag(75, 125)              # ['set rateLimiter_stateBag_rate 75', 'set rateLimiter_stateBag_burst 125']
rateLimiter_stateBagFlood(150, 175)        # ['set rateLimiter_stateBagFlood_rate 150', 'set rateLimiter_stateBagFlood_burst 175']
rateLimiter_stateBagSize(131072, 262144)   # ['set rateLimiter_stateBagSize_rate 131072', 'set rateLimiter_stateBagSize_burst 262144']

# Set all rate limiters at once
rateLimiter_all()                           # ['set rateLimiter_challenge_rate 4', ...]

# Individual convar functions
rateLimiter_challenge_rate(4)               # set rateLimiter_challenge_rate 4
rateLimiter_challenge_burst(10)             # set rateLimiter_challenge_burst 10
rateLimiter_handshake_rate(4)               # set rateLimiter_handshake_rate 4
rateLimiter_handshake_burst(10)             # set rateLimiter_handshake_burst 10
# ... (36 total individual convars)
```

### txAdmin Configuration

```python
from kit import *

txAdmin_menuEnabled(True)                   # set txAdmin-menuEnabled true
txAdmin_menuAlignRight(False)               # set txAdmin-menuAlignRight false
txAdmin_menuPageKey("Tab")                 # set txAdmin-menuPageKey Tab
txAdmin_hideDefaultAnnouncement(False)      # set txAdmin-hideDefaultAnnouncement false
txAdmin_hideDefaultDirectMessage(False)     # set txAdmin-hideDefaultDirectMessage false
txAdmin_hideDefaultWarning(False)           # set txAdmin-hideDefaultWarning false
txAdmin_hideDefaultScheduledRestartWarning(False) # set txAdmin-hideDefaultScheduledRestartWarning false
txAdmin_debugMode(False)                    # setr txAdmin-debugMode false
txAdmin_menuPlayerIdDistance(150)           # setr txAdmin-menuPlayerIdDistance 150
txAdmin_menuDrunkDuration(0)               # setr txAdmin-menuDrunkDuration 0
```

### The `use_set` Parameter

Every convar function accepts a `use_set` keyword argument to control whether the `set` prefix is included:

```python
from kit import *

# Default: with set prefix
sv_hostname("My Server")                    # set sv_hostname "My Server"
sv_maxClients(64)                           # set sv_maxClients 64
sv_lan(True)                                # set sv_lan true

# Without set prefix
sv_hostname("My Server", use_set=False)     # sv_hostname "My Server"
sv_maxClients(64, use_set=False)            # sv_maxClients 64
sv_lan(True, use_set=False)                 # sv_lan true

# Set commands
set("myConvar", "value")                    # set myConvar value
set("myConvar", "value", use_set=False)     # myConvar value

setr("myConvar", "value")                   # setr myConvar value
setr("myConvar", "value", use_set=False)    # myConvar value

sets("myConvar", "value")                   # sets myConvar value
sets("myConvar", "value", use_set=False)    # myConvar value
```

### Batch Functions

```python
from kit import *

# Generate default resource ensures
batch_default_ensures()
# ['ensure mapmanager', 'ensure chat', 'ensure spawnmanager',
#  'ensure sessionmanager', 'ensure basic-gamemode', 'ensure hardcap',
#  'ensure rconlog', 'ensure baseevents']

# Generate admin permissions
batch_admin_permissions()
# ['add_ace group.admin command allow', 'add_ace group.admin txAdmin.kick allow', ...]

# Generate ensures for specific resources
batch_ensures("mapmanager", "chat", "my_resource")
# ['ensure mapmanager', 'ensure chat', 'ensure my_resource']

# Generate standard server config
batch_standard_server_config("My Server", 48, "license_key")
# ['set sv_hostname "My Server"', 'set sv_maxClients 48',
#  'set sv_licenseKey "license_key"', 'set netPort 30120',
#  'endpoint_add_tcp 0.0.0.0:30120']

# Generate OneSync config
batch_standard_onesync(64)
# ['onesync on', 'set onesync_enableInfinity true',
#  'set onesync_population true', 'set onesync_forceMigration true',
#  'set onesync_distanceCulling true', 'set onesync_radiusFrequency true']

# Generate identifier principals
batch_identifier_steam("76561198000000000", "group.admin")
# ['add_principal identifier.steam:76561198000000000 group.admin']

batch_identifier_license("abc123", "group.admin")
# ['add_principal identifier.license:abc123 group.admin']

batch_identifier_discord("1234567890", "group.admin")
# ['add_principal identifier.discord:1234567890 group.admin']
```

### Principal Constants

```python
from kit import *

# Built-in
PRINCIPAL_EVERYONE                          # "builtin.everyone"
PRINCIPAL_RESTRICTED                        # "builtin.restricted"

# Groups
PRINCIPAL_GROUP_ADMIN                       # "group.admin"
PRINCIPAL_GROUP_MODERATOR                   # "group.moderator"
PRINCIPAL_GROUP_OWNER                       # "group.owner"
PRINCIPAL_GROUP_USER                        # "group.user"
PRINCIPAL_GROUP_SUPPORT                     # "group.support"
PRINCIPAL_GROUP_HELPER                      # "group.helper"
PRINCIPAL_GROUP_GOD                         # "group.god"
PRINCIPAL_GROUP_SUPERADMIN                  # "group.superadmin"
PRINCIPAL_GROUP_DEVELOPER                   # "group.developer"

# Identifiers
PRINCIPAL_IDENTIFIER_STEAM                  # "identifier.steam"
PRINCIPAL_IDENTIFIER_LICENSE                # "identifier.license"
PRINCIPAL_IDENTIFIER_DISCORD                # "identifier.discord"
PRINCIPAL_IDENTIFIER_FIVEM                  # "identifier.fivem"
PRINCIPAL_IDENTIFIER_IP                     # "identifier.ip"
PRINCIPAL_IDENTIFIER_XBL                    # "identifier.xbl"

# Resources
PRINCIPAL_RESOURCE_MAPMANAGER               # "resource.mapmanager"
PRINCIPAL_RESOURCE_CHAT                     # "resource.chat"
PRINCIPAL_RESOURCE_SPAWNMANAGER             # "resource.spawnmanager"
PRINCIPAL_RESOURCE_SESSIONMANAGER           # "resource.sessionmanager"
PRINCIPAL_RESOURCE_HARDCAP                  # "resource.hardcap"
PRINCIPAL_RESOURCE_RCONLOG                  # "resource.rconlog"
PRINCIPAL_RESOURCE_BASEEVENTS               # "resource.baseevents"

# Bare Resources
PRINCIPAL_MAPMANAGER                        # "mapmanager"
PRINCIPAL_CHAT                              # "chat"
PRINCIPAL_SPAWNMANAGER                      # "spawnmanager"
PRINCIPAL_SESSIONMANAGER                    # "sessionmanager"
PRINCIPAL_BASIC_GAMEMODE                    # "basic-gamemode"
PRINCIPAL_HARDCAP                           # "hardcap"
PRINCIPAL_RCONLOG                           # "rconlog"
PRINCIPAL_BASEEVENTS                        # "baseevents"

# Commands
PRINCIPAL_COMMAND                           # "command"
PRINCIPAL_COMMAND_KICK                      # "command.kick"
PRINCIPAL_COMMAND_BAN                       # "command.ban"
PRINCIPAL_COMMAND_TEMPBAN                   # "command.tempban"
PRINCIPAL_COMMAND_SETGROUP                  # "command.setgroup"
PRINCIPAL_COMMAND_ADMIN                     # "command.admin"
PRINCIPAL_COMMAND_NOCLIP                    # "command.noclip"
PRINCIPAL_COMMAND_TPM                       # "command.tpm"
PRINCIPAL_COMMAND_BRING                     # "command.bring"
PRINCIPAL_COMMAND_REVIVE                    # "command.revive"
PRINCIPAL_COMMAND_HEAL                      # "command.heal"
PRINCIPAL_COMMAND_ANNOUNCE                  # "command.announce"
PRINCIPAL_COMMAND_CAR                       # "command.car"
PRINCIPAL_COMMAND_WEATHER                   # "command.weather"
PRINCIPAL_COMMAND_TIME                      # "command.time"
PRINCIPAL_COMMAND_QUIT                      # "command.quit"
PRINCIPAL_COMMAND_ADD_ACE                   # "command.add_ace"
PRINCIPAL_COMMAND_ADD_PRINCIPAL             # "command.add_principal"

# txAdmin
PRINCIPAL_TXADMIN_KICK                      # "txAdmin.kick"
PRINCIPAL_TXADMIN_BAN                       # "txAdmin.ban"
PRINCIPAL_TXADMIN_WARN                      # "txAdmin.warn"
PRINCIPAL_TXADMIN_PLAYERS_HEAL              # "txAdmin.players.heal"

# Frameworks
PRINCIPAL_QBCORE_ADMIN                      # "qbcore.admin"
PRINCIPAL_QBX_ADMIN                         # "qbx.admin"
PRINCIPAL_ESX_ADMIN                         # "esx.admin"
```

### String Constants

```python
from kit import *

# Built-in
builtin_everyone                            # "builtin.everyone"
builtin_restricted                          # "builtin.restricted"

# Groups
group_admin                                 # "group.admin"
group_moderator                             # "group.moderator"
group_owner                                 # "group.owner"
group_user                                  # "group.user"
group_support                               # "group.support"
group_helper                                # "group.helper"
group_god                                   # "group.god"
group_superadmin                            # "group.superadmin"
group_developer                             # "group.developer"

# Identifiers
identifier_steam                            # "identifier.steam"
identifier_license                          # "identifier.license"
identifier_discord                          # "identifier.discord"
identifier_fivem                            # "identifier.fivem"
identifier_ip                               # "identifier.ip"
identifier_xbl                              # "identifier.xbl"

# Resources
resource_mapmanager                         # "resource.mapmanager"
resource_chat                               # "resource.chat"
resource_spawnmanager                       # "resource.spawnmanager"
resource_sessionmanager                     # "resource.sessionmanager"
resource_hardcap                            # "resource.hardcap"
resource_rconlog                            # "resource.rconlog"
resource_baseevents                         # "resource.baseevents"

# Bare Resources
baseevents                                  # "baseevents"
basic_gamemode                              # "basic-gamemode"
chat                                        # "chat"
hardcap                                     # "hardcap"
mapmanager                                  # "mapmanager"
rconlog                                     # "rconlog"
sessionmanager                              # "sessionmanager"
spawnmanager                                # "spawnmanager"

# Commands
command_str                                 # "command"
command_add_ace                             # "command.add_ace"
command_add_principal                       # "command.add_principal"
command_admin                               # "command.admin"
command_announce                            # "command.announce"
command_ban                                 # "command.ban"
command_bring                               # "command.bring"
command_car                                 # "command.car"
command_heal                                # "command.heal"
command_kick                                # "command.kick"
command_noclip                              # "command.noclip"
command_quit                                # "command.quit"
command_revive                              # "command.revive"
command_setgroup                            # "command.setgroup"
command_tempban                             # "command.tempban"
command_time                                # "command.time"
command_tpm                                 # "command.tpm"
command_weather                             # "command.weather"

# txAdmin Permissions
txAdmin_kick                                # "txAdmin.kick"
txAdmin_ban                                 # "txAdmin.ban"
txAdmin_warn                                # "txAdmin.warn"
txAdmin_players_heal                        # "txAdmin.players.heal"

# Frameworks
qbcore_admin                                # "qbcore.admin"
qbx_admin                                   # "qbx.admin"
esx_admin                                   # "esx.admin"

# txAdmin ConVar Keywords
TXADMIN_MENU_ENABLED                        # "txAdmin-menuEnabled"
TXADMIN_MENU_ALIGN_RIGHT                    # "txAdmin-menuAlignRight"
TXADMIN_MENU_PAGE_KEY                       # "txAdmin-menuPageKey"
TXADMIN_HIDE_DEFAULT_ANNOUNCEMENT           # "txAdmin-hideDefaultAnnouncement"
TXADMIN_HIDE_DEFAULT_DIRECT_MESSAGE         # "txAdmin-hideDefaultDirectMessage"
TXADMIN_HIDE_DEFAULT_WARNING                # "txAdmin-hideDefaultWarning"
TXADMIN_HIDE_DEFAULT_SCHEDULED_RESTART_WARNING # "txAdmin-hideDefaultScheduledRestartWarning"
TXADMIN_DEBUG_MODE                          # "txAdmin-debugMode"
TXADMIN_MENU_PLAYER_ID_DISTANCE             # "txAdmin-menuPlayerIdDistance"
TXADMIN_MENU_DRUNK_DURATION                 # "txAdmin-menuDrunkDuration"
```

---

## Buffer Utilities

```python
from kit import *

# Constants
BYTE                                        # 1
KILOBYTE                                    # 1024
MEGABYTE                                    # 1048576
GIGABYTE                                    # 1073741824
TERABYTE                                    # 1099511627776

# Size constants
BUFFER_SIZE                                 # 4096
MAX_FILENAME_LEN                            # 255
MIN_FILENAME_LEN                            # 1
MAX_FILE_SIZE                               # 104857600
MAX_PACKET_SIZE                             # 1500
MAX_EVENT_SIZE                              # 16384
MAX_NET_EVENT_SIZE                          # 65536
MAX_STATEBAG_SIZE                           # 1048576
MAX_ENTITY_OWNERS                           # 64
MAX_CLIENTS                                 # 128
MAX_PLAYERS                                 # 256
MAX_RESOURCE_NAME                           # 128
MAX_IP_LEN                                  # 45
MAX_LICENSE_LEN                             # 512
MAX_DISCORD_LEN                             # 32
MAX_STEAM_LEN                               # 32
MAX_XBL_LEN                                 # 32
MAX_COMMAND_LEN                             # 128
MAX_CHAT_LEN                                # 256
MAX_CONVAR_LEN                              # 1024
MAX_HOSTNAME_LEN                            # 128
MAX_RESOURCE_PATH                           # 256
MAX_SCRIPT_PATH                             # 256
MAX_CFG_LINE                                # 4096
MAX_CFG_FILE                                # 1048576

# Conversion functions
to_bytes(42)                                # b'\x00\x00\x00*'
from_bytes(b'\x00\x00\x00*')              # 42
fmt_size(1048576)                           # "1.00 MB"
fmt_bits(1048576)                           # "8388608 bits"
fmt_bits_per_sec(1048576)                   # "8.00 Mbps"

# Validation functions
clamp(100, 0, 255)                          # 100
in_range(50, 0, 100)                        # True
is_valid_buffer(b"data")                    # True
is_valid_filename("file.txt")               # True
is_valid_cfg_line("sv_hostname \"test\"")   # True
is_valid_cfg_size(b"data")                  # True
is_valid_packet(b"data")                    # True
is_valid_hostname("My Server")              # True
is_valid_resource_name("chat")              # True
is_valid_convar_value("value")              # True
is_valid_command("kick")                    # True
is_valid_chat_msg("Hello!")                 # True

# Bit manipulation
chunks(b"data", 1024)                       # [b"data"]
align(42, 8)                                # 48
log2_floor(1024)                            # 10
log2_ceil(1000)                             # 10
next_power_of_2(1000)                       # 1024
prev_power_of_2(1000)                       # 512
popcount(42)                                # 3

# Buffer class
buf = Buffer(1024)                          # Create 1KB buffer
buf.write(b"Hello")                         # Write bytes
buf.read(5)                                 # Read 5 bytes
buf.seek(0)                                 # Seek to start
buf.tell()                                  # Current position
buf.size()                                  # Buffer size

# BufferConvert class
BufferConvert.bytes_to_str(b"Hello")        # "Hello"
BufferConvert.str_to_bytes("Hello")         # b"Hello"
BufferConvert.int_to_bytes(42)              # b'\x00\x00\x00*'
BufferConvert.bytes_to_int(b'\x00\x00\x00*') # 42
BufferConvert.float_to_bytes(3.14)          # bytes
BufferConvert.bytes_to_float(b"...")        # 3.14
BufferConvert.bool_to_bytes(True)           # b'\x01'
BufferConvert.bytes_to_bool(b'\x01')        # True
BufferConvert.hex_to_bytes("FF")            # b'\xff'
BufferConvert.bytes_to_hex(b'\xff')         # "FF"
BufferConvert.bin_to_bytes("01010101")      # b'\x55'
BufferConvert.bytes_to_bin(b'\x55')         # "01010101"
BufferConvert.base64_encode(b"Hello")       # "SGVsbG8="
BufferConvert.base64_decode("SGVsbG8=")     # b"Hello"
BufferConvert.json_to_bytes({"key": "val"}) # bytes
BufferConvert.bytes_to_json(b'{"key":"val"}') # {"key": "val"}
BufferConvert.pickle_to_bytes({"key": "val"}) # bytes
BufferConvert.bytes_to_pickle(b"...")       # {"key": "val"}
BufferConvert.ip_to_bytes("192.168.1.1")    # b'\xc0\xa8\x01\x01'
BufferConvert.bytes_to_ip(b'\xc0\xa8\x01\x01') # "192.168.1.1"
BufferConvert.mac_to_bytes("00:11:22:33:44:55") # b'\x00\x11\x22\x33\x44\x55'
BufferConvert.bytes_to_mac(b'\x00\x11\x22\x33\x44\x55') # "00:11:22:33:44:55"
BufferConvert.bits_to_bytes(8)              # 1
BufferConvert.bytes_to_bits(1)              # 8
```

---

## VS Code Extension

### Installation

```bash
# Clone the repository
git clone https://github.com/n11kol11c/acelang.git
cd acelang/packages/vscode

# Run installer
./install.sh        # macOS / Linux
install.bat         # Windows
```

### Features

- **Syntax Highlighting** - Full TextMate grammar for `.ac` files
- **Comment Toggling** - `Ctrl+/` for single-line, `Shift+Alt+A` for block comments
- **Bracket Matching** - Automatic bracket and quote closing
- **Color Customization** - Configurable token colors via `settings.json`

### Color Customization

Customize syntax colors in VS Code `settings.json`:

```json
{
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "keyword.command.server.acelang",
                "settings": { "foreground": "#ff6b9d" }
            },
            {
                "scope": "keyword.command.resource.acelang",
                "settings": { "foreground": "#ff6b9d" }
            },
            {
                "scope": "keyword.control.directive.acelang",
                "settings": { "foreground": "#ff6b9d" }
            },
            {
                "scope": "keyword.control.flow.acelang",
                "settings": { "foreground": "#c586c0" }
            },
            {
                "scope": "support.type.principal.acelang",
                "settings": { "foreground": "#4ec9b0" }
            },
            {
                "scope": "support.type.identifier.acelang",
                "settings": { "foreground": "#4ec9b0" }
            },
            {
                "scope": "support.type.resource.acelang",
                "settings": { "foreground": "#4ec9b0" }
            },
            {
                "scope": "string.quoted.double.acelang",
                "settings": { "foreground": "#ce9178" }
            },
            {
                "scope": "string.quoted.single.acelang",
                "settings": { "foreground": "#ce9178" }
            },
            {
                "scope": "comment.line.number-sign.acelang",
                "settings": { "foreground": "#6a9955", "fontStyle": "italic" }
            },
            {
                "scope": "comment.block.acelang",
                "settings": { "foreground": "#6a9955", "fontStyle": "italic" }
            },
            {
                "scope": "constant.numeric.integer.acelang",
                "settings": { "foreground": "#b5cea8" }
            },
            {
                "scope": "constant.numeric.float.acelang",
                "settings": { "foreground": "#b5cea8" }
            },
            {
                "scope": "constant.language.boolean.acelang",
                "settings": { "foreground": "#569cd6" }
            },
            {
                "scope": "constant.character.escape.acelang",
                "settings": { "foreground": "#d7ba7d" }
            },
            {
                "scope": "keyword.operator.acelang",
                "settings": { "foreground": "#d4d4d4" }
            }
        ]
    }
}
```

---

## Project Structure

```
acelang/
├── packages/
│   ├── vscode/                          # VS Code Extension
│   │   ├── src/
│   │   │   └── extension.ts             # Extension entry point
│   │   ├── syntaxes/
│   │   │   └── acelang.tmLanguage.json  # TextMate grammar
│   │   ├── language-configuration.json  # Language configuration
│   │   ├── package.json                 # Extension manifest
│   │   ├── tsconfig.json                # TypeScript config
│   │   ├── install.sh                   # Unix installer
│   │   ├── install.bat                  # Windows installer
│   │   ├── test.ac                      # Test file
│   │   ├── configtest.ac                # Config test file
│   │   └── fivem_api_reference.ac       # API reference
│   │
│   └── cli/                             # Python SDK
│       ├── acelang/                     # Package source
│       │   ├── __init__.py              # Package init (521 exports)
│       │   ├── identifier.py            # 225 keywords + metadata
│       │   ├── parser.py                # Configuration parser
│       │   ├── validator.py             # Syntax validator
│       │   ├── buffer.py                # Buffer utilities
│       │   └── fivem_api.ac             # Complete API reference
│       ├── setup.py                     # Package setup
│       └── README.md                    # Package documentation
│
├── CONTRIBUTING.md                      # Contribution guidelines
├── LICENSE                              # MIT License
└── README.md                            # This file
```

---

## Development

### Prerequisites

- **Node.js** 18+ (for VS Code extension)
- **Python** 3.8+ (for SDK)
- **VS Code** (for extension development)

### VS Code Extension

```bash
cd packages/vscode
npm install
npm run compile
npm run watch
```

### Python SDK

```bash
cd packages/cli
pip install -e .
pip install -e ".[dev]"  # With dev dependencies
```

### Running Tests

```bash
# VS Code Extension
cd packages/vscode
npm test

# Python SDK
cd packages/cli
pytest
pytest --cov=acelang  # With coverage
```

### Code Style

**TypeScript:**
- Follow existing code style
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

**Python:**
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for public methods
- Keep functions focused and testable

---

## Contributing

Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Start

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add or update tests if applicable
5. Update documentation if needed
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep the first line under 72 characters
- Reference issues and pull requests where appropriate

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Built with ❤️ for the FiveM community
</p>
