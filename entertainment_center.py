import fresh_tomatoes
import media
#creating a array of instances
matrix = media.Movie("Matrix","http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle","https://www.youtube.com/watch?v=vKQi3bBA1y8")
avengers = media.Movie("Avengers","http://t1.gstatic.com/images?q=tbn:ANd9GcTp0qlAoWcOOswIkL_qpjYzJqCCDmWXiBzCXiqbE43Obo8c0Z-s",
                      "https://www.youtube.com/watch?v=eOrNdBpGMv8")
thor= media.Movie("Thor","http://t3.gstatic.com/images?q=tbn:ANd9GcST1uigGrukMvSAVUefFNuQ0NMZAR-FjfFIwSZFCR5ZkyMSgCyj","https://www.youtube.com/watch?v=ue80QwXMRHg")
captain_america = media.Movie("Captain America","http://t3.gstatic.com/images?q=tbn:ANd9GcTz1xU3qYlGXViIS51HIQh71D339ceW2nlWnb8zzSaJAL0newVj","https://www.youtube.com/watch?v=dKrVegVI0Us")
black_panther = media.Movie("Black Panther","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUdXmIWoiA0IusdOs5lRUatudjsOKnS0-wo4gPFakvRJNVcRVZuPsDMg","https://www.youtube.com/watch?v=xjDjIWPwcPU")
martian = media.Movie("Martian","http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ","https://www.youtube.com/watch?v=ej3ioOneTy8")
baahubali = media.Movie("Baahubali","https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg","https://www.youtube.com/watch?v=VdafjyFK3ko")
baahubali2 = media.Movie("Baahubali 2","https://images-na.ssl-images-amazon.com/images/I/711eHgGtnFL._SX385_.jpg","https://www.youtube.com/watch?v=G62HrubdD6o")
#storing array of movies into list
movies = [matrix,avengers,thor,captain_america,black_panther,martian,baahubali,baahubali2]

#function call to load the website
fresh_tomatoes.open_movies_page(movies)
