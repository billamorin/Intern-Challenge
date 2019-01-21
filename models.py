from google.appengine.ext import ndb
import logging


class Product(ndb.Model):

    title = ndb.StringProperty()  # E.g., 'home', 'work'
    price = ndb.StringProperty()
    inventory_count = ndb.IntegerProperty()
    product_id = ndb.StringProperty()

    @classmethod
    def entity_from_dict(cls, parent_key, data_dict):
        valid_properties = {}
        for cls_property in cls._properties:
            if cls_property in data_dict:
                valid_properties.update({cls_property: data_dict[cls_property]})
        print(valid_properties)
        # logging.info(valid_properties)
        # Update the id from the data_dict
        if 'id' in data_dict:  # if creating a new entity
            valid_properties['id'] = data_dict['id']
        # Add the parent
        valid_properties['parent'] = parent_key
        try:
            entity = cls(**valid_properties)
            print(type(entity))
            return entity
        except Exception as e:
            logging.exception('Could not create entity \n' + repr(e))



