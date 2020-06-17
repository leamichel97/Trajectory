# -*- coding: utf-8 -*-
"""
  run_doe.py generated by WhatsOpt 1.9.1
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 735

import sys
import numpy as np
import matplotlib.pyplot as plt
from packaging import version

from openmdao import __version__ as OPENMDAO_VERSION
from openmdao.api import Problem, SqliteRecorder, CaseReader
from openmdao_extensions.smt_doe_driver import SmtDOEDriver
from trajectoire import Trajectoire 

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

pb = Problem(Trajectoire())
pb.driver = SmtDOEDriver(sampling_method_name='LHS', n_cases=options.n_cases, sampling_method_options={'criterion': 'ese'})
pb.driver.options['run_parallel'] = options.parallel

case_recorder_filename = 'trajectoire_doe.sqlite'        
recorder = SqliteRecorder(case_recorder_filename)
pb.driver.add_recorder(recorder)
if version.parse(OPENMDAO_VERSION) > version.parse("2.8.0"):
    pb.model.nonlinear_solver.options['err_on_non_converge'] = True
else:
    pb.model.nonlinear_solver.options['err_on_maxiter'] = True


pb.model.add_design_var('alpha', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('DeltaV', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('gamma', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('mu', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('r_M', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('V1', lower=-sys.float_info.max, upper=sys.float_info.max)


pb.model.add_objective('a2')
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
data['inputs']['gamma'] = np.zeros((n,)+(1,))
data['inputs']['mu'] = np.zeros((n,)+(1,))
data['inputs']['r_M'] = np.zeros((n,)+(1,))
data['inputs']['V1'] = np.zeros((n,)+(1,))

data['outputs']['a2'] = np.zeros((n,)+(1,))
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
    data['inputs']['gamma'][i,:] = case.outputs['gamma']
    data['inputs']['mu'][i,:] = case.outputs['mu']
    data['inputs']['r_M'][i,:] = case.outputs['r_M']
    data['inputs']['V1'][i,:] = case.outputs['V1']
    data['outputs']['a2'][i,:] = case.outputs['a2']
    data['outputs']['e'][i,:] = case.outputs['e']
    data['outputs']['h'][i,:] = case.outputs['h']
    data['outputs']['p'][i,:] = case.outputs['p']
    data['outputs']['ra'][i,:] = case.outputs['ra']
    data['outputs']['rp'][i,:] = case.outputs['rp']
    data['outputs']['V2'][i,:] = case.outputs['V2']
      

output = data['outputs']['a2'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 6, 1)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('a2')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 6, 2)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['gamma'].reshape(-1)
plt.subplot(7, 6, 3)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('gamma')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 6, 4)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 6, 5)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 6, 6)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['e'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 6, 7)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('e')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 6, 8)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['gamma'].reshape(-1)
plt.subplot(7, 6, 9)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('gamma')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 6, 10)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 6, 11)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 6, 12)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['h'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 6, 13)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('h')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 6, 14)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['gamma'].reshape(-1)
plt.subplot(7, 6, 15)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('gamma')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 6, 16)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 6, 17)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 6, 18)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['p'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 6, 19)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('p')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 6, 20)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['gamma'].reshape(-1)
plt.subplot(7, 6, 21)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('gamma')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 6, 22)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 6, 23)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 6, 24)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['ra'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 6, 25)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('ra')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 6, 26)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['gamma'].reshape(-1)
plt.subplot(7, 6, 27)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('gamma')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 6, 28)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 6, 29)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 6, 30)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['rp'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 6, 31)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('rp')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 6, 32)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['gamma'].reshape(-1)
plt.subplot(7, 6, 33)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('gamma')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 6, 34)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 6, 35)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 6, 36)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')


output = data['outputs']['V2'].reshape(-1)

input = data['inputs']['alpha'].reshape(-1)
plt.subplot(7, 6, 37)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('V2')
plt.xlabel('alpha')

input = data['inputs']['DeltaV'].reshape(-1)
plt.subplot(7, 6, 38)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('DeltaV')

input = data['inputs']['gamma'].reshape(-1)
plt.subplot(7, 6, 39)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('gamma')

input = data['inputs']['mu'].reshape(-1)
plt.subplot(7, 6, 40)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('mu')

input = data['inputs']['r_M'].reshape(-1)
plt.subplot(7, 6, 41)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('r_M')

input = data['inputs']['V1'].reshape(-1)
plt.subplot(7, 6, 42)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('V1')

plt.show()
