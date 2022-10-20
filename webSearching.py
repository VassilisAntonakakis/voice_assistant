import webbrowser

def internetSearch(searchTerm):
    url="https://www.google.com/search?q=" + searchTerm
    webbrowser.open_new_tab(url)