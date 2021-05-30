#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:22:26 2021.

@author: tristantacule
"""


# %%
# Libraries.
import os
import sys

from pathlib import Path

import importlib.util

# %%
# Initialisation. Getting the working directory.
challpath = Path(os.environ['CTF_CHALL2'])

DEBUG = True

# Importing custom functions.
if DEBUG:
    sys.path.append(str(challpath / '01-code'))
    import tools_chall2 as tls
    import network.network as network
else:
    spec = importlib.util.spec_from_file_location("tools", challpath / '01-code/tools_chall2.py')
    tls = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tls)

    spec = importlib.util.spec_from_file_location("network", challpath / '01-code/network/network.py')
    network = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(network)

# %%
# Parametres and variables.

# The flag to find.
flag = '067089066069082084070123073095076048086095073052095067089066051082125'

# The key is used to shuffle the pixels
key = 'Dimitri_Kiriznov_403'

# Net and data.
net = tls.load_network(challpath)
# training_data, validation_data, test_data = tls.load_data_wrapper()

# The desired size of final images.
size = 512
# Shuffled positions.
vect_pos = tls.get_shuffle_bis(key, size)
# Positions of important pixels
vect_adv_pos = vect_pos[:net.sizes[0]]

# with open(challpath / 'vect_RC4.txt', 'w') as file:
#     for elt in vect_adv_pos:
#         file.write(f'{str(elt)}\n')

# %%
# Simple test. Generate an adversarial image and chank that the predicted result is indeed the targeted result.
tls.simple_test(net, target=8, plot=True)

# %%
# Load backup directories for adversarial images, images, and gifs.
tls.load_backup(challpath)

# %%
# Let's generate our adversarial images.
for i in range(10):
    tls.gen_adv_images(net, i, challpath)

# %%
# We can now check that our adversarial images yield the right answer.
lst_files = os.listdir(challpath / '03-img_adv')
lst_test_adv = []

for file in lst_files:
    lst_test_adv.append(tls.test_adv_image(net, challpath, file))

print(all(lst_test_adv))

# %%

# '067089066069082084070123073095076048086095073052095067089066051082125'

tls.gen_gif_RGB_from_list_adv(net, challpath, size, flag, vect_adv_pos, purge_img=True, purge_gif=True)

lst_preds = tls.parse_gif_RGB(net, challpath, size, vect_adv_pos, file='chall2_flagged')
print(''.join(lst_preds))

parsed_flag = tls.parse_flag(lst_preds)
print(parsed_flag)
