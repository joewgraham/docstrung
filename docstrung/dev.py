"""
docstrung dev
"""

import docstrung
from docstrung import get
from docstrung import parse
from docstrung import options
from docstrung import template
from docstrung import docstrung
from inspect import cleandoc


netpyne_package = docstrung.Docstrung('netpyne')

for item in netpyne_package.all_docstrungs:

    print()
    print()
    print(item.object_name)
    print('=====================================================')
    print(item.docstring)
    print('=====================================================')
    print()
    print()
    print()




