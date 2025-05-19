from department import Department
from __init__ import CURSOR, CONN
import pytest


class TestDepartment:
    '''Class Department in department.py'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''drop table prior to each test.'''
        CURSOR.execute("DROP TABLE IF EXISTS departments")

    def test_creates_table(self):
        '''contains method "create_table()" that creates table "departments" if it does not exist.'''

       

    def test_drops_table(self):
        '''contains method "drop_table()" that drops table "departments" if it exists.'''

        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

        
        sql_table_names = """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='departments'
        """
        result = CURSOR.execute(sql_table_names).fetchone()
        
    def test_saves_department(self):
        '''contains method "save()" that saves a Department instance to the db and assigns the instance an id.'''

        
        department = Department("Payroll", "Building A, 5th Floor")
        

        sql = """
            SELECT * FROM departments
        """
        

    def test_creates_department(self):
        '''contains method "create()" that creates a new row in the db using parameter data and returns a Department instance.'''

        
        

        sql = """
            SELECT * FROM departments
        """
        

    def test_updates_row(self):
        '''contains a method "update()" that updates an instance's corresponding db row to match its new attribute values.'''
        

        
        
        

        # Assign new values for name and location
        

        # Persist the updated name and location values
       
        # assert department1 row was not updated, department1 object state not updated
        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        
        # assert department2 row was updated, department2 object state is correct
        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        

    def test_deletes_record(self):
        '''contains a method "delete()" that deletes the instance's corresponding db row'''
        

        
       

       

        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        
        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
       