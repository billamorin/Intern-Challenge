from google.appengine.ext import ndb
from models import Product


class Dao:

    def __init__(self):
        pass

    def fetch_product_id(self, product_id):
        product_data = {}
        ancestor_key = ndb.Key('Product', product_id)
        query = Product.query(ancestor=ancestor_key)
        query_results = query.fetch()
        if len(query_results) == 0:
            return None
        data = query_results[0]
        product_data.update(data.to_dict())
        return product_data

    def create_product(self, product_id, product_info):
        key = ndb.Key('Product', product_id)
        query_count = Product.query(Product.product_id == product_id).count(keys_only=True)
        if query_count > 0:
            return False
        db_entry = Product.entity_from_dict(parent_key=key, data_dict=product_info)
        db_entry.put()
        return True
