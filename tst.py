from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput



# config = Config()
# config.trace_filter = GlobbingFilter(exclude=[
# 'pycallgraph.*',
# '*.secret_function',
# ])
# graphviz = GraphvizOutput(output_file='filter_exclude.png')
#
with PyCallGraph(output=GraphvizOutput(output_file='filter_none.png')):
    print('Hola mundo')
    print('Hello world')