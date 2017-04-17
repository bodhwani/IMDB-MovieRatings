# IMDb Movie Information

A python script that looks up all movies in a folder on IMDb and gets the ratings, genre and plot of the movie and stores it in an excel sheet.
I wrote this to be able to decide which movie I wanted to watch from all the movies I had on my disk.

###Demo<br>
![alt text](/DEMO.png "Demo of Excel file")


###Installation<br>
    git clone https://github.com/bodhwani/IMDB-MovieRatings.git<br>
    cd IMDB-MovieRatings<br>
    python imdbFinal.py<br>
After running this script, excel file will be generated in the same folder in which this script is present.<br>

###Requirements<br>
- urllib - pip install urllib2<br>
- json - pip install simplejson<br>
- pandas - pip install pandas<br>
- requests - pip install request<br>
- xlsxwriter - sudo pip install xlsxwriter<br>

###Conditions<br>
Your movies in the folder must contain names that can be found in IMDB. For eg. It cannot be like The Double(2013)[YTS], The Double1080.pxBR etc.The Double(2013) will work fine.


	
