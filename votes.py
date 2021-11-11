from bs4 import BeautifulSoup
import requests
import tkinter as tk

root = tk.Tk()
root.title("Votes Scrapper")
root.geometry("500x140")
root.configure(background='#E8E7E3')

title = tk.Label(root, text='Comptabilisateur de votes', font=(
    "Courier New", 15), bg="#E8E7E3", fg="black")
title.pack(pady=7.5)

text_input = tk.Entry(root, font=(
    "Courier New", 8), relief="flat")
text_input.insert(0, 'Url du sujet de votes')
text_input.place(x=12.5, y=45, width=475, height=40)


def get_url():
    url_input = text_input.get()
    html_text = requests.get(
        url_input).text
    soup = BeautifulSoup(html_text, 'lxml')
    users_list = list(soup.find_all('span', class_='pseudal'))

    result_list = []
    voters_list = []
    with open('votes.txt', 'w', encoding='utf-8') as f:
        f.write('Votes du mois: \n\n')
        print('Votes du mois: \n')
    for users in users_list:
        user_name = users.text
        result_list.append(user_name)

    for i in result_list:
        count = result_list.count(i)
        voters_list.append(f'{i} : {count}')

    voters_list = list(dict.fromkeys(voters_list))
    voters_list.sort()

    with open('votes.txt', 'a', encoding='utf-8') as f:
        for votes in voters_list:
            f.write(votes)
            f.write('\n')
            print(votes)


valid = tk.Button(root, text="Enregistrer", command=get_url, relief="flat", font=(
    "Courier New", 8), bg="#6cb46c", fg="white", activebackground="#6cb46c", activeforeground="white")
valid.place(x=200, y=95, width=100, height=35)

root.mainloop()
