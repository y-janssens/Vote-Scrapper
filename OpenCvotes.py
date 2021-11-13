from bs4 import BeautifulSoup
import requests
import cv2 as cv
import numpy as np

img = np.zeros((140, 500, 3), dtype='uint8')
img[:] = (227, 231, 232)


def get_url():
    #url_input = text_input.get()
    html_text = requests.get(
        'https://marbrume.forumactif.com/t6212-votes-de-novembre-2021').text
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


while True:
    cv.imshow("Votes Scrapper", img)
    cv.createTrackbar( 'thresh', 'ctrl', 128, 255 )

    k = cv.waitKey(1)
    if k == 27:  # Esc key to breakloop and shutdown
        break

cv.destroyAllWindows()
