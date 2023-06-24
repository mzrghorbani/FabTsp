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
def FabTsp(config='tsp', label='', **args):
    '''
    Submit a single job of tsp

    fabsim <remote_machine> FabTsp:tsp
    fabsim localhost FabTsp:tsp
    '''
    if len(label) > 0:
        env.job_name_template += "_{}".format(label)

    update_environment(args)
    with_config(config)
    execute(put_configs, config)
    job(dict(script='run_par'), args)


@task
@load_plugin_env_vars("FabTsp")
def FabTsp_ensemble(config='tsp', label='', **args):
    '''
    Submit an ensemble of tsp jobs

    fabsim <remote_machine> FabTsp_ensemble:tps
    fabsim localhost FabTsp_ensemble:tsp
    '''

    if len(label) > 0:
        env.job_name_template += "_{}".format(label)

    update_environment(args)
    path_to_config = find_config_file_path(config)
    print("local config file path at: %s" % path_to_config)
    sweep_dir = path_to_config + "/SWEEP"
    env.script = 'run_par'
    env.input_name_in_config = 'tsp'
    with_config(config)
    run_ensemble(config, sweep_dir, **args)
