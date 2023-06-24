# -*- coding: utf-8 -*-
#
# This source file is part of the FabSim software toolkit, which is distributed under the BSD 3-Clause license.
# Please refer to LICENSE for detailed information regarding the licensing.
#
# This file contains FabSim definitions specific to FabTsp.

try:
    from fabsim.base.fab import *
    from fabsim.VVP import vvp
except ImportError:
    from base.fab import *

# Add local script, blackbox and template path.
add_local_paths("FabTsp")


@task
@load_plugin_env_vars("FabTsp")
def stsp(config='stsp', label='', **args):
    '''
    Submit a single job of tsp (non-MPI)

    fabsim <remote_machine> stsp:stsp
    fabsim localhost stsp:stsp
    '''
    if len(label) > 0:
        env.job_name_template += "_{}".format(label)

    update_environment(args)
    with_config(config)
    execute(put_configs, config)
    job(dict(script='stsp'), args)


@task
@load_plugin_env_vars("FabTsp")
def ptsp(config='ptsp', label='', **args):
    '''
    Submit a single job of tsp (MPI)

    fabsim <remote_machine> ptsp:tsp
    fabsim localhost ptsp:tsp
    '''
    if len(label) > 0:
        env.job_name_template += "_{}".format(label)

    update_environment(args)
    with_config(config)
    execute(put_configs, config)
    job(dict(script='ptsp'), args)


@task
@load_plugin_env_vars("FabTsp")
def ptsp_ensemble(config='tsp', label='', **args):
    '''
    Submit an ensemble of tsp jobs (MPI)

    fabsim <remote_machine> FabTsp_ensemble:ptps
    fabsim localhost FabTsp_ensemble:ptsp
    '''

    if len(label) > 0:
        env.job_name_template += "_{}".format(label)

    update_environment(args)
    path_to_config = find_config_file_path(config)
    print("local config file path at: %s" % path_to_config)
    sweep_dir = path_to_config + "/SWEEP"
    env.script = 'ptsp'
    env.input_name_in_config = 'tsp'
    with_config(config)
    run_ensemble(config, sweep_dir, **args)
