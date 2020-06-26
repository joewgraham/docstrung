"""
Can't assume indentation based on type, just saw a class defined in a try/except
    Problem seems limited to neuromlFormat, but should be handled
Need to start paths at netpyne top dir (not local dir)
Need to link to main GitHub repo (docstrung branch) in report
Move archive print statements to Docstrung
Just because the default is None, doesn't mean that's the input type
Include things to replace in brackets?  e.g. [input type], [Short description]
Maybe restore files that no longer import to their original state?
"""

import os
import inspect
from collections import OrderedDict

from . import get
from . import write
from . import parse
from . import options
from . import report


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

        name_list = object_name.split('.')

        self.object = imported_object
        self.fullname = object_name
        self.name = name_list.pop()
        self.parent = '.'.join(name_list)
        self.type = object_type
        self.file = get.get_object_file(object_name)
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

        if options.write_to_file:
            self.write_to_file()

        if options.create_report and self.docstring != self.original_docstring:
            self.create_report()

            if options.save_report:
                pass

            if options.submit_report:
                self.submit_report()
        
    def write_to_file(self):        
        write.write_to_file(self.object_dict, self.docstring, self.file, self.original_docstring, options=options)

    def create_report(self):
        self.report = report.create_report(self)

    def save_report(self):
        report.save_report(self)

    def submit_report(self):
        report.submit_report(self)



class Docstrung():

    def __init__(self, object_name, exclude=[], options=options):

        self.name = object_name
        self.object, self.type = get.get_object(object_name, return_type=True)
        self.all_docstrungs = []
        self.exclude = exclude
        self.process_package()
        

    def process_package(self):

        self.create_counters()
        print()
        print()
        print('  docstrung is processing:')
        print('  ============================')
        print('  object_name:', self.name)
        print('  object_type:', self.type)
        print()
        print('  items being processed:')
        print('  ============================')

        if self.type == 'package':

            print('exclude:', self.exclude)

            self.counters['packages']['total'] += 1
            print('  package:    ', self.name)
            package_docstrung = DocstrungDocstring(self.name, options=options)
            self.all_docstrungs.append(package_docstrung)
            if not package_docstrung.original_docstring:
                self.counters['packages']['no_docstring'] += 1
                self.counters['packages']['updated'] += 1
            elif package_docstrung.original_docstring != package_docstrung.docstring:
                self.counters['packages']['updated'] += 1

            print()
            self.subpackages = get.get_all_subpackages(self.name, options=options)
            for subpackage in self.subpackages:
                if subpackage not in self.exclude:
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
            self.modules = get.get_all_modules(self.name, options=options)
            for module in self.modules:
                if module not in self.exclude:
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
            self.functions = get.get_all_functions(self.name, options=options)
            for function in self.functions:
                if function not in self.exclude:
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
            self.classes = get.get_all_classes(self.name, options=options)
            for classi in self.classes:
                if classi not in self.exclude:
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
                self.methods = get.get_all_methods(self.name, options=options)
                for method in self.methods:
                    if method not in self.exclude:
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
        print('  object_name:', self.name)
        print('  object_type:', self.type)
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



