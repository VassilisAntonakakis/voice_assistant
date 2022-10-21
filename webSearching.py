import webbrowser

def internetSearch(searchTerm):
    url="https://www.google.com/search?q=" + searchTerm
    webbrowser.open_new_tab(url)

def dictSearch(searchTerm):
    url="https://www.google.com/search?q=" + "define:" + searchTerm
    webbrowser.open_new_tab(url)

def exactSearch(searchTerm):
    url = "https://www.google.com/search?q=" + '"' + searchTerm + '"'
    print(url)
    webbrowser.open_new_tab(url)

internetSearch("music -movie")