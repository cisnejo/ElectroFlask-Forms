from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

def getCredentials(SCOPES,DISCOVERY_DOC):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)
    return service


def testing():
    SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
    service = getCredentials(SCOPES,DISCOVERY_DOC)
    # Prints the responses of your specified form:
    form_id = '14oTx7VoIwe9NP3msdkdDNpAq8F6QH1cCJNPBPpsO7J8'
    result = service.forms().responses().list(formId=form_id).execute()
    print(result)
    return result

#testing()
