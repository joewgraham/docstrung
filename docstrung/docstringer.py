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


initial_newline = options.initial_newline
spacer          = options.spacer
include_private = options.include_private





def docstringer_subpackage():
    pass

def docstringer_module():
    pass

def docstringer_function(function_name, initial_newline=initial_newline, spacer=spacer):
    
    new_docstring = write.write_docstring(function_name, initial_newline=initial_newline, spacer=spacer)


def docstringer_class(class_name, initial_newline=initial_newline, spacer=spacer):
    
    new_docstring = write.write_docstring(class_name, initial_newline=initial_newline, spacer=spacer)


def docstringer_method(method_name, initial_newline=initial_newline, spacer=spacer):

    new_docstring = write.write_docstring(method_name, initial_newline=initial_newline, spacer=spacer)

    



















def docstringer(object_name, initial_newline=initial_newline, spacer=spacer):

    print()
    print(object_name)
    print('============================================================')

    imported_object, object_type = get.get_object(object_name, return_type=True)

    print('object_type:', object_type)
    
    if object_type == 'package':

        subpackages = get.get_all_subpackages(object_name, include_private=include_private)
        print()
        print('subpackages:', subpackages)
        print()
        for subpackage in subpackages:
            print()
            print('subpackage: ', subpackage)

        modules = get.get_all_modules(object_name, include_private=include_private)
        print()
        print('modules:', modules)
        print()
        for module in modules:
            print()
            print('module:', module)

        functions = get.get_all_functions(object_name, include_private=include_private)
        print()
        print('functions:', functions)
        print()
        for function in functions:
            print()
            print('function:', function)
            docstringer_function(function, initial_newline=initial_newline, spacer=spacer)

        classes = get.get_all_classes(object_name, include_private=include_private)
        print()
        print('classes:', classes)
        print()
        for classi in classes:
            print()
            print('class:', classi)
            docstringer_class(classi, initial_newline=initial_newline, spacer=spacer)

        methods = get.get_all_methods(object_name, include_private=include_private)
        print()
        print('methods:', methods)
        print()
        for method in methods:
            print()
            print('method:', method)
            docstringer_method(method, initial_newline=initial_newline, spacer=spacer)






















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


