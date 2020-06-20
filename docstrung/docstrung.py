"""
Fix: **Default**: ``required``

Fix: second scipt should have ``
    script : 
        Short description of script
"""

from collections import OrderedDict

from . import get
from . import write
from . import parse
from . import options


# Class definitions for package objects
class ObjectDict(OrderedDict):
    def __init__(self):
        self['name']               = '' 
        self['type']               = ''
        self['default']            = ''
        self['description']        = []
        self['long_description']   = []
        self['warnings']           = []
        self['notes']              = []
        self['see_also']           = []
        self['examples']           = []
        self['references']         = []
        self['object']             = None


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
        self['raises'] = []
        self['returns'] = None
        self['yields'] = None
        

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



class ParsedDocstring:
    
    def __init__(self, object_name, options=options):

        imported_object, object_type = get.get_object(object_name, return_type=True)

        self.object_name = object_name
        self.object_type = object_type
        self.object = imported_object
        self.original_docstring = get.get_docstring(object_name)
        
        if object_type == 'package':
            self.object_dict = PackageDict()
        elif object_type == 'module':
            self.object_dict = ModuleDict()
        elif object_type == 'class':
            self.object_dict = ClassDict()
        elif object_type == 'function' or object_type == 'method':
            self.object_dict = FunctionDict()
            self.object_dict['parameters'] = parse.read_parameters(object_name)
        else:
            self.object_dict = ObjectDict()

        self.object_dict['name']   = object_name 
        self.object_dict['type']   = object_type
        self.object_dict['object'] = imported_object
        self.object_dict['original_docstring'] = self.original_docstring

        self.docstring_parser = getattr(parse, options.docstring_parser)
        self.object_dict = self.docstring_parser(self.object_dict)
        self.docstring_writer = getattr(write, options.docstring_writer)



class DocstrungDocstring(ParsedDocstring):

    def __init__(self, object_name, options=options):
        
        super().__init__(object_name, options=options)

        self.docstring = self.docstring_writer(self.object_dict, options=options)



class Docstrung():

    def __init__(self, object_name, options=options):

        self.object_name = object_name
        self.object, self.object_type = get.get_object(object_name, return_type=True)
        self.all_docstrungs = []
        self.process_package()
        

    def process_package(self):

        self.create_counters()
        print()
        print()
        print('  docstrung is processing:')
        print('  ============================')
        print('  object_name:', self.object_name)
        print('  object_type:', self.object_type)
        print()
        print('  items being docstrung:')
        print('  ============================')

        if self.object_type == 'package':

            self.counters['packages']['total'] += 1
            print('  package:    ', self.object_name)
            package_docstrung = DocstrungDocstring(self.object_name, options=options)
            self.all_docstrungs.append(package_docstrung)
            if not package_docstrung.original_docstring:
                self.counters['packages']['no_docstring'] += 1
                self.counters['packages']['updated'] += 1
            elif package_docstrung.original_docstring != package_docstrung.docstring:
                self.counters['packages']['updated'] += 1

            print()
            self.subpackages = get.get_all_subpackages(self.object_name, options=options)
            for subpackage in self.subpackages:
                self.counters['packages']['total'] += 1
                print('  subpackage: ', subpackage)
                subpackage_docstrung = DocstrungDocstring(subpackage, options=options)
                self.all_docstrungs.append(subpackage_docstrung)
                if not subpackage_docstrung.original_docstring:
                    self.counters['packages']['no_docstring'] += 1
                    self.counters['packages']['updated'] += 1
                elif subpackage_docstrung.original_docstring != subpackage_docstrung.docstring:
                    self.counters['packages']['updated'] += 1

            print()
            self.modules = get.get_all_modules(self.object_name, options=options)
            for module in self.modules:
                self.counters['modules']['total'] += 1
                print('  module:     ', module)
                module_docstrung = DocstrungDocstring(module, options=options)
                self.all_docstrungs.append(module_docstrung)
                if not module_docstrung.original_docstring:
                    self.counters['modules']['no_docstring'] += 1
                    self.counters['modules']['updated'] += 1
                elif module_docstrung.original_docstring != module_docstrung.docstring:
                    self.counters['modules']['updated'] += 1

            print()
            self.functions = get.get_all_functions(self.object_name, options=options)
            for function in self.functions:
                self.counters['functions']['total'] += 1
                print('  function:   ', function)
                function_docstrung = DocstrungDocstring(function, options=options)
                self.all_docstrungs.append(function_docstrung)
                if not function_docstrung.original_docstring:
                    self.counters['functions']['no_docstring'] += 1
                    self.counters['functions']['updated'] += 1
                elif function_docstrung.original_docstring != function_docstrung.docstring:
                    self.counters['functions']['updated'] += 1

            print()
            self.classes = get.get_all_classes(self.object_name, options=options)
            for classi in self.classes:
                self.counters['classes']['total'] += 1
                print('  class:      ', classi)
                class_docstrung = DocstrungDocstring(classi, options=options)
                self.all_docstrungs.append(class_docstrung)
                if not class_docstrung.original_docstring:
                    self.counters['classes']['no_docstring'] += 1
                    self.counters['classes']['updated'] += 1
                elif class_docstrung.original_docstring != class_docstrung.docstring:
                    self.counters['classes']['updated'] += 1

            if options.include_methods:
                print()
                self.methods = get.get_all_methods(self.object_name, options=options)
                for method in self.methods:
                    self.counters['methods']['total'] += 1
                    print('  method:     ', method)
                    method_docstrung = DocstrungDocstring(method, options=options)
                    self.all_docstrungs.append(method_docstrung)
                    if not method_docstrung.original_docstring:
                        self.counters['methods']['no_docstring'] += 1
                        self.counters['methods']['updated'] += 1
                    elif method_docstrung.original_docstring != method_docstrung.docstring:
                        self.counters['methods']['updated'] += 1


        self.sum_counters()
        

        print()
        print()
        print('  docstrung processed:')
        print('  ============================')
        print('  object_name:', self.object_name)
        print('  object_type:', self.object_type)
        print()
        print('  Total items docstrung:')
        print('  ----------------------------')
        print('  number of items:', self.counters['total']['total'])
        print('     undocumented:', self.counters['total']['no_docstring'])
        print('          updated:', self.counters['total']['updated'])
        print()
        print('  Packages docstrung:')
        print('  ----------------------------')
        print('  number of items:', self.counters['packages']['total'])
        print('     undocumented:', self.counters['packages']['no_docstring'])
        print('          updated:', self.counters['packages']['updated'])
        print()
        print('  Modules docstrung:')
        print('  ----------------------------')
        print('  number of items:', self.counters['modules']['total'])
        print('     undocumented:', self.counters['modules']['no_docstring'])
        print('          updated:', self.counters['modules']['updated'])
        print()
        print('  Functions docstrung:')
        print('  ----------------------------')
        print('  number of items:', self.counters['functions']['total'])
        print('     undocumented:', self.counters['functions']['no_docstring'])
        print('          updated:', self.counters['functions']['updated'])
        print()
        print('  Classes docstrung:')
        print('  ----------------------------')
        print('  number of items:', self.counters['classes']['total'])
        print('     undocumented:', self.counters['classes']['no_docstring'])
        print('          updated:', self.counters['classes']['updated'])
        print()
        print('  Methods docstrung:')
        print('  ----------------------------')
        print('  number of items:', self.counters['methods']['total'])
        print('     undocumented:', self.counters['methods']['no_docstring'])
        print('          updated:', self.counters['methods']['updated'])
        print()


    def create_counters(self):

        self.counters = OrderedDict()
        self.counters['total'] = OrderedDict()
        self.counters['total']['no_docstring'] = 0
        self.counters['total']['bad_docstring'] = 0
        self.counters['total']['updated'] = 0
        self.counters['total']['total'] = 0
        self.counters['packages'] = OrderedDict()
        self.counters['packages']['no_docstring'] = 0
        self.counters['packages']['bad_docstring'] = 0
        self.counters['packages']['updated'] = 0
        self.counters['packages']['total'] = 0
        self.counters['modules'] = OrderedDict()
        self.counters['modules']['no_docstring'] = 0
        self.counters['modules']['bad_docstring'] = 0
        self.counters['modules']['updated'] = 0
        self.counters['modules']['total'] = 0
        self.counters['functions'] = OrderedDict()
        self.counters['functions']['no_docstring'] = 0
        self.counters['functions']['bad_docstring'] = 0
        self.counters['functions']['updated'] = 0
        self.counters['functions']['total'] = 0
        self.counters['classes'] = OrderedDict()
        self.counters['classes']['no_docstring'] = 0
        self.counters['classes']['bad_docstring'] = 0
        self.counters['classes']['updated'] = 0
        self.counters['classes']['total'] = 0
        self.counters['methods'] = OrderedDict()
        self.counters['methods']['no_docstring'] = 0
        self.counters['methods']['bad_docstring'] = 0
        self.counters['methods']['updated'] = 0
        self.counters['methods']['total'] = 0


    def sum_counters(self):

        sc = self.counters

        sc['total']['total'] = sc['packages']['total']  \
                             + sc['modules']['total']   \
                             + sc['functions']['total'] \
                             + sc['classes']['total']   \
                             + sc['methods']['total']  

        sc['total']['no_docstring'] = sc['packages']['no_docstring']  \
                                    + sc['modules']['no_docstring']   \
                                    + sc['functions']['no_docstring'] \
                                    + sc['classes']['no_docstring']   \
                                    + sc['methods']['no_docstring']  

        sc['total']['bad_docstring'] = sc['packages']['bad_docstring']  \
                                     + sc['modules']['bad_docstring']   \
                                     + sc['functions']['bad_docstring'] \
                                     + sc['classes']['bad_docstring']   \
                                     + sc['methods']['bad_docstring']  

        sc['total']['updated'] = sc['packages']['updated']  \
                               + sc['modules']['updated']   \
                               + sc['functions']['updated'] \
                               + sc['classes']['updated']   \
                               + sc['methods']['updated']  


# print()
# print('  your original package was copied here:')
# print('     ', archive_dir )
# print()
# print('  your docstrung package is here: ')
# print('     ', package_dir)
# print()



