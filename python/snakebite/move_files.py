#!/usr/bin/env python

import os
from snakebite.client import Client


client = Client("trevally.amer.nevint.com", 9000, use_trash=False, effective_user='hadoop')


#for res in client.mkdir(['/user/hadoop/test/move/file'],create_parent=True, mode=755):
#    print res

for res in client.rename(['/user/hadoop/test.tar'],'/user/hadoop/test3.tar'):
    print res

