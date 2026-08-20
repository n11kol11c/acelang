"""
Validator for .ac (Acelang) config files
"""

from typing import List, Dict, Any
from .parser import AcelangParser, Command


class AcelangValidator:
    """Validator for .ac config files"""
    
    # Valid server commands
    VALID_SERVER_COMMANDS = {
        'set', 'setr', 'sets', 'add_ace', 'remove_ace', 'test_ace',
        'add_principal', 'remove_principal', 'add_group', 'alias', 'jmp',
        'exec', 'refresh', 'quit', 'say', 'status', 'clientkick', 'svgui',
        'gamename', 'gametype', 'mapname', 'netPort', 'net_tcpConnLimit',
        'block_net_game_event', 'unblock_net_game_event',
        'con_channelFilters', 'con_addChannelFilter', 'con_removeChannelFilter',
        'increase_pool_size', 'sync_start_recording', 'sync_stop_recording',
        'replay_start', 'replay_stop'
    }
    
    # Valid resource commands
    VALID_RESOURCE_COMMANDS = {
        'ensure', 'ensure_stop', 'start', 'stop', 'restart'
    }
    
    # Valid convars (sv_*, onesync_*, steam_*, rateLimiter_*)
    VALID_CONVAR_PREFIXES = {
        'sv_', 'onesync_', 'steam_', 'rateLimiter_', 'netPort', 'net_tcpConnLimit'
    }
    
    # Valid principal patterns
    VALID_PRINCIPAL_PREFIXES = {
        'group.', 'builtin.', 'identifier.', 'resource.'
    }
    
    # Valid permission states
    VALID_PERMISSIONS = {'allow', 'deny', 'deny_socket'}
    
    def __init__(self):
        self.errors: List[Dict[str, Any]] = []
    
    def validate_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Validate a .ac file"""
        parser = AcelangParser()
        result = parser.parse_file(file_path)
        return self.validate(result)
    
    def validate(self, parse_result: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Validate parsed .ac content"""
        self.errors = []
        
        for command in parse_result['commands']:
            self._validate_command(command)
        
        return self.errors
    
    def _validate_command(self, command: Command):
        """Validate a single command"""
        name = command.name
        
        # Check if it's a valid command
        if name not in self.VALID_SERVER_COMMANDS and name not in self.VALID_RESOURCE_COMMANDS:
            # Check if it's a valid convar
            is_valid_convar = any(name.startswith(prefix) for prefix in self.VALID_CONVAR_PREFIXES)
            
            if not is_valid_convar:
                self.errors.append({
                    'line': command.line_number,
                    'command': name,
                    'message': f'Unknown command: {name}'
                })
        
        # Validate specific commands
        if name == 'add_ace' or name == 'remove_ace':
            self._validate_ace_command(command)
        elif name == 'add_principal' or name == 'remove_principal':
            self._validate_principal_command(command)
        elif name in ('set', 'setr', 'sets'):
            self._validate_convar_command(command)
    
    def _validate_ace_command(self, command: Command):
        """Validate add_ace/remove_ace command"""
        if len(command.args) < 3:
            self.errors.append({
                'line': command.line_number,
                'command': command.name,
                'message': f'{command.name} requires 3 arguments: principal, object, permission'
            })
            return
        
        # Check principal
        principal = command.args[0]
        if not any(principal.startswith(prefix) for prefix in self.VALID_PRINCIPAL_PREFIXES):
            self.errors.append({
                'line': command.line_number,
                'command': command.name,
                'message': f'Invalid principal: {principal}'
            })
        
        # Check permission
        permission = command.args[2]
        if permission not in self.VALID_PERMISSIONS:
            self.errors.append({
                'line': command.line_number,
                'command': command.name,
                'message': f'Invalid permission: {permission}. Must be allow, deny, or deny_socket'
            })
    
    def _validate_principal_command(self, command: Command):
        """Validate add_principal/remove_principal command"""
        if len(command.args) < 2:
            self.errors.append({
                'line': command.line_number,
                'command': command.name,
                'message': f'{command.name} requires 2 arguments: child, parent'
            })
            return
        
        # Check child
        child = command.args[0]
        if not any(child.startswith(prefix) for prefix in self.VALID_PRINCIPAL_PREFIXES):
            self.errors.append({
                'line': command.line_number,
                'command': command.name,
                'message': f'Invalid child principal: {child}'
            })
        
        # Check parent
        parent = command.args[1]
        if not any(parent.startswith(prefix) for prefix in self.VALID_PRINCIPAL_PREFIXES):
            self.errors.append({
                'line': command.line_number,
                'command': command.name,
                'message': f'Invalid parent principal: {parent}'
            })
    
    def _validate_convar_command(self, command: Command):
        """Validate set/setr/sets command"""
        if len(command.args) < 2:
            self.errors.append({
                'line': command.line_number,
                'command': command.name,
                'message': f'{command.name} requires at least 2 arguments: name, value'
            })
