from os.path import exists

file_exists = exists("./app/uploads/music.csv")
database_exists = exists("./database/db2.sqlite")

def test_checks_csv():
    """This checks if the csv file was uploaded"""
    assert file_exists == True

def test_checks_database():
    """This checks the database after the csv is processed """
    assert database_exists == True
