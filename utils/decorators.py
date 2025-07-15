def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: Contact '{e.args[0]}' is not found."
        except ValueError as e:
            return e
        except TypeError:
            return "Invalid input format or missing arguments."
        except Exception as e:
            return "An unexpected error occurred. Please try again."

    return inner
