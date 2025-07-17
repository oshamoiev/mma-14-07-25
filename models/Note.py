class Note:
    def __init__(self, key, content):
        if not key or not content:
            raise ValueError("Note key and content cannot be empty.")

        self.content = content
        self.key = key
