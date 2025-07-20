class Note:
    def __init__(self, key, content):
        if not key or not content:
            raise ValueError("Note key and content cannot be empty.")

        self.content = content
        self.key = key
        self.tags = []

    def add_tag(self, tag):
        if not tag:
            raise ValueError("Tag cannot be empty.")

        if len(tag.split()) > 2:
            raise ValueError("Tag must be a single word or two words maximum.")

        if tag in self.tags:
            raise ValueError(f"Tag '{tag}' already exists in the note.")

        self.tags.append(tag)
