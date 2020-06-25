import os
import json
import requests

USERNAME = 'joewgraham'
PASSWORD = 'PASSWORD'

REPO_OWNER = 'joewgraham'
REPO_NAME = 'netpyne'

def create_report():
    pass

def save_report():
    pass

def submit_report(title, body=None, labels=None):

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
