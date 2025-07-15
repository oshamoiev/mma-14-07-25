def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: Contact '{e.args[0]}' is not found."
        except ValueError:
            return "Please provide valid data: name and phone number (or date for birthdays)."
        except IndexError:
            return "Please enter the required arguments (e.g., a user name)."
        except TypeError:
            return "Invalid input format or missing arguments."
        except Exception as e:
            return "An unexpected error occurred. Please try again."

    return inner
