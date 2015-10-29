from github import Github
from github3 import authorize

g = Github("mitrakatamreddy","Chandumitra1%")
for repo in g.get_user().get_repos():
    print repo.name
    #repo.edit(has_wiki=False)
user = 'mitrakatamreddy'
password = 'Abcdef1%'
note = 'github3'
note_url = 'http://example.com'
scopes = ['user', 'repo']
auth = authorize(user,password,scopes,note,note_url)
print auth.token


