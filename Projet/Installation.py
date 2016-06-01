"""
Installation class
"""

class Installation:

    """
    Installation class constructor
    """

    def __init__(self, id, name, streetNumber,street, postcode, city, latitude, longitude):
        self.id = id
        self.name = name
        self.streetNumber = streetNumber
        self.street = street
        self.postcode = postcode
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
