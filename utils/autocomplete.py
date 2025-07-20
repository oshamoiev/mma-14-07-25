import sys

try:
    import readline  
except ImportError:
    if sys.platform.startswith("win"):
        try:
            import pyreadline3 as readline
        except ImportError:
            print("Autocomplete not available. Install pyreadline3.")
            readline = None
    else:
        print("Autocomplete not available.")
        readline = None


def get_completer(commands):
    def completer(text, state):
        options = [cmd for cmd in commands if cmd.startswith(text)]
        if state < len(options):
            return options[state]
        return None

    return completer


def setup_autocomplete(commands):
    if readline:
        readline.parse_and_bind("tab: complete")
        readline.set_completer(get_completer(commands))