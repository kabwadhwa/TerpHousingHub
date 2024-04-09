""" 
This script allows for UMD students to browse through studnet housing 
options and leave reviews for their current housing.
"""
class Hub:
    """ A class that represents a collection of housing options

    Attributes:
        Housing (list of Properties): a list containing all the
            properties currently in our database of hosing options.
    """

    def add_listing(address, on_off, apply):
        """ Creates a new Property object and adds it to the Housing list.

        Args:
            address (string): the addres of the listing
            on_campus (bool): True if the property is on campus, False otherwise
            apply (string): information on how to apply for listed property
        """
        pass

class Property:
    """ A class that represents single property listing

    Attributes:
        address (string) : the address of the listed property
        ratings (list of floats) : list of ratings (a number 1-5) given by past tennents
        on-campus (bool): true if the listing in on campus, false if listing is off-campus
        apply (string): url or email to apply for the residence
        
    """
    def add_rating(self, rating):
        """ Allows for someone to rate a property. Rating is added to the ratings attribute

        Args:
            rating (float): a number 1-5 that represents a person's experience 
            living at this residence
        """
        pass

    def avg_rating(self):
        """ Calculates the average rating of a property

        Returns:
            return a float average of the ratings associated with this property
        """
        pass