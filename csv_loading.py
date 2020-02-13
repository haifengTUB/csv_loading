#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:26:59 2019

@author: xiao_ha
"""

import os
from pydlr.misc.hdf import hdf
mex_path = os.getenv('mex')

save_path = mex_path + 'mola_reprs_ring4_piece2122_ucl_aligned_' + \
                       'mosaic_regeo_profiles.h5'

h5 = hdf(save_path, mode='r')
profs1_geo = h5.to_dict('profs1_geo/')
#cor_zpt_profs1 = h5.to_dict('cor_zpt_profs1/')
#    h5.save_dict('cor_zpt_profs1', cor_zpt_profs1, verbose=True)
#    h5.save_dict('profs2_geo', profs2_geo, verbose=True)
#    h5.save_dict('cor_zpt_profs2', cor_zpt_profs2, verbose=True)    
h5.close()

print(profs1_geo.keys())
# print(cor_zpt_profs1)
