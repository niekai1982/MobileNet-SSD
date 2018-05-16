from __future__ import print_function, absolute_import
from google.protobuf import text_format
import argparse
import re
import sys
import math

sys.path.insert(0, '/Users/niekai/caffe-ssd/caffe/python')
caffe_flag = True

try:
    import caffe
    from caffe.proto import caffe_pb2
except ImportError:
    caffe_flag = False
    from .caffe_parse import caffe_pb2

def read_proto_solver_filer(file_path):
    solver_config = ''
    if caffe_flag:
        solver_config = caffe.proto.caffe_pb2.NetParameter()
    else:
        solver_config = caffe_parse.caffe_pb2.NetParameter()
    return read_proto_file(file_path, solver_config)

def read_proto_file(file_path, parse_object):
    file = open(file_path, "r")
    if not file:
        raise Exception("ERROR(" + file_path + ")!")
    text_format.Merge(str(file.read()), parse_object)
    file.close()
    return parse_object






