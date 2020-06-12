from collections import OrderedDict
from . import options



# Create the templates dictionary
docstring_templates = {}



# Define the default template
docstring_templates['default_template'] = {}

docstring_templates['default_template']['main'] = OrderedDict()
main = docstring_templates['default_template']['main']

main['description'] = '{initial_indent}{description}\n\n'
main['long_description'] = '{initial_indent}{long_description}\n\n'

main['attributes'] = '{initial_indent}Attributes\n'
main['attributes'] += '{initial_indent}----------\n'

main['parameters'] = '{initial_indent}Parameters\n'
main['parameters'] += '{initial_indent}----------\n'

main['returns'] = '{initial_indent}Returns\n'
main['returns'] += '{initial_indent}-------\n'

main['yields'] = '{initial_indent}Yields\n'
main['yields'] += '{initial_indent}------\n'

main['raises'] = '{initial_indent}Raises\n'
main['raises'] += '{initial_indent}------\n'

main['warnings'] = '{initial_indent}Warnings\n'
main['warnings'] += '{initial_indent}--------\n'

main['notes'] = '{initial_indent}Notes\n'
main['notes'] += '{initial_indent}-----\n'

main['see_also'] = '{initial_indent}See Also\n'
main['see_also'] += '{initial_indent}--------\n'

main['examples'] = '{initial_indent}Examples\n'
main['examples'] += '{initial_indent}--------\n'

main['references'] = '{initial_indent}References\n'
main['references'] += '{initial_indent}----------\n'

docstring_templates['default_template']['subsection'] = {}
subsection = docstring_templates['default_template']['subsection']

subsection['attributes'] = '{initial_indent}{name} : {type}\n'
subsection['attributes'] += '{initial_indent}{spacer}{description}\n'
subsection['attributes'] += '{initial_indent}{spacer}**Default:**{default}\n'
subsection['attributes'] += '{initial_indent}{spacer}**Options:**\n\n'

subsection['parameters'] = '{initial_indent}{name} : {type}\n'
subsection['parameters'] += '{initial_indent}{spacer}{description}\n'
subsection['parameters'] += '{initial_indent}{spacer}**Default:**{default}\n'
subsection['parameters'] += '{initial_indent}{spacer}**Options:**\n\n'

subsection['returns'] = '{initial_indent}{type}\n'
subsection['returns'] += '{initial_indent}{spacer}{description}\n\n'

subsection['yields'] = '{initial_indent}{type}\n'
subsection['yields'] += '{initial_indent}{spacer}{description}\n\n'

subsection['raises'] = '{initial_indent}{type}\n'
subsection['raises'] += '{initial_indent}{spacer}{description}\n\n'

