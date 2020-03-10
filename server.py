from flask import Flask, request
import requests
import yaml, json

app = Flask(__name__)

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = ''
PASSWORD = ''

# The repository to add this issue to
REPO_OWNER = 'emergenzeHack'
REPO_NAME = 'covid19italia_segnalazioni'


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/report', methods=['POST'])
def process_report():
    payload = request.json
    yaml_payload = "```\n"+yaml.dump(payload)+"\n```"
    print(yaml_payload)
    issue_type=request.headers.get('type')
    open_github_issue(title=issue_type, body=yaml_payload)
    return "OK", 200

def open_github_issue(title, body=None, assignee=None, milestone=None, labels=["provaform"]):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'assignee': assignee,
             'milestone': milestone,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print('Successfully created Issue', title)
    else:
        print('Could not create Issue', title)
        print('Response:', r.content)


#make_github_issue('Test')
app.run(host='0.0.0.0');