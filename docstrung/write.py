from . import get
from . import parse
from . import template



        
def write_docstring(object_name, initial_newline=True, spacer='    '):


    # Need template and object_dict



    line_space = '\n' + spacer
    line_space_space = line_space + spacer
    if initial_newline:
        new_docstring += line_space

    new_docstring += line_space.join(parsed_docstring['short_description'])
    new_docstring += '\n\n'

    if parsed_docstring['long_description']:

        new_docstring += line_space.join(parsed_docstring['long_description'])
        new_docstring += '\n\n'

    if parsed_docstring['parameters']:

        new_docstring += spacer + 'Parameters\n'
        new_docstring += spacer + '----------\n'

        for param, param_dict in parsed_docstring['parameters'].items():

            new_docstring += spacer + param + ' : ' + str(param_dict['type']) + '\n'
            new_docstring += spacer + spacer + param_dict['description'] + '\n'

            if not 'default' in param_dict['description']:
                new_docstring += spacer + spacer + '**Default**: ``' + param_dict['default'] + '``\n'
                    
            if not 'options' in param_dict['description'] and not 'required' in param_dict['default']:
                new_docstring += spacer + spacer + '**Options**: \n '
            
            new_docstring += '\n'

        new_docstring += '\n'








    if parsed_docstring['methods']:

        new_docstring += spacer + 'Methods\n'
        new_docstring += spacer + '----------\n'

        for param, param_dict in parsed_docstring['methods'].items():

            new_docstring += spacer + param + ' : ' + str(param_dict['type']) + '\n'
            new_docstring += spacer + spacer + param_dict['description'] + '\n'

            if not 'default' in param_dict['description']:
                new_docstring += spacer + spacer + '**Default**: ``' + param_dict['default'] + '``\n'
                    
            if not 'options' in param_dict['description'] and not 'required' in param_dict['default']:
                new_docstring += spacer + spacer + '**Options**: \n '
            
            new_docstring += '\n'

        new_docstring += '\n'








    if parsed_docstring['returns']:

        new_docstring += spacer + 'Returns\n'
        new_docstring += spacer + '-------\n'
        new_docstring += spacer + parsed_docstring['returns']['type'] + '\n'
        new_docstring += spacer + spacer +  line_space_space.join(parsed_docstring['returns']['description'])
        new_docstring += '\n\n'

    if parsed_docstring['yields']:
        pass

    if parsed_docstring['receives']:
        pass

    if parsed_docstring['raises']:
        pass

    if parsed_docstring['warns']:
        pass

    if parsed_docstring['other_parameters']:
        pass

    if parsed_docstring['attributes']:
        pass

    if parsed_docstring['methods']:
        print('============================================================================================================')
        print('Missing some parsed methods (see write.py)')
        print("parsed_docstring['methods']:\n\n")
        print(parsed_docstring['methods'])
        print('\n\n')
        pass

    if parsed_docstring['see_also']:

            # new_docstring += spacer + 'See Also\n'
            # new_docstring += spacer + '--------\n'
            # new_docstring += spacer + module + ' :\n\n'
            pass

    if parsed_docstring['notes']:

        new_docstring += line_space.join(parsed_docstring['notes'])
        new_docstring += '\n\n'

    if parsed_docstring['warnings']:

        new_docstring += line_space.join(parsed_docstring['warnings'])
        new_docstring += '\n\n'

    if parsed_docstring['references']:

        new_docstring += line_space.join(parsed_docstring['references'])
        new_docstring += '\n\n'

    if parsed_docstring['examples']:

        # new_docstring += spacer + 'Examples\n'
        # new_docstring += spacer + '--------\n'
        # new_docstring += spacer + '>>> import netpyne, netpyne.examples.example\n'
        # new_docstring += spacer + '>>> ' + module + '.' + item + '()\n'
        pass

    return new_docstring


