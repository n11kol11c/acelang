from _components.identifier import _G
from _components.identifier import *

print("=== Test Results ===")
print(f"Total keywords: {len(_G.ALL)}")
print(f"Stats: {get_stats()}")
print(f"build_hostname: {build_hostname('My Server')}")

# Test keyword lookup
info = _G.META.get("svgui")
print(f"svgui: {info}")

# Test deprecated
print(setr("vmenu_stuff", "allow"))
print(sv_maxClients(32, use_set=False))
print(onesync_compressionDictionarySamples(False, use_set=False))
print(gamename("GTAV"))
print(add_principal(group_admin, identifier_license + ":102859758"))
print(get_all_lines())