from bs4 import BeautifulSoup
import requests
import tkinter as tk
import time

root_url = 'https://marbrume.forumactif.com'
topics_index = requests.get(
    'https://marbrume.forumactif.com/f66-aider-le-forum').text
soup_index = BeautifulSoup(topics_index, 'lxml')
lasts_topics = soup_index.find_all('a', class_='topictitle')
last_topic_list = []

for i in lasts_topics:
    topic = i['href']
    last_topic_list.append(topic)

last_topic = root_url + last_topic_list[1]
print(f'''
Les derniers sujets créés sont:
{root_url + last_topic_list[1]}
{root_url + last_topic_list[2]}
{root_url + last_topic_list[3]}
''')

root = tk.Tk()
root.title("Votes Scrapper")
root.geometry("500x140")
root.configure(background='#E8E7E3')

title = tk.Label(root, text='Comptabilisateur de votes', font=(
    "Courier New", 15), bg="#E8E7E3", fg="black")
title.pack(pady=7.5)


text_input = tk.Entry(root, font=(
    "Courier New", 8), relief="flat")
text_input.insert(
    0, last_topic)
text_input.place(x=12.5, y=45, width=475, height=40)


def get_url():
    start = time.time()
    print('Votes du mois: \n')
    result_list = []
    counter = 0
    url = text_input.get()
    root = url[:32]
    topic = url[32:37]
    name = url[37:]

    for i in range(0, 1125, 15):
        counter = i

        if counter == 0:
            pagination = ''
        else:
            pagination = f'p{counter}'

        page = root + topic + pagination + name
        html_text = requests.get(page).text
        soup = BeautifulSoup(html_text, 'lxml')
        users_list = list(soup.find_all('span', class_='pseudal'))

        voters_list = []
        final_votes = []

        with open('votes.txt', 'w', encoding='utf-8') as f:
            f.write('Votes du mois:\n\n')

        for users in users_list:
            user_name = users.text
            result_list.append(user_name)

        for i in result_list:
            count = result_list.count(i)
            voters_list.append(f'{i} : {count}')

        voters_list = list(dict.fromkeys(voters_list))
        voters_list.sort()

        for votes in voters_list:
            final_votes.append(votes)

    with open('votes.txt', 'a', encoding='utf-8') as f:
        for z in final_votes:
            f.write(z)
            f.write('\n')
            print(z)
    end = time.time()
    total = str(end - start).replace('.', ',')[0:5]
    print(f'\nResults saved, time elapsed: {total}s')


valid = tk.Button(root, text="Enregistrer", command=get_url, relief="flat", font=(
    "Courier New", 8), bg="#6cb46c", fg="white", activebackground="#6cb46c", activeforeground="white")
valid.place(x=200, y=95, width=100, height=35)

root.mainloop()
