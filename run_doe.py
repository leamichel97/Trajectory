# -*- coding: utf-8 -*-
"""
  run_doe.py generated by WhatsOpt 1.9.4
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 735

import sys
import numpy as np
import matplotlib.pyplot as plt

from openmdao.api import Problem, SqliteRecorder, CaseReader
from openmdao_extensions.smt_doe_driver import SmtDOEDriver
from trajectory_version2 import TrajectoryVersion2 

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--batch",
                  action="store_true", dest="batch", default=False,
                  help="do not plot anything")
parser.add_option("-n", "--ncases", type="int",
                  dest="n_cases", default=50,
                  help="number of samples")
parser.add_option("-p", "--parallel", 
                  action="store_true", default=False,
                  help="run doe in parallel")
(options, args) = parser.parse_args()

pb = Problem(TrajectoryVersion2())
pb.driver = SmtDOEDriver(sampling_method_name='LHS', n_cases=options.n_cases, sampling_method_options={'criterion': 'ese'})
pb.driver.options['run_parallel'] = options.parallel

case_recorder_filename = 'trajectory_version2_doe.sqlite'        
recorder = SqliteRecorder(case_recorder_filename)
pb.driver.add_recorder(recorder)
pb.model.nonlinear_solver.options['err_on_non_converge'] = True


pb.model.add_design_var('alpha', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('DeltaV', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('mu', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('r_M', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('V1', lower=-sys.float_info.max, upper=sys.float_info.max)


pb.model.add_objective('a')
pb.model.add_objective('e')
pb.model.add_objective('h')
pb.model.add_objective('p')
pb.model.add_objective('ra')
pb.model.add_objective('rp')
pb.model.add_objective('V2')

pb.setup()  
pb.run_driver()        


if options.batch or options.parallel:
    exit(0)
reader = CaseReader(case_recorder_filename)
cases = reader.list_cases('driver')
n = len(cases)
data = {'inputs': {}, 'outputs': {} }

data['inputs']['alpha'] = np.zeros((n,)+(1,))
data['inputs']['DeltaV'] = np.zeros((n,)+(1,))
data['inputs']['mu'] = np.zeros((n,)+(1,))
data['inputs']['r_M'] = np.zeros((n,)+(1,))
data['inputs']['V1'] = np.zeros((n,)+(1,))

data['outputs']['a'] = np.zeros((n,)+(1,))
data['outputs']['e'] = np.zeros((n,)+(1,))
data['outputs']['h'] = np.zeros((n,)+(1,))
data['outputs']['p'] = np.zeros((n,)+(1,))
data['outputs']['ra'] = np.zeros((n,)+(1,))
data['outputs']['rp'] = np.zeros((n,)+(1,))
data['outputs']['V2'] = np.zeros((n,)+(1,))

for i in range(len(cases)):
    case = reader.get_case(cases[i])
    data['inputs']['alpha'][i,:] = case.outputs['alpha']
    data['inputs']['DeltaV'][i,:] = case.outputs['DeltaV']
    data['inputs']['mu'][i,:] = case.outputs['mu']
    data['inputs']['r_M'][i,:] = case.outputs['r_M']
    data['inputs']['V1'][i,:] = case.outputs['V1']
    data['outputs']['a'][i,:] = case.outputs['a']
    data['outputs']['e'][i,:] = case.outputs['e']
    data['outputs']['h'][i,:] = case.outputs['h']
    data['outputs']['p'][i,:] = case.outputs['p']
    data['outputs']['ra'][i,:] = case.outputs['ra']
    data['outputs']['rp'][i,:] = case.outputs['rp']
    data['outputs']['V2'][i,:] = case.outputs['V2']
      

output = data['outputs']['a'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 5, 1)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('a')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 5, 2)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 5, 3)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 5, 4)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 5, 5)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['e'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 5, 6)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('e')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 5, 7)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 5, 8)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 5, 9)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 5, 10)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['h'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 5, 11)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('h')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 5, 12)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 5, 13)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 5, 14)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 5, 15)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['p'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 5, 16)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('p')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 5, 17)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 5, 18)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 5, 19)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 5, 20)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['ra'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 5, 21)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('ra')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 5, 22)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 5, 23)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 5, 24)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 5, 25)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['rp'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 5, 26)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('rp')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 5, 27)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 5, 28)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 5, 29)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 5, 30)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['V2'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 5, 31)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('V2')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 5, 32)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 5, 33)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 5, 34)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 5, 35)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')

plt.show()
