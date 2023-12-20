# setup and imports
from lxml import html
import pandas as pd
import requests
from bs4 import BeautifulSoup

# retrieving the data from the table in the url 
cabinets_url = 'https://en.wikipedia.org/wiki/List_of_cabinets_of_the_Netherlands' 
table_class = 'wikitable sortable jquery-tablesorter'
response = requests.get(cabinets_url)
soup = BeautifulSoup(response.text, 'html.parser')
indiatable = soup.find('table',{'class':'wikitable'})

# building the dataframe from the table 
cabinets_overview = pd.read_html(str(indiatable))
cabinets_overview = pd.DataFrame(cabinets_overview[0])
cabinets_overview = cabinets_overview.drop(['Prime Minister', 'Demissionary', 'Time in office',
                                            'Legislature Status', 'Type', 'Election', 'Orientation'], axis=1)

# cleaning and reformatiing the data
cabinets_overview = cabinets_overview.rename(columns = {'Term of office':'Term of office (Start)',
                                                        'Term of office.1':'Term of office (End)'})
cabinets_overview['Cabinet'] = cabinets_overview['Cabinet'].str.split('[')
cabinets_overview['Cabinet'] = cabinets_overview['Cabinet'].str[0]
cabinets_overview['Cabinet'] = cabinets_overview['Cabinet'].str[:-1]
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace("D'66","D66")
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('A A','A • A')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('A C','A • C')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('A D','A • D')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('D A','D • A')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('D D','D • D')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('F V','F • V')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('P A','P • A')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('P C','P • C')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('R D','R • D')
cabinets_overview['Parties'] = cabinets_overview['Parties'].str.replace('U D','U • D')
cabinets_overview['Political position'] = cabinets_overview['Political position'].str.split('[')
cabinets_overview['Political position'] = cabinets_overview['Political position'].str[0]

# filtering the dataframe
cabinets_1950 = cabinets_overview[29:58]

# export as .csv file
cabinets_1950.to_csv('Dutch_cabinets.csv', index=False)