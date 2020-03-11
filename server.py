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
    stripped_payload = strip_meta(payload)
    yaml_payload = "```\n"+yaml.dump(stripped_payload)+"```"
    print(yaml_payload)
    label=request.headers.get('label')
    if label == "iniziativa":
        if "natura" in list(payload):
            if payload["natura"] == "culturale-ricr":
                label = "Attivita culturali e ricreative"
            elif payload["natura"] == "solidale":
                label = "Servizi e iniziative solidali "
                if "Tipo_di_soggetto" in list(payload):
                    if payload["Tipo_di_soggetto"] == "privato":
                        label += "private"
                    else:
                        label += "pubbliche"
                
            elif payload["natura"] == "didattica":
                label = "Didattica a distanza e-learning"
            elif payload["natura"] == "sostegno-lavor":
                label = "Sostegno lavoro e imprese"
    if "titolo" in list(payload):
        issue_title=payload["titolo"][0:50]
    elif "cosa" in list(payload):
        issue_title=payload["cosa"][0:50]
    elif "testo" in list(payload):
        issue_title=payload["testo"][0:50]
    elif "descrizione" in list(payload):
        issue_title=payload["descrizione"][0:50]
    else:
        issue_title=label
    open_github_issue(title=issue_title, body=yaml_payload, labels=[label, "form"])
    return "OK", 200

def strip_meta(payload):
    excludelist = ["end", "start", "formhub/uuid", "meta/instanceID"]
    # Rimuovi tutti i campi meta che iniziano con _
    for k in list(payload):
        if k.startswith('_'):
            payload.pop(k)
        # Rimuovi anche le chiavi specificate nella lista
        elif k in excludelist:
            payload.pop(k)
    return payload

def open_github_issue(title, body=None, assignee=None, milestone=None, labels=[]):
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
