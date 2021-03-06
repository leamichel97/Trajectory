# -*- coding: utf-8 -*-
"""
  trajectory_version2_base.py generated by WhatsOpt 1.9.4
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: https://ether.onera.fr/whatsopt
# analysis_id: 735


import numpy as np
from numpy import nan

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from trajectory import Trajectory



class TrajectoryVersion2Base(Group):
    """ An OpenMDAO base component to encapsulate TrajectoryVersion2 MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(TrajectoryVersion2Base, self). __init__(**kwargs)

        self.nonlinear_solver = NonlinearBlockGS() 
        self.nonlinear_solver.options['atol'] = 1.0e-10
        self.nonlinear_solver.options['rtol'] = 1.0e-10
        self.nonlinear_solver.options['err_on_non_converge'] = True
        self.nonlinear_solver.options['reraise_child_analysiserror'] = False

        self.linear_solver = ScipyKrylov()       
        self.linear_solver.options['atol'] = 1.0e-10
        self.linear_solver.options['rtol'] = 1.0e-10
        self.linear_solver.options['err_on_non_converge'] = True
        self.linear_solver.options['iprint'] = 1

    def setup(self): 
        indeps = self.add_subsystem('indeps', IndepVarComp(), promotes=['*'])

        indeps.add_output('alpha', 1.0)
        indeps.add_output('DeltaV', 1.0)
        indeps.add_output('mu', 1.0)
        indeps.add_output('r_M', 1.0)
        indeps.add_output('V1', 1.0)
        self.add_subsystem('Trajectory', self.create_trajectory(), promotes=['a', 'alpha', 'DeltaV', 'e', 'h', 'mu', 'p', 'ra', 'rp', 'r_M', 'V1', 'V2'])

    def create_trajectory(self):
    	return Trajectory()


# Used by Thrift server to serve disciplines
class TrajectoryVersion2FactoryBase(object):
    @staticmethod
    def create_trajectory():
    	return Trajectory()
