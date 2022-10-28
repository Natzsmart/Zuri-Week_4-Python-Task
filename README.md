We would be building a simple song CRUD application. 
In our models.py file inside the “musicapp” application we created, you are expected to add the following Models and Attributes.

Model: Artiste, Song, Lyric
Attributes for “Artiste” : first_name, last_name, age
Attributes for “Song” : title, date released, likes, artiste_id
Attributes for “Lyric”: content, song_id
 

As you might have guessed, there is a relationship between all three Models. An Artiste can have multiple songs, and a song can have multiple lyrics.A song must only belong to one Artiste and a lyric must only belong to a song. You are to specify the foreignkey relationship yourself.

Also, the model field attributes should be specified by you. 
