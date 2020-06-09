
import inspect
from collections import OrderedDict
from . import get
from . import template
from . import parse
from . import options



ObjectDict    = template.ObjectDict
AttributeDict = template.AttributeDict
ParameterDict = template.ParameterDict
ReturnsDict   = template.ReturnsDict
YieldsDict    = template.YieldsDict
RaisesDict    = template.RaisesDict
FunctionDict  = template.FunctionDict
MethodDict    = template.MethodDict
ClassDict     = template.ClassDict
ModuleDict    = template.ModuleDict
PackageDict   = template.PackageDict



class DocstringParser:
    
    def __init__(self, object_name, parser_function=options.docstring_parser):

        imported_object, object_type = get.get_object(object_name, return_type=True)

        self.object_name = object_name
        self.object_type = object_type
        self.object = imported_object
        self.original_docstring = get.get_docstring(object_name)
        
        if object_type == 'package':
            self.object_dict = template.PackageDict()
        elif object_type == 'module':
            self.object_dict = template.ModuleDict()
        elif object_type == 'class':
            self.object_dict = template.ClassDict()
        elif object_type == 'function' or object_type == 'method':
            self.object_dict = template.FunctionDict()
            self.object_dict['parameters'] = parse_parameters(object_name)
        else:
            self.object_dict = template.ObjectDict()

        self.object_dict['name']   = object_name 
        self.object_dict['type']   = object_type
        self.object_dict['object'] = imported_object
        self.object_dict['original_docstring'] = self.original_docstring

        parser_function = getattr(parse, parser_function)
        self.object_dict = parser_function(self.object_dict)



def parse_parameters(object_name):

    parameters = []
    signature = get.get_object_signature(object_name)
    
    if signature:

        imported_object, object_type = get.get_object(object_name, return_type=True)

        for param_name in signature.parameters:

            ParameterDict = template.ParameterDict()
            ParameterDict['name'] = param_name
            param = signature.parameters[param_name]
            ParameterDict['default'] = param.default
            ParameterDict['description'] = 'Short description of ' + param_name
            
            if param.default is None:
                ParameterDict['type'] = 'None'
            else:
                ParameterDict['type'] = type(param.default).__name__
            
            if type(param.default) == type(inspect._empty):
                ParameterDict['default'] = 'required'
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

    parsed_docstring = None
    if original_docstring:
        parsed_docstring = parse(original_docstring)

    if parsed_docstring:

        if parsed_docstring.short_description:
            object_dict['description'] = parsed_docstring.short_description

        if parsed_docstring.long_description:
            object_dict['long_description'] = parsed_docstring.long_description

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






