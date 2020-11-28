class Mapper:
    """This module takes a user-input string and chunks it into formatted tuples which
contains relevant data for all essential pieces of string."""

    def maptolist(self, arg, langbound):
        # Returns formatted-tuple containing relevant data
        return langbound.split(arg)