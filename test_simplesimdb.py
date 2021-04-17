import pytest
import simplesimdb as sim
import os.path

# Run with pytest --capture=tee-sys . to see stdout output

def test_construction_and_destruction():
    print ( "TEST")
    m = sim.Manager()
    assert os.path.isdir( "data")
    m.delete_all()
    assert not os.path.isdir( "data")

def test_creation() :
    print ( "TEST CREATION")
    m = sim.Manager( directory='creation_test', executable='cp', filetype = 'json')
    assert m.directory == "creation_test"
    assert m.executable == "cp"
    assert m.filetype == "json"
    inputdata = {"Hello": "World"}
    m.create( inputdata)
    content = m.table( )
    assert content == [inputdata]
    m.delete_all()
    assert not os.path.isdir( m.directory)

def test_selection () :
    print ( "TEST SELECTION")
    m = sim.Manager( directory='selection_test', executable='cp', filetype = 'json')
    inputdata =  {"Hello": "World"}
    inputdata2 = {"Hello": "World!"}
    m.create( inputdata)
    m.create( inputdata2)
    data = m.select( inputdata )
    assert os.path.isfile( data)
    assert data == m.outfile( inputdata)
    m.delete_all()
    assert not os.path.isdir( m.directory)

def test_restart () :
    print ( "TEST RESTART")
    m = sim.Manager( directory='restart_test', executable='touch', filetype = 'th')
    inputdata =  {"Hello": "World"}
    for i in range(0,17) :
        m.create( inputdata, i)
    count = m.count( inputdata)
    assert count  == 17
    data = m.select( inputdata, 3)
    assert os.path.isfile( data)
    content = m.table()
    assert content == [inputdata]
    files = m.files()
    assert( len(files) == 17)
    m.delete_all()
    assert not os.path.isdir( m.directory)
