"""
docstrung dev
"""

import docstrung
from docstrung import get
from docstrung import parse
from inspect import cleandoc
from sphinx.ext.napoleon import Config
from sphinx.ext.napoleon import docstring as napoleon_docstring
# from sphinx.ext.napoleon docstring import GoogleDocstring, NumpyDocstring



# def parse_docstring(object_name):
    
#     config = Config()

#     imported_object, object_type = get.get_object(object_name, return_type=True)
#     object_docstring = get.get_docstring(object_name)

    
#     parsed = napoleon_docstring.NumpyDocstring(
#                 cleandoc(object_docstring),
#                 config = config, 
#                 app    = None, 
#                 what   = object_type,
#                 name   = object_name, 
#                 obj    = imported_object
#                 )

    

#     return parsed


# foo = parse_docstring('netpyne.analysis.info.granger')



pack = parse.DocstringParser('netpyne')
print(pack)

subpack = parse.DocstringParser('netpyne.analysis')
print(subpack)

mod = parse.DocstringParser('netpyne.analysis.info')
print(mod)

func = parse.DocstringParser('netpyne.analysis.info.granger')
print(func)

classi = parse.DocstringParser('netpyne.specs.netParams.NetParams')



