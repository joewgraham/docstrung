import inspect
from collections import OrderedDict
from numpydoc.docscrape import FunctionDoc, ClassDoc
from . import get
from .template import docstringTemplate
from .template import default_template_dict



default_docstringTemplate = docstringTemplate(sections_dict=default_template_dict)



class docstringParser:

    def __init__(self):

        pass



def parse_parameters(object_name):

    signature = get.get_object_signature(object_name)
    params_dict = OrderedDict()

    for param_name in signature.parameters:

        params_dict[param_name] = {}
        param = signature.parameters[param_name]
        params_dict[param_name]['default'] = param.default
        params_dict[param_name]['description'] = 'Short description of ' + param_name
        
        if param.default is None:
            params_dict[param_name]['type'] = None
        else:
            params_dict[param_name]['type'] = type(param.default).__name__
        
        if type(param.default) == type(inspect._empty):
            params_dict[param_name]['default'] = 'required'
            params_dict[param_name]['type'] = ''
        elif params_dict[param_name]['type'] == 'str':
            params_dict[param_name]['default'] = "'" + params_dict[param_name]['default'] + "'"
        else:
            params_dict[param_name]['default'] = str(param.default)


    return params_dict



def parse_docstring(object_name, template=default_docstringTemplate):

    imported_object, object_type = get.get_object(object_name, return_type=True)
    print()
    print('parse_docstring imported_object:', imported_object)
    print()

    try:
        parsed = FunctionDoc(imported_object)
        
        print()
        print(object_name)
        print('=============================')
        print('Successfully parsed docstring')

        if parsed['Parameters']:
            print('  Parameters were parsed.')
            parsable = True
        else:
            print('  Parameters were not parsed.')
            parsable = False
    except:
        print('Parsing failed.')
        parsable = False


    docstring_sections = template.template_dict
    
    if parsed['Summary']:
        docstring_sections['short_description'] = parsed['Summary']
    else:
        docstring_sections['short_description'] = ['Short description of ' + object_name]
    
    if parsed['Extended Summary']:
        docstring_sections['long_description '] = parsed['Extended Summary']

    docstring_sections['parameters'] = parse_parameters(object_name)
    for param in docstring_sections['parameters']:
        
        if param in parsed:

            if parsed['parameters'][param]['type']:
                docstring_sections['parameters'][param]['type'] = parsed['parameters'][param]['type']

            if parsed['parameters'][param]['default']:
                docstring_sections['parameters'][param]['default'] = parsed['parameters'][param]['default']

            if parsed['parameters'][param]['description']:
                docstring_sections['parameters'][param]['description'] = parsed['parameters'][param]['description']

    for param in parsed['Returns']:
        docstring_sections['returns']['name'] = param.name
        docstring_sections['returns']['type'] = param.type
        docstring_sections['returns']['description'] = param.desc
    
    for param in parsed['Yields']:
        docstring_sections['yields'][param.name] = {'type': param.type, 'description': param.desc}
    
    for param in parsed['Receives']:
        docstring_sections['receives'][param.name] = {'type': param.type, 'description': param.desc}
    
    for param in parsed['Raises']:
        docstring_sections['raises'][param.name] = {'type': param.type, 'description': param.desc}
    
    for param in parsed['Warns']:
        docstring_sections['warns'][param.name] = {'type': param.type, 'description': param.desc}

    for param in parsed['Other Parameters']:
        docstring_sections['other_parameters'][param.name] = {'type': param.type, 'description': param.desc}

    for param in parsed['Attributes']:
        docstring_sections['attributes'][param.name] = {'type': param.type, 'description': param.desc}    
    
    for param in parsed['Methods']:
        docstring_sections['methods'][param.name] = {'type': param.type, 'description': param.desc}
    
    for param in parsed['See Also']:            
        docstring_sections['see_also'][param[0][0][0]] = {'type': None, 'description': param[0][0][1]}

    for param in parsed['Notes']:
        docstring_sections['notes'][param.name] = {'type': param.type, 'description': param.desc}
    
    for param in parsed['Warnings']:
        docstring_sections['warnings'][param.name] = {'type': param.type, 'description': param.desc}

    for param in parsed['References']:
        docstring_sections['references'][param.name] = {'type': param.type, 'description': param.desc}

    docstring_sections['examples'] = parsed['Examples']

    return docstring_sections

