import importlib
import inspect



def get_subpackages(package_name): 
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

    return subpackages



def get_all_modules(package_name):
    """
    From the given package, return a list of all module names from all subpackages.
    """

    modules = []
    items = get_subpackages(package_name)

    for item in items:
        item = package_name + '.' + item
        subitems = get_subpackages(item)

        if not subitems:
            modules.append(item) 
        
        else:
            for subitem in subitems:
                subitem = item + '.' + subitem
                subsubitems = get_subpackages(subitem)

                if not subsubitems:
                    modules.append(subitem)
        
                else:
                    for subsubitem in subsubitems:
                        subsubitem = subitem + '.' + subsubitem
                        subsubsubitems = get_subpackages(subsubitem)

                        if not subsubsubitems:
                            modules.append(subsubitem)

    modules.sort()
    return modules



def get_functions(module_name, include_private=True):
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

    return functions



def get_all_functions(package_name, include_private=True, include_module=True):
    """
    From the given package, returns a list of all functions from all subpackages.
    """

    functions = []

    modules = get_all_modules(package_name)

    for module in modules:
        
        new_funcs = get_functions(module, include_private=include_private)
        if include_module:
            new_funcs = [module + '.' + function for function in new_funcs]

        functions.extend(new_funcs)

    return functions



def get_classes(module_name, include_private=True):
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

    return classes



def get_all_classes(package_name, include_private=True, include_module=True):
    """
    From the given package, returns a list of all classes from all subpackages.
    """

    classes = []

    modules = get_all_modules(package_name)

    for module in modules:
        
        new_classes = get_classes(module, include_private=include_private)
        if include_module:
            new_classes = [module + '.' + classi for classi in new_classes]

        classes.extend(new_classes)

    return classes



def get_methods(class_name):
    pass


def get_all_methods(package_name):
    pass


def get_docstring(object):
    pass






