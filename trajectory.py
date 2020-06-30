# -*- coding: utf-8 -*-
"""
  trajectory.py generated by WhatsOpt 1.9.4
"""
import numpy as np
from trajectory_base import TrajectoryBase

class Trajectory(TrajectoryBase):
    """ An OpenMDAO component to encapsulate Trajectory discipline """
		
    def compute(self, inputs, outputs):
        """ Trajectory computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:  
            alpha = inputs['alpha']
            DeltaV = inputs['DeltaV']
            mu = inputs['mu']
            r_M = inputs['r_M']
            V1 = inputs['V1']

            V2 = np.sqrt(V1**2 + DeltaV**2 + 2 * DeltaV * V1 * np.cos(alpha))
            a = (r_M * mu) / ((2 * mu) - (V2**2 * r_M))
            cos_gamma = (V1**2 + V2**2 - DeltaV**2) / (2 * V1 * V2)
            h = r_M * V2 * cos_gamma
            p = h**2 / mu
            e = np.sqrt(1 - p/a) 
            rp = a * (1-e)
            ra = a * (1+e)

            outputs['a']= a
            outputs['e'] = e
            outputs['h'] = h
            outputs['p'] = p
            outputs['ra'] = ra
            outputs['rp'] = rp 
            outputs['V2'] = V2
        return outputs 

# Reminder: inputs of compute()
#   
#       inputs['alpha'] -> shape: 1, type: Float    
#       inputs['DeltaV'] -> shape: 1, type: Float    
#       inputs['mu'] -> shape: 1, type: Float    
#       inputs['r_M'] -> shape: 1, type: Float    
#       inputs['V1'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Trajectory, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Trajectory """
#   
#       	partials['a', 'alpha'] = np.zeros((1, 1))
#       	partials['a', 'DeltaV'] = np.zeros((1, 1))
#       	partials['a', 'mu'] = np.zeros((1, 1))
#       	partials['a', 'r_M'] = np.zeros((1, 1))
#       	partials['a', 'V1'] = np.zeros((1, 1))
#       	partials['e', 'alpha'] = np.zeros((1, 1))
#       	partials['e', 'DeltaV'] = np.zeros((1, 1))
#       	partials['e', 'mu'] = np.zeros((1, 1))
#       	partials['e', 'r_M'] = np.zeros((1, 1))
#       	partials['e', 'V1'] = np.zeros((1, 1))
#       	partials['h', 'alpha'] = np.zeros((1, 1))
#       	partials['h', 'DeltaV'] = np.zeros((1, 1))
#       	partials['h', 'mu'] = np.zeros((1, 1))
#       	partials['h', 'r_M'] = np.zeros((1, 1))
#       	partials['h', 'V1'] = np.zeros((1, 1))
#       	partials['p', 'alpha'] = np.zeros((1, 1))
#       	partials['p', 'DeltaV'] = np.zeros((1, 1))
#       	partials['p', 'mu'] = np.zeros((1, 1))
#       	partials['p', 'r_M'] = np.zeros((1, 1))
#       	partials['p', 'V1'] = np.zeros((1, 1))
#       	partials['ra', 'alpha'] = np.zeros((1, 1))
#       	partials['ra', 'DeltaV'] = np.zeros((1, 1))
#       	partials['ra', 'mu'] = np.zeros((1, 1))
#       	partials['ra', 'r_M'] = np.zeros((1, 1))
#       	partials['ra', 'V1'] = np.zeros((1, 1))
#       	partials['rp', 'alpha'] = np.zeros((1, 1))
#       	partials['rp', 'DeltaV'] = np.zeros((1, 1))
#       	partials['rp', 'mu'] = np.zeros((1, 1))
#       	partials['rp', 'r_M'] = np.zeros((1, 1))
#       	partials['rp', 'V1'] = np.zeros((1, 1))
#       	partials['V2', 'alpha'] = np.zeros((1, 1))
#       	partials['V2', 'DeltaV'] = np.zeros((1, 1))
#       	partials['V2', 'mu'] = np.zeros((1, 1))
#       	partials['V2', 'r_M'] = np.zeros((1, 1))
#       	partials['V2', 'V1'] = np.zeros((1, 1))        
