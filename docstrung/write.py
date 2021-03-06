from . import get
from . import parse
from . import options



def default_writer(object_dict, options=options):

    initial_newline = options.initial_newline
    initial_indent = options.initial_indent
    tab_size = options.tab_size

    if object_dict['type'] == 'package' or object_dict['type'] == 'module':

        if initial_newline:
            initial_newline_string = '\n'
        else:
            initial_newline_string = ''
        docstring_string = initial_newline_string
            
        if object_dict['description']:
            for line in object_dict['description']:
                docstring_string += line + '\n'
            docstring_string += '\n'

        if object_dict['long_description']:
            for line in object_dict['long_description']:
                docstring_string += line + '\n'
            docstring_string += '\n'

    elif object_dict['type'] == 'function' or object_dict['type'] == 'class':

        if initial_newline:
            initial_newline_string = '\n' + initial_indent
        else:
            initial_newline_string = ''

        docstring_string = initial_newline_string
        first_line_written = False

        if object_dict['description']:
            for line in object_dict['description']:
                if not first_line_written and initial_newline:
                    docstring_string += line + '\n'
                else:
                    docstring_string += initial_indent + line + '\n'
                first_line_written = True
            docstring_string += '\n'

        if object_dict['long_description']:
            for line in object_dict['long_description']:
                if not first_line_written and initial_newline:
                    docstring_string += line + '\n'
                else:
                    docstring_string += initial_indent + line + '\n'
                first_line_written = True
            docstring_string += '\n'

        if 'parameters' in object_dict:
            if object_dict['parameters']:
                
                docstring_string += initial_indent + 'Parameters\n'
                docstring_string += initial_indent + '----------\n'  

                for param_dict in object_dict['parameters']:

                    docstring_string += initial_indent + param_dict['name'] + ' : ' + param_dict['type'] + '\n'
                    docstring_string += initial_indent + tab_size + param_dict['description'].replace('\n', '\n' + initial_indent + tab_size) + '\n'

                    if 'required' in param_dict['default'] or 'Required' in param_dict['default']:
                        docstring_string += initial_indent + tab_size + '**Default:** *required*\n'
                    else:
                        desc = param_dict['description']
                        if not 'default' in desc and not 'Default' in desc:
                            docstring_string += initial_indent + tab_size + '**Default:** ``' + param_dict['default'] + '``\n'
                        if not 'options' in desc and not 'Options' in desc:
                            docstring_string += initial_indent + tab_size + '**Options:** ``<option>`` <description of option>\n '

                        # use_old = False
                        # if not use_old:
                        #     docstring_string += initial_indent + tab_size + '**Default:** ``' + param_dict['default'] + '``\n'
                        #     docstring_string += initial_indent + tab_size + '**Options:** \n '
                    
                    docstring_string += '\n'
            
        if 'returns' in object_dict:
            if object_dict['returns']:

                docstring_string += initial_indent + 'Returns\n'
                docstring_string += initial_indent + '-------\n'
                
                #docstring_string += '    ' + object_dict['returns']['type'] + '\n'
                #docstring_string += '        ' + object_dict['returns']['description']

                docstring_string += '\n\n'

        
        if 'yields' in object_dict:
            if object_dict['yields']:
                docstring_string += initial_indent + 'Yields\n'
                docstring_string += initial_indent + '------\n'
                docstring_string += '\n\n'
        
        if 'raises' in object_dict:
            if object_dict['raises']:
                docstring_string += initial_indent + 'Raises\n'
                docstring_string += initial_indent + '------\n'
                docstring_string += '\n\n'

        if 'see_also' in object_dict:
            if object_dict['see_also']:
                docstring_string += initial_indent + 'See Also\n'
                docstring_string += initial_indent + '--------\n'
                #docstring_string += '    ' + module + ' :'
                docstring_string += '\n\n'

        if 'examples' in object_dict:
            if object_dict['examples']:
                docstring_string += initial_indent + 'Examples\n'
                docstring_string += initial_indent + '--------\n'
                #docstring_string += '    >>> import netpyne, netpyne.examples.example\n'
                #docstring_string += '    >>> ' + module + '.' + item + '()\n'
                docstring_string += '\n\n'

    elif object_dict['type'] == 'method':
        pass
    
    return docstring_string



def write_to_file(object_dict, new_docstring, file_location, original_docstring=None, options=options):
    
    object_type = object_dict['type']
    object_name = object_dict['name'].split('.').pop()

    in_file = open(file_location, 'r')
    file_text = in_file.read()
    in_file.close()

    if original_docstring is not None:
        
        docstring_loc = file_text.find(original_docstring)

        if len(get.get_string_indexes(file_text, original_docstring)) > 1:
            raise Exception('The same docstring occurs in multiple locations.')
        
        if docstring_loc != -1:
            file_text = file_text.replace(original_docstring, new_docstring)
        else:
            raise Exception('  Error: original docstring exists but was not found in file.')

    else:

        if object_type == 'package' or object_type == 'module':
            docstring_loc = 0
            new_docstring = '"""' + new_docstring + '"""\n\n'
            
        if object_type == 'function': 
        
            func_loc = get.get_string_indexes(file_text, 'def ' + object_name + '(')

            if func_loc:
                obj_loc = func_loc[0] 
            else:
                raise Exception('  Error: could not find function in file.')

            docstring_loc = file_text.find('):', obj_loc) + 2
            new_docstring = '\n    """' + new_docstring + '\n    """\n\n'

        elif object_type == 'class': 

            class_loc = get.get_string_indexes(file_text, 'class ' + object_name + '(')

            if class_loc:
                obj_loc = class_loc[0]
            else:
                raise Exception('  Error: could not find class in file.')
        
            docstring_loc = file_text.find('):', obj_loc) + 2
            new_docstring = '\n    """' + new_docstring + '\n    """\n\n'
        
        file_text = file_text[:docstring_loc] + new_docstring + file_text[docstring_loc:]

    out_file = open(file_location, 'w')
    out_file.write(file_text)
    out_file.close()
