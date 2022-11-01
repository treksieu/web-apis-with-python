import sqlite3 as SQL


def match_exact(word: str) -> list:
    

    # TODO: Establish connection to the dictionary database

    db = SQL.connect("data/dictionary.db")

    # TODO: Query the database for exact matches

    sql_query = "SELECT * from entries WHERE word=?"
    match = db.execute(sql_query, (word,)).fetchall()

    # TODO: Close the connection to the database

    db.close()
    

    # Return the results
    return match


def match_like(word: str) -> list:
    
    # TODO: Establish connection to the dictionary database
    db = SQL.connect("data/dictionary.db")
    # TODO: Query the database for exact matches
    sql_query = "SELECT * from entries WHERE word LIKE ?"
    match = db.execute(sql_query,("%"+word+"%",)).fetchall()
    # TODO: Close the connection to the database
    db.close()
    
    # Return the results
    return match
