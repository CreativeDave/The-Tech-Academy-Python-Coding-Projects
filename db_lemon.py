
"""
finds all file names with extension '.lemon' in a list, 
stores their names in an array, then prints to the console. It then 
creates a database with an identiry column and name column and
stores the names of the files.
""" 


import sqlite3


#iterates through list and stores '.lemons' then prints message 
def lifeGivesYouLemons():
    lemons = []
    lemonList = ('lemon.docx','lemonade.lemon','lemonYellow.png', \
            'lemonbasket.mpg','lemonySnicket.lemon','lemonLife.pdf', \
            'myPhoto.juicepg', 'Don.lemon')
    for lemon in lemonList:
         if lemon.endswith('.lemon'):
             lemons.append(lemon)
    print('lemon files:\n')
    print(*lemons, sep = ",\n")
    makeLemonade(lemons)

#creates the lemon database and stores the file names
def makeLemonade(lemons):
    conn = sqlite3.connect("db_lemon.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_lemonade( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_name TEXT)")
        for i in lemons:
            cur.execute("INSERT INTO tbl_lemonade (col_name) VALUES (?)",
                        (i,))
            conn.commit()
    conn.close()
    

if __name__ == "__main__":
    lifeGivesYouLemons()
