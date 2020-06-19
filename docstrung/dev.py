"""
docstrung dev
"""

import docstrung
from docstrung import get
from docstrung import parse
from docstrung import options
from docstrung import docstrung
from inspect import cleandoc


netpyne_package = docstrung.Docstrung('netpyne')

for item in netpyne_package.all_docstrungs:

    print()
    print()
    print()
    print()
    print(item.object_name, item.object_type)
    print('=====================================================')
    print()
    print()
    print('old docstring')
    print('-----------------------------------------------------')
    print(item.original_docstring)
    print('-----------------------------------------------------')
    print()
    print()
    print('new docstring')
    print('-----------------------------------------------------')
    print(item.docstring)
    print('=====================================================')
    print()
    print()
    print()
    print()




# from docstrung.docstrung import DocstrungDocstring

# good = DocstrungDocstring('netpyne.analysis.info.granger')
# bad = DocstrungDocstring('netpyne.analysis.interactive.iplotDipole')
# none = DocstrungDocstring('netpyne.analysis.interactive.iplotLFP')

# print()
# print('good')
# print('=======================================================')
# print(good.docstring)
# print('=======================================================')
# print()

# print()
# print('bad')
# print('=======================================================')
# print(bad.docstring)
# print('=======================================================')
# print()

# print()
# print('none')
# print('=======================================================')
# print(none.docstring)
# print('=======================================================')
# print()