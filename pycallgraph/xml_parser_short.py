import xml.dom.minidom as pars                      # library to parse XML documents
import pandas as pd
import numpy as np
from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput

config = Config(max_depth=6)
# config.trace_filter = GlobbingFilter(exclude=[
# 'pycallgraph.*',
# '*_find_and_load',
# ])

with PyCallGraph(output=GraphvizOutput(output_file='filter_max_depth6.png'), config=config):

    def xml_par(xmlfile):                               # function that parses an XML file by name
        rows_P = []                                     # creates an empty array for P

        doc = pars.parse(xmlfile)                       # parses an XML file
        for node in doc.getElementsByTagName('P'):      # returns a collection of all elements in the document (node) with the specified tag name 'P'
            P = node.firstChild.toxml()                 # looks for the first child of a node and returns the XML that this node represents
            P_split = P.split(' ')                      # splits the string P by space ' '
            P_split_f = list(map(float,P_split))        # converts the list P in float for every single element
            rows_P.append(P_split_f)                    # appends the converted list P to the array rows_P
        P_np = np.array(rows_P)                         # converts array into np array
        #print(P_np)

        # Do the same for F

        rows_F = []                                     # creates an empty array for F
        for node in doc.getElementsByTagName('F'):
            F = node.firstChild.toxml()
            F_split = F.split(' ')
            F_split_f = list(map(float,F_split))
            rows_F.append(F_split_f)
        F_np = np.array(rows_F)
        #print(F_np)

        dict = {'Points': P_np, 'Faces': F_np}          # creates a dictionary with P and F as key and P_np and F_np as values
        print(dict)                                     # prints the P and F as dictionary



    xml_par('/Users/glinares/PycharmProjects/Test/01_P.xml')
# input path and filename