# A Simple simulation data creator and database manager
A python module for creation and management of simple simulation data.
Essentially, a very basic database manager that creates its own data.


[![LICENSE : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation
We do not yet have an uploaded version on pypi.
To install you have to clone the repository and then use the package manager [pip](https://pip.pypa.io/en/stable/).
> You need python3 to install this module

```bash
git clone https://github.com/mwiesenberger/simplesimdb
cd path/to/simplesimdb
pip install -e . # editable installation of the module
pytest . # run the unittests
```

## Usage
Use this module if you have (i) an executable (the simulation code) that takes a set of input parameters
and generates a single output file and (ii) you want to explore a large region of the
available parameter space ( large here means more than you want to do by hand
but probably less than millions say).
Its tasks are
 - generate json input files from given python dictioniaries and assign unique
   filenames
 - call the user provided executable on the input files to create the
   corresponding output file
 - select existing output files from the data folder based on a given input
 - display all input parameters for which output data exists in the folder

Here is an example of how to use the module

```python
import json
import simplesimdb
import yaml

db = simplesimdb.Manager(
    directory = 'ds_data',
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

outfile = db.create( inputfile) # call executable to create the simulation data using inputfile as input
with open( outfile) as f:
    output = yaml.full_load(f)
    print (json.dumps(output, indent=4))

content = db.table() # a list of dictionaries of all existing input in the directory
file_list = db.files() # a list of dictionaries containing "id", "inputfile" and "outputfile" entries.
outfile = db.select( inputfile) # select an existing simulation

db.delete_all() # delete all generated data in directory and the directory itself if empty
```
where execute.sh is a bash script that takes hashid.json as input and creates the file
hashid.yaml
Here is an example of how the exectuable can look like. We use a bash script
to parse the json input into command line arguments to a Feltor code
and redirect its output into the yaml file.
```bash
#!/bin/bash

: ${FELTOR_PATH:="../feltor"}

# Feltor's ds_t requires input parameters from the command line
# so we parse the json string using jq
cat $1 | jq '.n, .Nx, .Ny, .Nz, .mx, .my' | $FELTOR_PATH/inc/geometries/ds_t > $2
```

### Why not just use an existing database management software like SQL
 - Relational databases are notoriously unsuited for scientific simulations so
   SQL is mostly not an option in the scientific community (in python we would
   use pandas anyway)
 - Search methods that DBMS offer are offered by python for dictionaries as
   well (especially if they are converted to tables in pandas)
 - There is an additional overhead of setting up and running a databaser server
 - When doing a parameter study you do not deal with millions of entries but a
   only a few hundred at best so a DBMS might just be overkill
 - There are NoSQL database managers like for example a document (json) manager
   like MongoDB that can  manage large files (videos, images, PDFs, etc.) along
   with supporting information (metadata) that fits naturally into JSON
   documents, but
 - Netcdf (or other output) files do not really map nicely into the mongodb
   data model since files larger than 16 MB require another FileGS server to be
   run
 - If netcdf files are stored by the DB manager how do we get access to it
   through other external programs like for example paraview?
 - If json files are hidden by the database manager how do we use them as input
   to run an executable to generate the output file?

### Current limitations of this module
 - Cannot manage restarted simulations i.e. sims, where one input file
   generates a continuous series of netcdf files
 - Cannot manage simulations with more than one input file (probably the
   easiest solution is to concatenate the two files)
 - Won't manage existing files that do not have names assigned by the class
   (create View )
 - Won't manage several inputs - several outputs scenario ( in particular the
   one where a simulation is restarted over and over)
 - Won't be able to submit and wait (unless you misuse it on a cluster and just
   ignore the output file parameter)
 - The input.json file can be viewed as the metadata of a simulation and we
   assume that it can uniquely identify the output (something which is not true
   if you do not include for example parallelization details)
 - Not optimized that is for (very) large input files (Mega or Giga bytes say) it
   is probably slow

### Contributions
Contributions are welcome.
### Authors
Matthias Wiesenberger

