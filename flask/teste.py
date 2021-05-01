import datetime
from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL
from dao import ProductDao
from models import Product, Barcode, Attribute

app = Flask(__name__)
app.secret_key = 'password'
app.config['MYSQL_HOST'] = "0.0.0.0"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "nodis_devops_test"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

product_dao = ProductDao(db)


@app.route('/criar')
def criar():
    produto = Product('Caneca', '8sDcvaadwd', 'verrde', 3.90, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                      datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    print(produto.last_updated)
    product_dao.save(produto)
    return render_template('new_product.html')
    # return redirect(url_for(''))


app.run(debug=True)
