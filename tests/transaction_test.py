from os.path import exists

"""
Test for transactions. 
Test
"""

def test_transac_access(client):
    """Test for access to uploading file"""
    with client:
        client.post('/login', data=dict(email='dhyey@test.com', password='dhyeytest'))
        res = client.get('/transactions', follow_redirects=True)
        assert res.status_code == 200
        #assert b"Transactions" in res.data



file_exists = exists("./app/uploads/transactions.csv")
database_exists = exists("./database/db2.sqlite")

def test_checks_transactions_csv():
    """This checks if the csv file was uploaded"""
    assert file_exists == True

def test_checks_transactions_database():
    """This checks the database after the csv is processed """
    assert database_exists == True