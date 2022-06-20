from deepface import DeepFace

df = DeepFace.find(img_path = "people/stallone.jpg",db_path= "my_db/", enforce_detection="true")
print ("Resultado ")
print (df)