from __future__ import print_function
import os
from oauth2client import client,tools
from oauth2client.file import Storage
import argparse

f = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()


class autharize:
    def __init__(self, S,CSF,AN):
        self.S = S
        self.CSF = CSF
        self.AN = AN


    def get_c(self):
        cd = os.getcwd()
        crd = os.path.join(cd, '.c')
        if not os.path.exists(crd):
            os.makedirs(crd)
        crp = os.path.join(crd,'d.json')

        st = Storage(crp)
        c = st.get()
        if not c or c.invalid:
            flow = client.flow_from_clientsecrets(self.CSF, self.S)
            flow.user_agent = self.AN
            if f:
                c = tools.run_flow(flow, st, f)
            else: 
                c = tools.run(flow, st)
            print('saving c ' + crp)
        return c

