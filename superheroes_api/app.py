from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

app = Flask(__name__)

# databaase configiration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initializing extesions
db.init_app(app)
migrate = Migrate(app, db)

# routes
@app.route('/')
def home():
    return '<h1>Superheroes API!</h1>'

# GET heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

# GET heros by id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if hero:
        hero_dict = hero.to_dict()
        hero_dict['hero_powers'] = [hp.to_dict() for hp in hero.hero_powers]
        return jsonify(hero_dict)
    else:
        return jsonify({"error": "Hero not found"}), 404
    
#GET powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

# GET powers by id
@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    else:
        return jsonify({"error": "Power not found"}), 404
    
#PATCH powers 
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.get_json()
    if 'description' in data:
        try:
            power.description = data['description']
            db.session.commit()
            return jsonify(power.to_dict())
        except ValueError as e:
            return jsonify({"errors": [str(e)]}), 400
    else:
        return jsonify({"errors": ["Invalid data"]}), 400
    

#POST hero_powers
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    if not strength or not hero_id or not power_id:
        return jsonify({"errors": ["Missing required fields"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)
    
    if not hero or not power:
        return jsonify({"errors": ["Hero or Power not found"]}), 404

    try:
        hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
        db.session.add(hero_power)
        db.session.commit()
        return jsonify(hero_power.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except IntegrityError:
        return jsonify({"errors": ["HeroPower creation failed"]}), 400



