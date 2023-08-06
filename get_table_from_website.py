import pandas as pd

def get_table_from_website():
    simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
    print(len(simpsons))
    print(simpsons[1])

get_table_from_website()