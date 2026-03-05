from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "cafe_DB"
app = Flask(__name__)


def connect_database(db_file):
    """
    creates a connection with the databse.
    :param db_file:
    :return:
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        print(f'An error occured when connecting to the database.')
    return


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu')
def render_menu():
    con = connect_database(DATABASE)
    query = "SELECT name, description, volume, image, price FROM products"
    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    print(product_list)
    con.close()
    return render_template('menu.html')


if __name__ == '__main__':
    app.run()
