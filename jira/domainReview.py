import requests
import json

jiraURL = "https://<your-instance-url>/rest/migration/latest/email/domain-rules"

#Generate this from Database (PSQL)
# 
#select right(cwd_user.email_address, strpos(reverse(cwd_user.email_address), '@') - 1)
#        from cwd_user
#                 inner join cwd_directory cd on cd.id = cwd_user.directory_id
#        where cd.active = 1
#group by 1;

domainFile = "C:\\99-temp\\jiraDomainReview.txt"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer <Jira PAT>"
}

with open(domainFile, mode="r") as lists:
    for line in lists:
        trustDomain = {"domainName": line.replace('\n',''), "rule": "TRUSTED"}
        response = requests.put(jiraURL, json=trustDomain,headers=headers)
        print(trustDomain)
        print(response)
