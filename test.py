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

### MODULE-CODE [BEGIN]
import pandas as pd
from module.Source.simulation.Heat_Recovery.Pinch.make_pinch_design_draw import make_pinch_design_draw
from module.Tests.Sources.simulation.ConvertPinch import isolatedstreams
from module.Source.simulation.Heat_Recovery.Pinch.convert_pinch import convert_pinch
from module.utilities.kb import KB
from module.utilities.kb_data import kb

import warnings
warnings.filterwarnings("ignore")

data_test = isolatedstreams(7)
result = convert_pinch(data_test, KB(kb))

energy_investment_optimization_pinch_info = list(map(lambda f : f['_info_pinch'], result['energy_recovered_optimization']))
energy_investment_optimization_pinch_info = list(map(lambda f : f['_info_pinch'], result['energy_investment_optimization']))

_info_pinch = energy_investment_optimization_pinch_info[0]

FIGHTML = make_pinch_design_draw(
                      _info_pinch['streams_info'],
                      _info_pinch['pinch_temperature'],
                      _info_pinch['df_hx'].to_dict(orient='records'),
                      _info_pinch['pinch_delta_T_min']
                      )

data_frame_example = _info_pinch['df_hx']
data_frame_in_html = _info_pinch['df_hx'].to_html(
    classes=['table'], 
    columns=['HX_Cold_Stream_T_Cold','HX_Cold_Stream_T_Hot','HX_Cold_Stream_flowrate','HX_Cold_Stream_mcp','HX_Hot_Stream_flowrate']
    )

### MODULE-CODE [END]


### REPORT_RENDERING_CODE [BEGIN]
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('asset'),
    autoescape=False
)

template = env.get_template('index.template.html')
template_content = template.render(plot=FIGHTML, streams=_info_pinch['streams_info'], df_hx=data_frame_in_html)


f = open("index.html", "w")
f.write(template_content)
f.close()

output = {
    "every" : "thing",
    "else" : "yes",
    "report" : template_content
}