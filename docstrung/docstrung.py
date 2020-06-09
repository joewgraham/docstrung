"""
Fix: **Default**: ``required``

Fix: second scipt should have ``
    script : 
        Short description of script
"""

from . import get
from . import write
from . import template
from . import parse
from . import options

from .parse import ParsedDocstring

# Create a template dictionary
class Docstrung():

    def __init__(self, object_name, docstring_template=options.docstring_template, options=options, recursive=True):

        self.object_name = object_name
        self.object, self.object_type = get.get_object(object_name, return_type=True)
        self.all_docstrungs = []

        self.main_template = template.docstring_templates[docstring_template]['main']
        self.subsection_templates = template.docstring_templates[docstring_template]['subsection']

        self.all_docstrungs = []

        print()
        print('docstrung is processing:')
        print('========================')
        print('object_name:', self.object_name)
        print('object_type:', self.object_type)
        print()
        print('items docstrung')
        print('===============')

        if self.object_type == 'package':

            print('package:    ', self.object_name)
            package_docstrung = ParsedDocstring(object_name, parser_function=options.docstring_parser)
            self.all_docstrungs.append(package_docstrung)

            print()
            self.subpackages = get.get_all_subpackages(object_name, include_private=options.include_private)
            for subpackage in self.subpackages:
                print('subpackage: ', subpackage)
                subpackage_docstrung = ParsedDocstring(subpackage, parser_function=options.docstring_parser)
                self.all_docstrungs.append(subpackage_docstrung)

            print()
            self.modules = get.get_all_modules(object_name, include_private=options.include_private)
            for module in self.modules:
                print('module:     ', module)
                module_docstrung = ParsedDocstring(module, parser_function=options.docstring_parser)
                self.all_docstrungs.append(module_docstrung)

            print()
            self.functions = get.get_all_functions(object_name, include_private=options.include_private)
            for function in self.functions:
                print('function:   ', function)
                function_docstrung = ParsedDocstring(function, parser_function=options.docstring_parser)
                self.all_docstrungs.append(function_docstrung)

            print()
            self.classes = get.get_all_classes(object_name, include_private=options.include_private)
            for classi in self.classes:
                print('class:      ', classi)
                class_docstrung = ParsedDocstring(classi, parser_function=options.docstring_parser)
                self.all_docstrungs.append(class_docstrung)

            print()
            self.methods = get.get_all_methods(object_name, include_private=options.include_private)
            for method in self.methods:
                print('method:     ', method)
                method_docstrung = ParsedDocstring(method, parser_function=options.docstring_parser)
                self.all_docstrungs.append(method_docstrung)





# # Set up the counters
# # -------------------
# item_count = 0
# undoc_count = 0
# bad_count = 0
# good_count = 0


# print('docstringer is processing the following functions and classes:')
# print('==============================================================')

# for module in modules_list:

#     imp_mod = imp_item = imp_file = options = old_docs = None
    
#     for item in modules_dict[module]:

#         item_count += 1

#         print(module + '.' + item)
        
#         imp_mod = importlib.import_module(module)
#         imp_item = getattr(imp_mod, item)
#         imp_file = imp_mod.__file__
#         options = inspect.signature(imp_item)        
#         old_docs = imp_item.__doc__

#         # Create dictionaries to hold the docstring parts

#         doc_dict = OrderedDict()
#         doc_dict['short_desc'] = 'Description of ' + module + '.' + item
#         doc_dict['long_desc'] = None
#         doc_dict['returns'] = {'description': 'Description of return.', 'type': 'return_type'}
        
#         params_dict = OrderedDict()
#         for param_name in options.parameters:

#             params_dict[param_name] = {}
#             param = options.parameters[param_name]
#             params_dict[param_name]['default'] = param.default
#             params_dict[param_name]['description'] = 'Description of ' + param_name
            
#             if param.default is None:
#                 params_dict[param_name]['type'] = ''
#             else:
#                 params_dict[param_name]['type'] = type(param.default).__name__
            
#             if type(param.default) == type(inspect._empty):
#                 params_dict[param_name]['default'] = 'required'
#                 params_dict[param_name]['type'] = ''
#             elif params_dict[param_name]['type'] == 'str':
#                 params_dict[param_name]['default'] = "'" + params_dict[param_name]['default'] + "'"
#             else:
#                 params_dict[param_name]['default'] = str(param.default)

    
#         # process old docs here
        
#         if not old_docs:

#             undoc_count += 1

#         elif old_docs is not None:

#             try:
#                 parsed = parse(old_docs)
#                 if parsed.params:
#                     use_old = True
#                 else:
#                     use_old = False
#                     bad_count += 1
#             except:
#                 use_old = False
#                 bad_count += 1

#             if use_old:

#                 good_count += 1

#                 doc_dict['short_desc'] = parsed.short_description
#                 doc_dict['long_desc'] = parsed.long_description

#                 if parsed.returns is not None:
#                     doc_dict['returns']['description'] = parsed.returns.description
#                     if parsed.returns.type_name is not None:
#                         doc_dict['returns']['type'] = parsed.returns.type_name
#                     else:
#                         doc_dict['returns']['type'] = 'None'

#                 for param in parsed.params:       

#                     if param.arg_name in params_dict:

#                         params_dict[param.arg_name]['description'] = param.description
#                         if param.type_name is None:
#                             params_dict[param.arg_name]['type'] = 'None'
#                         else:
#                             params_dict[param.arg_name]['type'] = param.type_name



#         # Write out new docstring

#         new_docs = doc_dict['short_desc'].replace('\n', '\n    ') + '\n\n'

#         if doc_dict['long_desc']:
#             new_docs = doc_dict['long_desc'].replace('\n', '\n    ') + '\n\n'

#         new_docs += '    Parameters\n'
#         new_docs += '    ----------\n'

#         for param, param_dict in params_dict.items():

#             new_docs += '    ' + param + ' : ' + param_dict['type'] + '\n'
#             new_docs += '        ' + param_dict['description'].replace('\n', '\n        ') + '\n'

#             if param_dict['default'] == 'required':
#                 new_docs += '        **(required)**\n'
#             else:
#                 if not use_old:
#                     new_docs += '        **Default**: ``' + param_dict['default'] + '``\n'
#                     new_docs += '        **Options**: \n '
            
#             new_docs += '\n'

#         new_docs += '\n'

#         new_docs += '    Returns\n'
#         new_docs += '    -------\n'
#         new_docs += '    ' + doc_dict['returns']['type'] + '\n'
#         new_docs += '        ' + doc_dict['returns']['description'] + '\n\n'

#         new_docs += '    See Also\n'
#         new_docs += '    --------\n'
#         new_docs += '    ' + module + ' :\n\n'

#         new_docs += '    Examples\n'
#         new_docs += '    --------\n'
#         new_docs += '    >>> import netpyne, netpyne.examples.example\n'
#         new_docs += '    >>> ' + module + '.' + item + '()\n'

        
#         # Read the appropriate Python file into a string
#         in_file = open(imp_file, 'r')
#         file_text = in_file.read()
#         in_file.close()

#         if old_docs is None:
#             doc_loc = -1
#         else:
#             doc_loc = file_text.find(old_docs)
            
#         if doc_loc != -1:

#             new_docs += '    '
#             file_text = file_text.replace(old_docs, new_docs)
        
#         else:

#             def_loc = find_all(file_text, 'def ' + item + '(')
#             class_loc = find_all(file_text, 'class ' + item + '(')

#             if def_loc:
#                 obj_loc = def_loc[0] 
#             if class_loc:
#                 obj_loc = class_loc[0]

#             doc_loc = file_text.find('):', obj_loc) + 2

#             new_docs = '\n    """' + new_docs + '\n    """\n\n'
            
#             file_text = file_text[:doc_loc] + new_docs + file_text[doc_loc:]

#         out_file = open(imp_file, 'w')
#         out_file.write(file_text)
#         out_file.close()

                    


# print()
# print('==============================================================')
# print('  docstringer complete')
# print('  docstrings created   :', item_count)
# print('  prev undocumented    :', undoc_count)
# print('  bad docstrings unused:', bad_count)
# print('  good docstrings used :', good_count)
# print()
# print('  your original package was copied here:')
# print('     ', archive_dir )
# print()
# print('  your docstrung package is here: ')
# print('     ', package_dir)
# print()







# '''
# Modularize the code
#     doc_dict_from_module
#     parse_docstring
#     use_old_docstring
#     write_docstring 
#     replace docstring
#     main function

# Look into auto-getting all functions/classes

# Dealing with classes
#     Need to document class methods
#     Need to format output for classes
#         Need to remove return, return_type, examples from classes

# Create GitHub issues with copy of original docstrings

# Go through Sphinx warnings

# Fix See Also parentheses

# Make docstringer into a package?
# '''


