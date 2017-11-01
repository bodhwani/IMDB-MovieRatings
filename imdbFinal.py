import urllib
from urllib2 import Request, urlopen, URLError
import json
import pandas as pd
import os
import requests
from lxml import html
import sys
import xlsxwriter


array = []
name_movie= []
rating_movie = []

genre_movie =  []

plot_movie = []
final = [[1,2,3,4]]




movie_names = []
genre = []
plot = []
ratings = []





def get_imdb_id(input):
    query = urllib.quote_plus(input)
    url = "http://www.imdb.com/find?ref_=nv_sr_fn&q="+query+"&s=all"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    if"No results" in (tree.xpath('//h1[@class="findHeader"]/text()')[0]):
        imdb_id = "tt00000"
    else:
        imdb_id=(tree.xpath('//td[@class="result_text"]//a')[0].get('href'))
        imdb_id = imdb_id.replace('/title/','')
        imdb_id = imdb_id.replace('/?ref_=fn_al_tt_1','')
    return (imdb_id)

def get_info(id):

    data = json.loads(urlopen(Request("http://theapache64.xyz:8080/movie_db/search?keyword={0}".format(id))).read())
    
    if data['error_code'] == 1:
        message = "No results found"
        genre.append(message)
        plot.append(message)
        ratings.append(message)

    else:
        genre.append(data['data']['genre'])
        plot.append(data['data']['plot'])
        ratings.append(data['data']['rating'])

def main():
    filepath = raw_input("Enter path")
    print("Processing...")
    for file in os.listdir(filepath):
        get_info(get_imdb_id(file))
        movie_names.append(file)


    array.append(movie_names)
    array.append(ratings)
    array.append(genre)
    array.append(plot)




    for i in range(len(array[0])):
        newarray = []
        newarray.append(array[0][i])
        newarray.append(array[1][i])
        newarray.append(array[2][i])
        newarray.append(array[3][i])
        final.append(newarray)


    workbook = xlsxwriter.Workbook('membersFinal.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(0,len(final)):
        worksheet.write('A'+str(i), final[i][0])
        worksheet.write('B'+str(i), final[i][1])
        worksheet.write('C'+str(i), str(final[i][2]))
        worksheet.write('D'+str(i), str(final[i][3]))


    workbook.close()
    print("Successfully Created Excel file in the same directory in which your python script is present")

if __name__ == "__main__":
    main()
