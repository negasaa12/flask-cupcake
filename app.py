from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.app_context().push()

connect_db(app)


# *****************************
# RESTFUL TODOS JSON API
# *****************************

@app.route('/api/cupcakes')
def all_cupcakes():

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    print(f'CUPCAKEEEEEEEEEE {all_cupcakes}')
    return jsonify(all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):

    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():

    new_cupcake = Cupcake(
        flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'])

    db.session.add(new_cupcake)
    db.session.commit()
    responst_json = jsonify(cupcake=new_cupcake.serialize())
    return (responst_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def upadate_cupcake(id):
    """Updates a particular todo and responds w/ JSON of that updated todo"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def delete_cupcake(id):
    """Updates a particular todo and responds w/ JSON of that updated todo"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='CAKE DELETED')
