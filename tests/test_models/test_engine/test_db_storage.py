from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import unittest
import MySQLdb


class TestDBStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    def test_01(self):
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user='hbnb_test',
                             passwd='hbnb_test_pwd',
                             db='hbnb_test_db',
                             charset='utf8')
        cur = db.cursor()
        cur.execute("""
        INSERT INTO states (id, created_at, updated_at, name)
        VALUES (1, '2017-11-10 00:53:19', '2017-11-10 00:53:19', "California")
        """)
        cur.execute('SELECT * FROM states')
        rows = cur.fetchall()
        self.assertTrue(len(rows), 1)
        cur.close()
        db.close()


if __name__ == "__main__":
    unittest.main()
