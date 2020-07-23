import os
import json
import requests

from . import get
from . import options



def create_report(docstring_object):
    
    doc = docstring_object
    
    report_string = 'Check the docstring for {}: `{}`'.format(doc.type, doc.name)
    report_string += '\n\n'

    report_string += 'The docstring for the {} `{}` '.format(doc.type, doc.name)
    if doc.parent:
        report_string += '(from `{}`) '.format(doc.parent)
    report_string += 'has been automagically updated by Docstrung.\n\n'

    top_package = doc.fullname.split('.')[0] 
    rel_path = doc.file[doc.file.find(top_package) + len(top_package) + 1:]
    link = 'https://github.com/Neurosim-lab/' + top_package + '/blob/docstrung/' + rel_path  

    report_string += 'It is located in the following location on GitHub:\n'
    report_string += link
    report_string += '\n\n'

    report_string += 'You can edit the docstring directly in your browser and commit.\n\n'

    report_string += 'Please ensure the new docstring is correct and '
    report_string += 'completely filled in.  Be sure to replace or '
    report_string += 'delete ``<carats>`` and their contents.\n\n'

    report_string += 'If the docstring is for a function, and if the '
    report_string += 'function returns something, be sure to add a '
    report_string += 'returns section to the end of the docstring:\n\n'

    report_string += '    Returns\n'
    report_string += '    =======\n'
    report_string += '    ``<return type>``\n'
    report_string += '        <description of return>\n\n'

    report_string += 'The original docstring was as follows:\n'
    report_string += '```'
    report_string += str(doc.original_docstring)
    report_string += '```'
    report_string += '\n\n'

    report_string += 'The new docstring is as follows:\n'
    report_string += '```'
    report_string += doc.docstring
    report_string += '```'
    report_string += '\n\n'

    return report_string



def save_report(docstring_object):
    pass



def submit_report(docstring_object, repo_owner=None, repo_name=None, repo_branch=None, user_name=None, token=None, labels=None, options=options):

    report_string = docstring_object.report
    
    if repo_owner is None:
        repo_owner = options.github_username
    if repo_name is None:
        repo_name = docstring_object.fullname.split('.')[0]
    if repo_branch is None:
        repo_branch = options.github_branch
    if user_name is None:
        user_name = options.github_username
    if token is None:
        token = get.get_github_token(options.github_token)
    if labels is None:
        labels = ['docstrung']
    
    title  = report_string.splitlines()[0]
    body   = report_string

    url = 'https://api.github.com/repos/%s/%s/issues' % (repo_owner, repo_name)
    session = requests.Session()
    session.auth = (user_name, token)
    issue = {'title': title, 'body': body, 'labels': labels}
    response = session.post(url, json.dumps(issue))
    if not response.status_code == 201:
        print ('Could not create GitHub issue: {0:s}'.format(title))
        print ('Response:', response.content)
