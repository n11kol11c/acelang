import * as vscode from 'vscode';

// const COMMANDS = [
//   'setr', 'set', 'sets', 'add_ace', 'remove_ace', 'test_ace',
//   'add_principal', 'remove_principal', 'ensure', 'ensure_stop',
//   'start', 'stop', 'restart', 'exec',
//   'endpoint_add_tcp', 'endpoint_add_udp', 'load_server_icon',
//   'sv_hostname', 'sv_maxclients', 'sv_licenseKey', 'sv_scriptHookAllowed',
//   'sv_endpointPrivacy', 'sv_enforceGameBuild', 'sv_master1',
//   'sv_scriptDebugDuplicates', 'rcon_password', 'onesync'
// ];

// const DIRECTIVES = [
//   '@include', '@from', '@include_once', '@mod', '@stub',
//   '@include_mod', '@include_stub', '@init'
// ];

// const FLOW_KEYWORDS = [
//   'if', 'else', 'elif', 'for', 'while', 'ret', 'brk',
//   'break', 'continue', 'pass', 'jmp'
// ];

// const SPECIAL_WORDS = [
//   'setr', 'set', 'add_principal', 'add_ace', 'remove_ace',
//   'remove_principal', 'test_ace', 'add_group', 'alias', 'jmp', 'exec',
//   'ensure', 'ensure_stop'
// ];

// const RESOURCES = [
//   'mapmanager', 'chat', 'spawnmanager', 'sessionmanager',
//   'basic-gamemode', 'hardcap', 'rconlog'
// ];

// const PRINCIPALS = [
//   'group.admin', 'group.moderator', 'group.owner', 'group.user',
//   'group.support', 'group.helper', 'group.god', 'group.superadmin',
//   'group.developer', 'builtin.everyone', 'builtin.restricted'
// ];

// const IDENTIFIERS = [
//   'identifier.steam:', 'identifier.license:', 'identifier.discord:',
//   'identifier.fivem:', 'identifier.ip:', 'identifier.xbl:'
// ];

// const TXADMIN_PERMS = [
//   'txAdmin.kick', 'txAdmin.ban', 'txAdmin.warn', 'txAdmin.players.heal'
// ];

// const FRAMEWORK_PERMS = [
//   'qbcore.admin', 'qbx.admin', 'esx.admin'
// ];

// const COMMON_COMMANDS = [
//   'command.kick', 'command.ban', 'command.tempban', 'command.setgroup',
//   'command.admin', 'command.noclip', 'command.tpm', 'command.bring',
//   'command.revive', 'command.heal', 'command.announce', 'command.car',
//   'command.weather', 'command.time', 'command.quit', 'command'
// ];

// const PERMISSION_STATES = ['allow', 'deny', 'deny_socket'];

// const BOOL_VALUES = ['true', 'false', 'on', 'off'];

// function makeItem(label: string, kind: vscode.CompletionItemKind, detail: string): vscode.CompletionItem {
//   const item = new vscode.CompletionItem(label, kind);
//   item.detail = detail;
//   return item;
// }

export function activate(context: vscode.ExtensionContext) {
  // const provider = vscode.languages.registerCompletionItemProvider('acelang', {
  //   provideCompletionItems(document: vscode.TextDocument, position: vscode.Position) {
  //     const items: vscode.CompletionItem[] = [];

  //     for (const cmd of COMMANDS) {
  //       items.push(makeItem(cmd, vscode.CompletionItemKind.Function, 'FiveM command'));
  //     }
  //     for (const kw of SPECIAL_WORDS) {
  //       items.push(makeItem(kw, vscode.CompletionItemKind.Function, 'special command'));
  //     }
  //     for (const d of DIRECTIVES) {
  //       items.push(makeItem(d, vscode.CompletionItemKind.Keyword, 'directive'));
  //     }
  //     for (const f of FLOW_KEYWORDS) {
  //       items.push(makeItem(f, vscode.CompletionItemKind.Keyword, 'flow control'));
  //     }
  //     for (const p of PRINCIPALS) {
  //       items.push(makeItem(p, vscode.CompletionItemKind.Value, 'principal'));
  //     }
  //     for (const id of IDENTIFIERS) {
  //       items.push(makeItem(id, vscode.CompletionItemKind.Struct, 'identifier'));
  //     }
  //     for (const r of RESOURCES) {
  //       items.push(makeItem(r, vscode.CompletionItemKind.Module, 'resource'));
  //     }
  //     for (const t of TXADMIN_PERMS) {
  //       items.push(makeItem(t, vscode.CompletionItemKind.Enum, 'txAdmin permission'));
  //     }
  //     for (const fw of FRAMEWORK_PERMS) {
  //       items.push(makeItem(fw, vscode.CompletionItemKind.Enum, 'framework permission'));
  //     }
  //     for (const c of COMMON_COMMANDS) {
  //       items.push(makeItem(c, vscode.CompletionItemKind.Enum, 'permission object'));
  //     }
  //     for (const s of PERMISSION_STATES) {
  //       items.push(makeItem(s, vscode.CompletionItemKind.EnumMember, 'permission state'));
  //     }
  //     for (const b of BOOL_VALUES) {
  //       items.push(makeItem(b, vscode.CompletionItemKind.Value, 'boolean'));
  //     }

  //     return items;
  //   }
  // }, '.', '@', ':' , ' ');

  // context.subscriptions.push(provider);
}

export function deactivate() {}
