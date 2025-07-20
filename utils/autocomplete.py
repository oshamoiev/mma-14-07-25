import readline


def get_completer(commands):
    def completer(text, state):
        options = [cmd for cmd in commands if cmd.startswith(text)]
        if state < len(options):
            return options[state]
        return None

    return completer


def setup_autocomplete(commands):
    readline.parse_and_bind("tab: complete")
    readline.set_completer(get_completer(commands))
