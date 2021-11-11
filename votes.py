from bs4 import BeautifulSoup
import requests

""" login_url = 'https://marbrume.forumactif.com/login'
data = {
    'username': 'Séraphin Chantebrume',
    'password': 'imovane78'
}

with requests.Session() as s:
    response = requests.post(login_url , data)
    print(response.text)
    index_page= s.get('https://marbrume.forumactif.com/admin/?part=admin&tid=545387369f9ee73d670a3f637808e907&_tc=1636586602')
    soup = BeautifulSoup(index_page.text, 'html.parser')
    print(soup.title)  """

html_text = requests.get('https://marbrume.forumactif.com/t4988-vote-d-avril-2020-sujet-3').text
soup = BeautifulSoup(html_text, 'lxml')
users_list = list(soup.find_all('span', class_='pseudal'))

result_list = []
voters_list = []

print('Votes du mois: \n')
for users in users_list:
    user_name = users.text    
    result_list.append(user_name)

for i in result_list:
    count = result_list.count(i)
    voters_list.append(f'{i} : {count}')

voters_list = list(dict.fromkeys(voters_list))
voters_list.sort()

for votes in voters_list:
    print(votes)