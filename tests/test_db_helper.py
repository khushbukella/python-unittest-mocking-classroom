import unittest
from unittest import TestCase, mock
from unittest.mock import patch
from src.db_helper import DbHelper
import mysql.connector as sql

#%%


class Test_Db_Helper(TestCase):
    def setUp(self):
        pass

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self,MockDbHelper):
        db_helper = MockDbHelper()
        with patch('src.db_helper.DbHelper', attr_or_replacement=True):
            db_helper.get_maximum_salary.return_value=1000
            db_helper.get_minimum_salary.return_value=100
            self.assertGreater(db_helper.get_maximum_salary(),db_helper.get_minimum_salary())


if __name__ =='__main__':
    unittest.main()