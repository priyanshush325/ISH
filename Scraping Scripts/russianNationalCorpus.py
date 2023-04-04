from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

#Need to use Requests-HTML rather than BeautifulSoup because the page uses JavaScript to render content, which BeautifulSoup doesn't support

def urlGenerator(word):
    base = "https://ruscorpora.ru/en/explore?req="
    base += word
    return base

session = HTMLSession()
response = session.get(urlGenerator("hello"))
response.html.render()


#Appears to be working but Requests-HTML is bad so you have to go through each container div manually 

#Gets list of all divs with CSS class .container
containersList = response.html.find('.container', clean = True)
print(urlGenerator("hello"))

#Gets the last .container, which is the one that should be housing the graph
graphContainer = containersList[len(containersList) - 1]
print(graphContainer)

#Gets container div that holds all the widgets
widgetContainer = graphContainer.find('.widgets', clean = True)[0]
print(widgetContainerx )

#Gets last widget in the widget container, which should be the graph
#widgetList = widgetContainer.find('widget widget--full-size', clean = True)





