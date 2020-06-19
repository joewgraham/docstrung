
import inspect
from collections import OrderedDict
from . import get
from . import parse
from . import options
from . import docstrung



def read_parameters(object_name):

    parameters = []
    signature = get.get_object_signature(object_name)
    
    if signature:

        imported_object, object_type = get.get_object(object_name, return_type=True)

        for param_name in signature.parameters:

            ParameterDict = docstrung.ParameterDict()
            ParameterDict['name'] = param_name
            param = signature.parameters[param_name]
            ParameterDict['default'] = param.default
            ParameterDict['description'] = 'Short description of ' + param_name
            
            if param.default is None:
                ParameterDict['type'] = 'None'
            else:
                ParameterDict['type'] = type(param.default).__name__
            
            if type(param.default) == type(inspect._empty):
                ParameterDict['default'] = 'Required'
                ParameterDict['type'] = ''
            
            elif ParameterDict['type'] == 'str':
                ParameterDict['default'] = "'" + ParameterDict['default'] + "'"
            
            else:
                ParameterDict['default'] = str(param.default)

            parameters.append(ParameterDict)

    return parameters



def default_parser(object_dict):

    from docstring_parser import parse

    object_type = object_dict['type']
    original_docstring = object_dict['original_docstring']
    object_dict['description'] = ['Short description of ' + object_dict['name']]

    parsed_docstring = None
    if original_docstring:
        parsed_docstring = parse(original_docstring)

    if parsed_docstring:

        if parsed_docstring.short_description:
            
            description = parsed_docstring.short_description
            # Split string into lines at newline, strip whitespace, and remove empty strings
            description = [line for line in [line.strip() for line in description.split(sep='\n')] if line]

            object_dict['description'] = description 

        if parsed_docstring.long_description:

            long_description = parsed_docstring.long_description
            # Split string into lines at newline, strip whitespace, and remove empty strings
            long_description = [line for line in [line.strip() for line in long_description.split(sep='\n')] if line]

            object_dict['long_description'] = long_description

        if object_type == 'package':
            pass

        elif object_type == 'module':
            pass

        elif object_type == 'class':
            pass

        elif object_type in ['function', 'method']:
            
            # replace attributes
            
            # replace parameters
            for parsed_param in parsed_docstring.params:

                for object_param in object_dict['parameters']:

                    if parsed_param.arg_name == object_param['name']:

                        if parsed_param.description:
                            object_param['description'] = parsed_param.description
                        if parsed_param.default:
                            object_param['default'] = parsed_param.default
                        if parsed_param.type_name:
                            object_param['type'] = parsed_param.type_name

            # replace returns

            # replace yields

            # replace raises

        elif object_type == 'attribute':
            pass

        else:
            pass

    return object_dict






