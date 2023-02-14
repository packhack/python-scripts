import requests
import json
import re
from bs4 import BeautifulSoup
 
jiraUrl="https://jira.com/rest/api/2/serverInfo"
ConfluenceUrl="https://confluence.com/login.action"

def get_json(url,header=False):
    # Make a GET request to the URL
    if header:
        response = requests.request('GET', url,headers=header)
    else:
        response = requests.request('GET',url)

    # Check if the request was successful
    if response.status_code == 200:
        content = response.text 
        return content
    
    return None

def stripe_url(url):
    match = re.search(r'https?://([^.]+)\.(.+\..+?)/', url)
    subdomain = match.group(1)
    domain = match.group(2)
    result = subdomain + "." + domain
    return result
   
def jiraVersion(url):
    resultUrl = stripe_url(url)
    content = get_json(url)
    version = json.loads(content)
    print(f"{resultUrl} - Version: " + version['version'])
    
def confluenceVersion(url):
    resultUrl = stripe_url(url)

    headers = {
        'Content-Type': 'text/html'
    }
    response = requests.get(url,headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    version = content.find('meta', {'name': 'ajs-version-number'})
    print(f"{resultUrl} - Version: " + version['content'])    

jiraVersion(jiraUrl)
confluenceVersion(confluenceUrl)
