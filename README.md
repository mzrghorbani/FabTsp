## Implementation of FabTsp for TSP algorithm 

The FabTsp plugin implementation follows the instructions in 'An automation toolkit for complex simulation tasks' here:

    https://fabsim3.readthedocs.io/en/latest/create_new_plugin/


## FabSim3 Project

FabSim3 is a Python-based automation toolkit for scientific simulation and data processing workflows, licensed under the BSD 3-clause license. 

It is developed as part of the SEAVEA project http://www.seavea-project.org, and VECMA Toolkit http://www.vecma-toolkit.eu.


## FabTsp Plugin

FabTsp plugin is part of a bigger FabSim3 project. All plugins are placed in FabSim3/plugins/ directory with its configuration files and scripts. The Travelling Salesman Problem (TSP) algorithm is then placed in FabTsp/config_files with all required files and scripts.

## Cloning Repositories 

The TSP plugin can be cloned from GitHub repository:

    https://github.com/mzrghorbani/tsp.git

The FabTsp utility can be found in GitHub repository:

    https://github.com/mzrghorbani/FabTsp.git

## Instructions

The FabTsp can be installed using FabSim3 command:

    fabsim localhost plugin_install:FabTsp

The FabTsp has a frozen version of TSP algorithm and files, however for more recent version, the tps can be cloned or copied to the FabTsp/config_files directory.

There are two versions of the tsp algorithm. With MPI and without MPI.

For the non-MPI version on localhost, run:

    fabsim localhost stsp:tsp

For the MPI version on localhost, run:

    fabsim localhost ptsp:tsp

Change localhost to a <remote_machine> to run jobs remotely (e,g,. archer2)

The jobs can also run  in ensemble mode with MPI using:

    fabsim localhost ensemble_stsp:tps,cores=<num_processors>,replicas=<num_replications>

