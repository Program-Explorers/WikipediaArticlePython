import requests
import bs4

while True:
    user_choice = input("\nWhat wikipedia article would you like: ")
    user_choice = user_choice.lower()
    base_url = 'https://en.wikipedia.org/wiki/{}'

    result = requests.get(base_url.format(user_choice))
    html_data = bs4.BeautifulSoup(result.text, "lxml")

    text = html_data.select('.mbox-text > b')

    if len(text) == 0 or user_choice.title() == text[0].getText():
        print('\nHere is your wikipedia article on', user_choice, ' ', base_url.format(user_choice))
        break

    elif 'Wikipedia does not have an article with this exact name.' in text[0].getText():
        print('\n')
        print(text[0].getText())
        print("Sorry that is not a valid wikipedia artile\n")
        continue

    else:
        print('Error')

exit(0)
