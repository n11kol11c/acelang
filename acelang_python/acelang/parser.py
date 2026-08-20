"""
Parser for .ac (Acelang) config files
"""

import re
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class Command:
    """Represents a command in .ac file"""
    name: str
    args: List[str] = field(default_factory=list)
    line_number: int = 0
    raw_line: str = ""


@dataclass
class Comment:
    """Represents a comment in .ac file"""
    content: str
    line_number: int = 0
    is_multiline: bool = False


@dataclass
class Directive:
    """Represents a directive (@include, @from, etc.)"""
    name: str
    args: List[str] = field(default_factory=list)
    line_number: int = 0


class AcelangParser:
    """Parser for .ac config files"""
    
    # Comments
    SINGLE_LINE_COMMENT = re.compile(r'#.*$')
    MULTI_LINE_COMMENT_START = re.compile(r'/;')
    MULTI_LINE_COMMENT_END = re.compile(r';/')
    
    # Directives
    DIRECTIVE = re.compile(r'@(\w+)\s*(.*)')
    
    # Commands
    COMMAND = re.compile(r'^(\w+)\s*(.*)')
    
    # String patterns
    STRING_DOUBLE = re.compile(r'"([^"]*)"')
    STRING_SINGLE = re.compile(r"'([^']*)'")
    
    def __init__(self):
        self.commands: List[Command] = []
        self.comments: List[Comment] = []
        self.directives: List[Directive] = []
        self.errors: List[Dict[str, Any]] = []
    
    def parse_file(self, file_path: str) -> Dict[str, Any]:
        """Parse a .ac file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return self.parse(content)
    
    def parse(self, content: str) -> Dict[str, Any]:
        """Parse .ac content"""
        lines = content.split('\n')
        in_multiline_comment = False
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Handle multi-line comments
            if in_multiline_comment:
                if self.MULTI_LINE_COMMENT_END.search(line):
                    in_multiline_comment = False
                continue
            
            # Check for multi-line comment start
            if self.MULTI_LINE_COMMENT_START.search(line):
                in_multiline_comment = True
                continue
            
            # Skip empty lines
            if not line:
                continue
            
            # Check for single-line comment
            if line.startswith('#'):
                self.comments.append(Comment(
                    content=line[1:].strip(),
                    line_number=line_num
                ))
                continue
            
            # Check for directive
            directive_match = self.DIRECTIVE.match(line)
            if directive_match:
                name = directive_match.group(1)
                args_str = directive_match.group(2)
                args = self._parse_args(args_str)
                self.directives.append(Directive(
                    name=name,
                    args=args,
                    line_number=line_num
                ))
                continue
            
            # Check for command
            command_match = self.COMMAND.match(line)
            if command_match:
                name = command_match.group(1)
                args_str = command_match.group(2)
                args = self._parse_args(args_str)
                self.commands.append(Command(
                    name=name,
                    args=args,
                    line_number=line_num,
                    raw_line=line
                ))
                continue
            
            # If we get here, it's an error
            self.errors.append({
                'line': line_num,
                'content': line,
                'message': 'Invalid syntax'
            })
        
        return {
            'commands': self.commands,
            'comments': self.comments,
            'directives': self.directives,
            'errors': self.errors
        }
    
    def _parse_args(self, args_str: str) -> List[str]:
        """Parse command arguments"""
        args = []
        
        # Find all quoted strings
        double_quoted = self.STRING_DOUBLE.findall(args_str)
        single_quoted = self.STRING_SINGLE.findall(args_str)
        
        # Remove quoted strings from args_str to get unquoted args
        temp = self.STRING_DOUBLE.sub('', args_str)
        temp = self.STRING_SINGLE.sub('', temp)
        
        # Split unquoted args by whitespace
        unquoted = temp.split()
        
        # Combine all args
        args.extend(double_quoted)
        args.extend(single_quoted)
        args.extend(unquoted)
        
        return args
    
    def get_commands_by_name(self, name: str) -> List[Command]:
        """Get all commands with a specific name"""
        return [cmd for cmd in self.commands if cmd.name == name]
    
    def get_convars(self) -> List[Command]:
        """Get all convar commands (set, setr, sets)"""
        return [cmd for cmd in self.commands if cmd.name in ('set', 'setr', 'sets')]
    
    def get_resources(self) -> List[Command]:
        """Get all resource commands (ensure, start, stop, restart)"""
        return [cmd for cmd in self.commands if cmd.name in ('ensure', 'ensure_stop', 'start', 'stop', 'restart')]
    
    def get_ace_permissions(self) -> List[Command]:
        """Get all ACE permission commands (add_ace, remove_ace, test_ace)"""
        return [cmd for cmd in self.commands if cmd.name in ('add_ace', 'remove_ace', 'test_ace')]
    
    def get_principals(self) -> List[Command]:
        """Get all principal commands (add_principal, remove_principal)"""
        return [cmd for cmd in self.commands if cmd.name in ('add_principal', 'remove_principal')]
