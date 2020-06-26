import os
import json
import requests

from . import get
from . import options



def create_report(docstring_object):
    
    doc = docstring_object
    
    report_string = 'Check docstring for {}: {}'.format(doc.type, doc.fullname)
    report_string += '\n\n'

    report_string += 'The docstring for the Python {} {} '.format(doc.type, doc.name)  
    report_string += 'has been automagically updated by Docstrung.\n\n'
    report_string += 'It is located in the following file:\n{}\n\n'.format(doc.file)

    report_string += 'Please ensure the new docstring is correct and '
    report_string += 'completely filled in.\n\n'

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



def submit_report(docstring_object, repo_owner=None, repo_name=None, user_name=None, token=None, labels=None, options=options):

    report_string = docstring_object.report
    
    if repo_owner is None:
        repo_owner = options.github_username
    if repo_name is None:
        repo_name = docstring_object.fullname.split('.')[0]
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
