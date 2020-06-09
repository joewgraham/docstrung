from . import get
from . import parse
from . import template
from . import options

initial_newline = options.initial_newline
initial_indent = options.initial_indent
spacer = options.spacer

        
def write_docstring(docstring_template, object_dict, initial_newline=initial_newline, initial_indent=initial_indent, spacer=spacer):

    section_templates = docstring_template['subsection']
    docstring_template = docstring_template['main']

    options_dict = {}
    options_dict['initial_newline'] = initial_newline
    options_dict['initial_indent'] = initial_indent
    options_dict['spacer'] = spacer


    if initial_newline:
        initial_newline_string = '\n'
    else:
        initial_newline_string = ''

    docstring_string = initial_newline_string

    for section, section_template in docstring_template.items():

        if not section in section_templates:
            if object_dict[section]:
                docstring_string += section_template.format(**{**object_dict, **options_dict})

        else:

            if section in object_dict:

                if object_dict[section]:

                    docstring_string += section_templates[section].format(**{**object_dict, **options_dict})
                    
                    for subsection in object_dict[section]:

                        subsection_template = section_templates[section]
                        subsection_string = subsection_template.format(**{**subsection, **options_dict})

                        docstring_string += subsection_string

    return docstring_string



def write_to_file():
    pass



