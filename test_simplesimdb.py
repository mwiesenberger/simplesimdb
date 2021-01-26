import pytest
import simplesimdb as sim
import os.path


def test_construction_and_destruction():
    m = sim.Manager()
    assert os.path.isdir( "data")
    m.delete_all()
    assert not os.path.isdir( "data")

def test_creation() :
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
