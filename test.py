# def testConvertPinch():

#     import time
#     t0 = time.time()

#     option = 1

#     # OPTION 1 - test isolated streams
#     if option == 1:
#         data_test = isolatedstreams(7)
#         test = convert_pinch(data_test, KB(kb))

#     # OPTION 2 - test processes, equipments
#     elif option ==2:
#         data_test = equipment_and_processes()
#         test = convert_pinch(data_test, KB(kb))

#     # OPTION 3 - test processes, equipments and isolated streams
#     elif option == 3:
#         data_test = equipment_process_isolated_stream()
#         test = convert_pinch(data_test, KB(kb))

#     # OPTION 4 - test equipment (one at a time)
#     elif option == 4:
#         data_test = equipment()
#         test = convert_pinch(data_test, KB(kb))


#     t1 = time.time()
#     total = t1 - t0

#     print('time simulation [s]:', total)

from module.Tests.Sources.simulation.ConvertPinch import isolatedstreams
from module.Source.simulation.Heat_Recovery.Pinch.convert_pinch import convert_pinch
from module.utilities.kb import KB
from module.utilities.kb_data import kb

data_test = isolatedstreams(4)
result = convert_pinch(data_test, KB(kb))


print(result)