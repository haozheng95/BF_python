#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: yinhaozheng
@software: PyCharm
@file: client.py
@time: 2020-10-28 12:51
"""

__mtime__ = '2020-10-28'

import os

BF_BIN_PATH = "BF_BIN_PATH"
LD_PRELOAD = "LD_PRELOAD"
LD_LIBRARY_PATH = "LD_LIBRARY_PATH"
BF_ADAPTOR_PATH = "BF_ADAPTOR_PATH"
BF_ADAPTOR_RDMA = "BF_ADAPTOR_RDMA"

os.environ[BF_BIN_PATH] = "/opt/bitfusion/lib/x86_64-linux-gnu///bin"
os.environ[LD_PRELOAD] = ":/opt/bitfusion/lib/x86_64-linux-gnu//bitfusion//lib/libsyscall_intercept.so"
os.environ[LD_LIBRARY_PATH] = "/opt/bitfusion/lib/x86_64-linux-gnu//bitfusion//lib/nvml:" \
                              "/opt/intel/opencl/lib64:" \
                              "/opt/bitfusion/lib/x86_64-linux-gnu//bitfusion//lib/cuda:" \
                              "/etc/bitfusion/icd:/opt/bitfusion/lib/x86_64-linux-gnu//bitfusion//lib/opencl:" \
                              "/opt/bitfusion/lib/x86_64-linux-gnu//bitfusion//lib:/bitfusion/usr/lib/x86_64-linux-gnu/:" \
                              "/bitfusion/usr/local/lib/:/opt/bitfusion/lib/x86_64-linux-gnu/bitfusion/lib/" \
                              ":/usr/share/bitfusion/:/bitfusion/lib/x86_64-linux-gnu/:"
os.environ[BF_ADAPTOR_PATH] = "/opt/bitfusion/lib/x86_64-linux-gnu/"
os.environ[BF_ADAPTOR_RDMA] = "1"

if __name__ == '__main__':
    os.system("bitfusion request_gpus 1")
    os.system("python "
              "/benchmark/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py"
              " --local_parameter_device=gpu"
              " --batch_size=32"
              " --model=inception3")
    os.system("bitfusion release_gpus")
