from flask import Flask, render_template, escape, abort, request
from ORM.models import *

app = Flask(__name__)
# it's bin
# descr=open('description.txt').readlines()
descr=['description of this wonderful book in progress']*6
name_pr=['C.P. Company 971-021','Louis Vuitton: Catwalk','Louis Vuitton: Celebrating Monogram','Hello, My Name Is Paul','A Denim Story: Inspirations From Bellbottoms To Boyfriends','Skira']
link_img=['CP Company.jpg','LouviusVuitton.jpg','Lv.jpg','PaulSmith.jpg','Rizzoli.jpg','Basquiat.jpg']
products=[]
for i in range(len(descr)):
    products.append(Product(name=name_pr[i], description=descr[i], img=link_img[i]))

products_three=products[:3]
@app.route('/')
def homepage():
    return render_template('HomePage.html', items = products_three)

@app.route('/About')
def about():
    return render_template('About.html')
#
@app.route('/Catalog')
def catalog():
    return render_template('Catalog.html',items = products)
#
@app.route('/Product/<item>')
def product(item):
    item=escape(item)
    for el in products:
        if el.name==item:
            return render_template('Product.html',item = el)
        # return abort(404)
if __name__=='__main__':
    app.run(debug=True)
