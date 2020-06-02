"""
"""

from collections import OrderedDict



default_template_dict = OrderedDict()
default_template_dict['short_description'] = []
default_template_dict['long_description']  = []
default_template_dict['parameters']        = OrderedDict()
default_template_dict['returns']           = OrderedDict()
default_template_dict['yields']            = OrderedDict()
default_template_dict['receives']          = OrderedDict()
default_template_dict['raises']            = OrderedDict()
default_template_dict['warns']             = OrderedDict()
default_template_dict['other_parameters']  = OrderedDict()
default_template_dict['attributes']        = OrderedDict()
default_template_dict['methods']           = OrderedDict()
default_template_dict['see_also']          = OrderedDict()
default_template_dict['notes']             = []
default_template_dict['warnings']          = []
default_template_dict['references']        = []
default_template_dict['examples']          = []



def write_template_string(sections_dict):

        template_string = ''
        
        for section in sections_dict:
            template_string += '{' + section + '}'
        
        return template_string



class docstringTemplate:

    def __init__(self, sections_dict=default_template_dict):
        
        self.template_dict = sections_dict
        self.template_string = write_template_string(sections_dict)


    


