# A Simple simulation data creator and manager
A python module for creation and management of simple simulation data

 The idea is that a json input file can be (uniquely) hashed to a file-name
 We can thus have a hash table of simulation results. The user is then able to
 create, search and select entries based on given python dictionaries
 that can be converted to json.

[![LICENSE : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install simplesimdb.

```bash
pip install foobar
```

If you want to develop the module then the editable flag (which then
will import the current state of the module)

```bash
cd path/to/simplesimdb
pip install -e . # editable installation of the module
pytest . # run the unittests
```

## Usage

```python
import json
import simplesimdb
import yaml

db = simplesimdb.Manager( directory = 'ds_data',
    filetype='yaml',
    executable='./execute.sh')

inputfile = {
        "n": 3,
        "Nx" : 20,
        "Ny" : 20,
        "Nz" : 20,
        "mx" : 10,
        "my" : 10
}

outfile = db.create( inputfile) # create the simulation data using inputfile as input
with open( outfile) as f:
    output = yaml.full_load(f)

    print (json.dumps(output, indent=4))
    f.close()

db.delete_all() # delete all data in the directory and the directory itself
```
where execute.sh is a bash script that takes in.json as input and creates the file
out.yaml
```bash
#!/bin/bash

: ${FELTOR_PATH:="../feltor"}

#echo "Compiling the source code ... "
#ake $FELTOR_PATH/src/lamb_dipole/Makefile
#echo "... Done"

#echo "$FELTOR_PATH/inc/geometries/ds_t"
cat $1 | jq '.n, .Nx, .Ny, .Nz, .mx, .my' | $FELTOR_PATH/inc/geometries/ds_t > $2
```

On the other hand
### Usage
 Use this module if
 - you do not deal with millions of entries but a only a few hundred at best so
   a DBMS might just be overkill
 - search methods for dictionaries (especially if they are converted to tables)
    are offered by python as well
 - There is an additional overhead of setting up and running a mongodb server
 - netcdf (or other output) files do not really map nicely into the mongodb data model since
   files larger than 16 MB require another FileGS server to be run
 - If netcdf files are stored by the DB manager how do we get access to it
   through for example paraview
 - If json files are hidden by the database manager how do we use them to run a
   code?

# Limitations of this class
 - how to manage restarted simulations i.e. sims, where one input file
   generates a continuous series of netcdf files
 - how to manage simulations with more than one input file (probably the
   easiest solution is to concatenate the two files)
 - the execution script is the highest requirement and should be documented
   so the class is more of a file creator than a database manager (in the
   classical sense)
 - won't manage existing files (create View )
 - won't manage several inputs - several outputs scenario ( in particular the one
   where a simulation is restarted over and over)
 - won't be able to submit and wait (unless you misuse it on a cluster and
   just ignore the output file parameter)
 - the input.json file can be viewed as the metadata of a simulation and we assume
   that it can uniquely identify the output (something which is not true if you do
   not include for example parallelization details)
 - This code may be re-inventing the wheel: NoSQL database managers may do a
    better job, e.g. the document (json) category MongoDB: manage large files
    (videos, images, PDFs, etc.) along with supporting information (metadata) that
    fits naturally into JSON documents
# Ideas on file views
 - We can have a separate class managing a view of (input.json, outfile) pairs
   without creating files but just managing the inputs
 - no functionality to create or delete files
 - add single files or whole folders (assuming json and nc file has the name)
# Idea on submit file creation
 - maybe use the simple-slurm package to generate slurm scripts


