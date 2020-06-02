import importlib
import inspect
import os



def get_subpackages(package_name, include_package=True): 
    """
    From a given package name, return a list of subpackage names 
    """

    package = importlib.import_module(package_name)
    items = package.__dir__()
    items = [item for item in items if not item.startswith('__')]
    subpackages = []

    for item in items:

        try:
            imp = importlib.import_module(package_name + '.' + item)
            subpackages.append(item)
        except:
            pass

    subpackages.sort()

    if include_package:
        subpackages = [package_name + '.' + subpackage for subpackage in subpackages]

    return subpackages



def get_all_modules(package_name, return_subpackages=False):
    """
    From the given package, return a list of all module names from all subpackages.

    This function could benefit from recursion...
    """

    modules = []
    subpackages = []
    items = get_subpackages(package_name, include_package=True)

    for item in items:
        subitems = get_subpackages(item, include_package=True)

        if not subitems:
            modules.append(item) 
        
        else:
            subpackages.append(item)
            for subitem in subitems:
                subsubitems = get_subpackages(subitem, include_package=True)

                if not subsubitems:
                    modules.append(subitem)

                else:
                    subpackages.append(subitem)
                    for subsubitem in subsubitems:
                        subsubsubitems = get_subpackages(subsubitem, include_package=True)

                        if not subsubsubitems:
                            modules.append(subsubitem)
                        else:
                            subpackages.append(subsubitem)

    modules.sort()
    subpackages.sort()

    if return_subpackages:
        return modules, subpackages
    else:
        return modules



def get_all_subpackages(package_name):

    modules, subpackages = get_all_modules(package_name, return_subpackages=True)

    return subpackages




def get_functions(module_name, include_private=True, include_module=True):
    """
    From the given module, return a list of all function names.
    """

    functions = []
    
    module = importlib.import_module(module_name)
    members = inspect.getmembers(module)
    members = [member for member in members if not member[0].startswith('__')]
    
    if not include_private:
        members = [member for member in members if not member[0].startswith('_')]

    for member in members:
        if inspect.isfunction(member[1]):
            if module == inspect.getmodule(member[1]):
                functions.append(member[0])

    if include_module:
        functions = [module_name + '.' + function for function in functions]

    return functions



def get_all_functions(package_name, include_private=True, include_module=True):
    """
    From the given package, returns a list of all functions from all subpackages.
    """

    functions = []
    modules = get_all_modules(package_name)

    for module in modules:
        
        new_funcs = get_functions(module, include_private=include_private, include_module=include_module)
        functions.extend(new_funcs)

    return functions



def get_classes(module_name, include_private=True, include_module=True):
    """
    From the given module, return a list of all class names.
    """

    classes = []
    
    module = importlib.import_module(module_name)
    members = inspect.getmembers(module)
    members = [member for member in members if not member[0].startswith('__')]
    
    if not include_private:
        members = [member for member in members if not member[0].startswith('_')]

    for member in members:
        if inspect.isclass(member[1]):
            if module == inspect.getmodule(member[1]):
                classes.append(member[0])

    if include_module:
        classes = [module_name + '.' + classi for classi in classes]

    return classes



def get_all_classes(package_name, include_private=True, include_module=True):
    """
    From the given package, returns a list of all classes from all subpackages.
    """

    classes = []
    modules = get_all_modules(package_name)

    for module in modules:
        
        new_classes = get_classes(module, include_private=include_private, include_module=include_module)
        classes.extend(new_classes)

    return classes



def get_methods(class_name, include_private=True, include_module=True):

    module_list = class_name.split('.')
    class_name = module_list.pop()
    module_name = '.'.join(module_list)
    imported_module = importlib.import_module(module_name)
    imported_class = getattr(imported_module, class_name)
    
    methods = inspect.getmembers(imported_class, predicate=inspect.isfunction) 
    methods = [method[0] for method in methods if not method[0].startswith('__')]

    if not include_private:
        methods = [method for method in methods if not method.startswith('_')]

    if include_module:
        methods = [module_name + '.' + class_name + '.' + method for method in methods]

    return methods



def get_all_methods(package_name, include_private=True, include_module=True):
    
    methods = []
    classes = get_all_classes(package_name, include_private=include_private, include_module=include_module)

    for classi in classes:

        new_methods = get_methods(classi, include_private=include_private, include_module=include_module)
        methods.extend(new_methods)

    return methods



def get_docstring(object_name):
    
    imported_object, object_type = get_object(object_name, return_type=True)

    docstring = imported_object.__doc__

    return docstring



def get_package_location(package_name):
    """
    Returns the path to the package directory.
    """

    package = importlib.import_module(package_name)

    location = os.path.split(package.__file__)[0]

    return location



def get_object_file(object_name):
    
    imported_object, object_type = get_object(object_name, return_type=True)

    object_file = imported_object.__file__

    return object_file



def get_object_signature(object_name):
    
    imported_object, object_type = get_object(object_name, return_type=True)

    signature = inspect.signature(imported_object)        

    return signature



def get_object(object_name, return_type=True):
    
    try:

        # Handles subpackages and modules
        imported_object = importlib.import_module(object_name)
        
        file_loc = imported_object.__file__
        object_type = ''
        if file_loc.endswith('__init__.py'):
            object_type += 'package'
        else:
            object_type += 'module'
    
    except:
        
        # Handles functions and classes
        module_list = object_name.split('.')
        object_name = module_list.pop()
        module_name = '.'.join(module_list)
        
        try:

            imported_module = importlib.import_module(module_name)
            imported_object = getattr(imported_module, object_name)
            object_type = type(imported_object).__name__
    
        except:
            
            # Handles methods
            object_name = module_list.pop()
            class_name = module_list.pop()
            module_name = '.'.join(module_list)
            imported_module = importlib.import_module(module_name)
            imported_class = getattr(imported_module, class_name)
            imported_object = getattr(imported_class, object_name)
            object_type = "method"


    if return_type:
        return imported_object, object_type
    else:
        return imported_object



def get_object_type(object_name):

    imported_object, object_type = get_object(object_name, return_type=True)

    return object_type

    












