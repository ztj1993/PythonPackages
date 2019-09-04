# -*- coding: utf-8 -*-
# Intro: 配置模块安装文件
# Author: Ztj
# Email: ztj1993@gmail.com
# Date: 2019-09-02

import os.path

from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8')
readme = f.read()
f.close()

setup(
    name='py-ztj-registry',
    version=__import__('registry').__version__,
    description='python registry package',
    long_description=readme,
    long_description_content_type="text/markdown",
    py_modules=["registry"],
    url='http://github.com/ztj1993/PythonPackages/blob/master/registry',
    author='ZhangTianJie',
    author_email='ztj1993@gmail.com',
    keywords='registry config json yaml',
    license='MIT License',
)
