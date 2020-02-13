#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:26:59 2019

@author: xiao_ha
"""

#import os
#from pydlr.misc.hdf import hdf
#mex_path = os.getenv('mex')
#
#save_reg = mex_path + 'mola_reprs_ring4_piece2122_ucl_aligned_' + \
#                      'mosaic_local_co_reg_radius_60km.h5'
#h5 = hdf(save_reg, mode='r')
#res = h5.to_dict('mola/')
#cor_regist = h5.file['par']
#
#print("Loading of data complete!!")

#import pydlr.la.mola as ml
#import pydlr.misc.tools as tools
#import os
#import spiceypy as spice
#import pydlr.cor.profile as cor_prof
#import pydlr.vic.io as vic_io
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#from scipy.constants import degree
#import time
#import pdb
#import gc
#import itertools
#from pydlr.misc.prog import Prog
#spkgeo = spice.spkgeo
#
## time delay
## time.sleep(32*3600)
#
## mola_path = /misc/system/exchange/haifeng/missions/mgs/data/mola/
#mola_path = os.getenv('mola')
## mgs_path = /misc/system/exchange/haifeng/missions/mgs/
#mgs_path = os.getenv('mgs')
#path_meta = mgs_path+'kernels/mk'
##  The improved spacecraft orbit data
#metakernel = path_meta+'/mgs_ipng_mgs95j_ck.tm'
##metakernel = path_meta+'/mgs_ipng_mgs95j_ck_mappingphase.tm'
#spice.kclear()
## load the SPICE kernels
#if (metakernel is not None):
#    spice.furnsh(metakernel)
#
## DTM used for the registration
## setenv mex /misc/system/exchange/haifeng/missions/mex/
#mex_path = os.getenv('mex')
#dtm_file = mex_path+'data/hrsc/dtm/ucl/orbital/batch_alignment'\
#+'/ucl_dtms_mosaic_after_alignment.dtm'
#
#Dtm = vic_io.Vicar(dtm_file)
#Dtm.read_Vicar()
#
#del Dtm

#from pydlr.misc.hdf import hdf
#import os
#
#mla_path = os.getenv('mla')
#
#mex_path = os.getenv('mex')
#
##save_reg = mex_path + 'mola_reprs_ring4_piece2122_ucl_aligned_' + \
##                      'mosaic_local_co_reg_radius_60km.h5'
#save_path = mla_path+'cor/mla_cor_2001_pam_bf_SSBObs.h5'
##h5 = hdf(save_reg, mode='r')
#h5 = hdf(save_path, mode='r')
#res = h5.to_dict('mla/')
#cor_regist = h5.file['par']
#
#print("Loading of data complete!!")
#
#res.keys()

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
