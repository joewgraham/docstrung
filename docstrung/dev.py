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


# classi = docstringer.Docstrung('netpyne.specs.netParams.NetParams')
# print(classi)

# func = docstringer.Docstrung('netpyne.analysis.info.granger')
# print(func)

# mod = docstringer.Docstrung('netpyne.analysis.info')
# print(mod)

# subpack = docstringer.Docstrung('netpyne.analysis')
# print(subpack)

pack = docstrung.Docstrung('netpyne')

foo = pack.all_docstrungs[0]


