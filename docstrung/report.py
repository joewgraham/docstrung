import os
import json
import requests

USERNAME = 'joewgraham'
PASSWORD = ''

REPO_OWNER = 'joewgraham'
REPO_NAME = 'netpyne'



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



def submit_report(docstring_object):
    
    report_string = docstring_object.report
    
    title  = report_string.splitlines()[0]
    body   = report_string
    labels = ['docstrung']

    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    issue = {'title': title,
             'body': body,
             'labels': labels}
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue {0:s}'.format(title))
    else:
        print ('Could not create Issue {0:s}'.format(title))
        print ('Response:', r.content)
