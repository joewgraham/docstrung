from collections import OrderedDict


initial_newline = True 
spacer = '    '
include_private = False
parser = 'default_parser'
template = 'default_template'



# Class definitions for package objects

class ObjectDict(OrderedDict):
    def __init__(self):
        self['name']              = '' 
        self['type']              = ''
        self['default']           = ''
        self['description']       = []
        self['long_description']  = []
        self['warnings']          = []
        self['notes']             = []
        self['see_also']          = []
        self['examples']          = []
        self['references']        = []
        self['object']            = None


class AttributeDict(ObjectDict):
    def __init__(self):
        super().__init__()


class ParameterDict(ObjectDict):
    def __init__(self):
        super().__init__()


class ReturnsDict(ObjectDict):
    def __init__(self):
        super().__init__()


class YieldsDict(ObjectDict):
    def __init__(self):
        super().__init__()


class RaisesDict(ObjectDict):
    def __init__(self):
        super().__init__()


class FunctionDict(ObjectDict):
    def __init__(self):
        super().__init__()
        self['attributes'] = []
        self['parameters'] = []
        self['returns'] = []
        self['yields'] = []
        self['raises'] = []


class MethodDict(FunctionDict):
    def __init__(self):
        super().__init__()


class ClassDict(FunctionDict):
    def __init__(self):
        super().__init__()
        self['methods'] = []


class ModuleDict(ClassDict):
    def __init__(self):
        super().__init__()
        self['functions'] = []
        self['classes'] = []
        self['methods'] = []


class PackageDict(ModuleDict):
    def __init__(self):
        super().__init__()
        self['modules'] = []




# Docstring templates

class DocstringSection:

    def __init__(self, section_title=''):

        self.initial_newline = ''
        self.header = section_title
        self.content = None
        self.underscore = '-'



docstring_templates = OrderedDict()

docstring_templates['default_template'] = OrderedDict()

docstring_templates['default_template']['description'] = OrderedDict()
docstring_templates['default_template']['long_description'] = OrderedDict()
docstring_templates['default_template']['attributes'] = OrderedDict()
docstring_templates['default_template']['parameters'] = OrderedDict()
docstring_templates['default_template']['returns'] = OrderedDict()
docstring_templates['default_template']['yields'] = OrderedDict()
docstring_templates['default_template']['raises'] = OrderedDict()
docstring_templates['default_template']['warnings'] = OrderedDict()
docstring_templates['default_template']['notes'] = OrderedDict()
docstring_templates['default_template']['see_also'] = OrderedDict()
docstring_templates['default_template']['examples'] = OrderedDict()
docstring_templates['default_template']['references'] = OrderedDict()
    




# Class definitions for docstring template

class DocstringTemplate(OrderedDict):

    def __init__(self):

        self['description']       = DescriptionDocstringTemplate()
        self['long_description']  = Long_descriptionDocstringTemplate()
        self['attributes']        = AttributesDocstringTemplate()
        self['parameters']        = ParametersDocstringTemplate()
        self['returns']           = ReturnsDocstringTemplate()
        self['yields']            = YieldsDocstringTemplate()
        self['raises']            = RaisesDocstringTemplate()
        self['warnings']          = WarningsDocstringTemplate()
        self['notes']             = NotesDocstringTemplate()
        self['see_also']          = See_alsoDocstringTemplate()
        self['examples']          = ExamplesDocstringTemplate()
        self['references']        = ReferencesDocstringTemplate()






def write_template_string(sections_dict):

    template_string = ''
    
    for section in sections_dict:
        template_string += '{' + section + '}'
    
    return template_string







            









# class DocstringTemplate:

#     def __init__(self, sections_dict=default_template_dict):
        
#         self.template_dict = sections_dict
#         self.template_string = write_template_string(sections_dict)












    """
    'args': self._parse_parameters_section,
    'arguments': self._parse_parameters_section,
    'attention': partial(self._parse_admonition, 'attention'),
    'attributes': self._parse_attributes_section,
    'caution': partial(self._parse_admonition, 'caution'),
    'danger': partial(self._parse_admonition, 'danger'),
    'error': partial(self._parse_admonition, 'error'),
    'example': self._parse_examples_section,
    'examples': self._parse_examples_section,
    'hint': partial(self._parse_admonition, 'hint'),
    'important': partial(self._parse_admonition, 'important'),
    'keyword args': self._parse_keyword_arguments_section,
    'keyword arguments': self._parse_keyword_arguments_section,
    'methods': self._parse_methods_section,
    'note': partial(self._parse_admonition, 'note'),
    'notes': self._parse_notes_section,
    'other parameters': self._parse_other_parameters_section,
    'parameters': self._parse_parameters_section,
    'return': self._parse_returns_section,
    'returns': self._parse_returns_section,
    'raises': self._parse_raises_section,
    'references': self._parse_references_section,
    'see also': self._parse_see_also_section,
    'tip': partial(self._parse_admonition, 'tip'),
    'todo': partial(self._parse_admonition, 'todo'),
    'warning': partial(self._parse_admonition, 'warning'),
    'warnings': partial(self._parse_admonition, 'warning'),
    'warns': self._parse_warns_section,
    'yield': self._parse_yields_section,
    'yields': self._parse_yields_section,

    """















    


