from hutch_python.utils import safe_load
from cxi.devices import Injector, Questar, Parameters

#from cxi.db import cxi
from cxi.db import cxi_pulsepicker
from cxi.db import daq
try:
        def daq_repeat(seconds=10):
                while True:
                        daq.begin(duration=seconds, wait=True)
                        daq.end_run()

except KeyboardInterrupt:
        daq.end_run()

def daq_fixed_runs(runtime, darktime = 0):
#       print "Run time =" run_time
#       print "Dark time =" dark_time
        while True:
                if darktime > 0:
                        cxi.pulsepicker.open(wait=True)
                        daq.record(duration=run_time, wait=True)
                        daq.end_run()

                else:
                        cxi.pulsepicker.close(wait=True)
                        daq.record(duration=darktime, wait=True)
                        cxi.pulsepicker.open(wait=True)
                        daq.record(duration=runtime,wait=True)
                        daq.end_run()


with safe_load('PI1_injector'):
    PI1 = {'name': 'PI1_injector',
           'coarseX': 'CXI:PI1:MMS:01',
           'coarseY': 'CXI:PI1:MMS:02',
           'coarseZ': 'CXI:PI1:MMS:03',
           'fineX': 'CXI:USR:MMS:01',
           'fineY': 'CXI:USR:MMS:02',
           'fineZ': 'CXI:USR:MMS:03'}

with safe_load('PI2_injector'):
    PI2 = {'name': 'PI2_injector',
           'coarseX': 'CXI:PI2:MMS:01',
           'coarseY': 'CXI:PI2:MMS:02',
           'coarseZ': 'CXI:PI2:MMS:03',
           'fineX': 'CXI:PI2:MMS:04',
           'fineY': 'CXI:PI2:MMS:05',
           'fineZ': 'CXI:PI2:MMS:06'}
    PI2_injector = Injector(**PI2)

with safe_load('PI3_injector'):
    PI3 = {'name': 'PI3_injector',
           'coarseX': 'CXI:PI3:MMS:01',
           'coarseY': 'CXI:PI3:MMS:02',
           'coarseZ': 'CXI:PI3:MMS:03',
           'fineX': 'CXI:PI3:MMS:04',
           'fineY': 'CXI:PI3:MMS:05',
           'fineZ': 'CXI:PI3:MMS:06'}
    PI3_injector = Injector(**PI3)

with safe_load('SC1_questar'):
    port_names = {'ROI_port': 'ROI1',
                  'ROI_stats_port': 'Stats1',
                  'ROI_image_port': 'IMAGE1'}
    SC1_questar = Questar(**port_names, prefix='CXI:SC1:INLINE', name='SC1_questar')

with safe_load('SC1_params'):
    SC1_params = Parameters(prefix='CXI:SC1:ONAXIS', name='SC1_params')
