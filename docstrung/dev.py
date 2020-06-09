"""
docstrung dev
"""

import docstrung
from docstrung import get
from docstrung import parse
from docstrung import options
from docstrung import template
from inspect import cleandoc




pack = parse.DocstringParser('netpyne')
pack_doc = template.DocstringTemplate()
print(pack)

subpack = parse.DocstringParser('netpyne.analysis')
print(subpack)

mod = parse.DocstringParser('netpyne.analysis.info')
print(mod)

func = parse.DocstringParser('netpyne.analysis.info.granger')
print(func)

classi = parse.DocstringParser('netpyne.specs.netParams.NetParams')



