# -*- coding: utf-8 -*-
# Intro: Aria2 客户端模块安装文件
# Author: Ztj
# Email: ztj1993@gmail.com
# Date: 2019-09-10

import os.path
import re

from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8')
readme = f.read()
f.close()

f = open(os.path.join(os.path.dirname(__file__), 'aria2client.py'), encoding='utf8')
version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)
f.close()

setup(
    name='py-ztj-aria2client',
    version=version,
    description='python aria2client package',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=['aria2client'],
    url='http://github.com/ztj1993/PythonPackages/blob/master/py_aria2rpc',
    author='ZhangTianJie',
    author_email='ztj1993@gmail.com',
    keywords='aria2 client rpc start stop service',
    install_requires=['py-ztj-aria2local', 'py-ztj-aria2rpc'],
    license='MIT License',
)
