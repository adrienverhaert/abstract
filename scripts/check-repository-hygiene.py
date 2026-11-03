"""Reject machine-local assistant instructions and credential files in Git."""
import re
import subprocess
import sys
from pathlib import PurePosixPath

INTERNAL_DIRS = {'.ai', '.agents', '.claude', '.codex', '.claude-plugin', '.codex-plugin', '.cursor', '.windsurf', '.continue'}
INTERNAL_FILES = {'agents.md', 'claude.md', 'gemini.md', 'skill.md', 'copilot-instructions.md', '.cursorrules', '.windsurfrules', '.clinerules'}


def private_path(path):
    parts = [part.lower() for part in PurePosixPath(path).parts]
    name = parts[-1]
    assistant = name in INTERNAL_FILES or re.fullmatch(r'(agents|claude|gemini)\.[^.]+\.md', name)
    credentials = (name == '.env' or name.startswith('.env.')) and name != '.env.example'
    return any(part in INTERNAL_DIRS for part in parts) or bool(assistant) or credentials


def git(*args):
    return subprocess.check_output(['git', *args], text=True)


def main():
    if '--self-test' in sys.argv:
        assert private_path('nested/AGENTS.md')
        assert private_path('AGENTS.override.md')
        assert private_path('.claude-plugin/plugin.json')
        assert private_path('.github/copilot-instructions.md')
        assert private_path('.cursorrules')
        assert private_path('.ai/skills/workflow/SKILL.md')
        assert private_path('nested/.env.production')
        assert not private_path('.env.example')
        assert not private_path('docs/language.md')
        print('Repository hygiene self-checks passed.')
        return 0
    errors = []
    for path in git('ls-files', '-z').split('\0'):
        if path and private_path(path):
            errors.append('Local-only file is tracked: ' + path)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('No machine-local instruction or credential files are tracked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
