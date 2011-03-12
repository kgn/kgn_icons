size = 32
extension = 'png'
choplist = 'icons.choplist'
icons = (
    ('green', 'add', 'up', 'down', 'check'),
    ('blue', 'refresh', 'revert', 'question', 'information', 'active'),
    ('red', 'deny', 'remove', 'delete', 'exclamation'),
    ('sign', 'push', 'pull', 'merge', 'branch', 'block', 'pause', 'warning'),
    ('window', 'terminal', 'revision', 'diff', 'compare', 'appearance', 'quicklook'),
    ('file', 'commit_file', 'remove_file', 'commit_files', 'add_remove_files', 'watch_file', 'attach_files'),
    ('clone', 'revert_to_revision', 'revert_to_head', 'reveal_in_finder', 'incoming', 'outgoing', 'left_arrow', 'right_arrow'),
    ('tag', 'preferences', 'preferences2', 'expand_all', 'mercurial', 'color', 'sound', 'user'),
    ('globe', 'bad_connection', 'good_connection', 'update', 'twitter', 'cloudapp', 'dribbble')
)

import plistlib

y = 0
plist = []
for row in icons:
    x = 0
    for icon in row:
        plist.append({
            'name': icon,
            'extension': extension,
            'x': x,
            'y': y,
            'width': size,
            'height': size
        })
        x += size
    y += size
plistlib.writePlist(plist, choplist)