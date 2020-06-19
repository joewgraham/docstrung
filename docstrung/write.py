from . import get
from . import parse
from . import options

"""
create a default_writer function
create a google_style_writer object

change spacer to tab_size
"""


def default_writer(object_dict, options=options):

    initial_newline = options.initial_newline
    initial_indent = options.initial_indent
    spacer = options.spacer

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

    return docstring_string



def write_to_file():
    pass



