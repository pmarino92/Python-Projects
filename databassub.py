import sqlite3

conn = sqlite3.connect('test2.db')# Creating new database called "test2"

with conn: # Creating table called list
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_list(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_name TEXT)") # Has two fields: Primary key and one column titled name
    conn.commit()

conn = sqlite3.connect('test2.db')

#Tuple of documents
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in tuple to find the files that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_list(col_name) VALUES(?)", (x,))
            print(x)
conn.close()
