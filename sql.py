import sqlite3

with sqlite3.connect("blog_posts.db") as connection:

    c = connection.cursor()
    c.execute('DROP TABLE posts')
    c.execute('CREATE TABLE posts(title TEXT, description TEXT)')
    c.execute('INSERT INTO posts VALUES("Lorem Ispum", "Lorem Ipsum dolor sit amet."(')
    c.execute('INSERT INTO posts VALUES("Ice Cream", "I delicious.")')
    c.execute('INSERT INTO posts VALUES("pizza", "Mmmmm pizza.")')
    c.execute('INSERT INTO posts VALUES("Hello World", "My very first blog post!.")')

print("Created Database!")
