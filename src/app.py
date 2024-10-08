import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootpassword@db/TestBoris'
db = SQLAlchemy(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Amin",
        "lastname": "Espinoza",
        "socialMedia":
        [
            {"facebookUser": "boris"},
            {"instagramUser": "aminespinoza10"},
            {"xUser": "aminespinoza"},
            {"linkedin": "amin-espinoza"},
            {"githubUser": "aminespinoza10"}
        ],
        "blog": "https://aminespinoza.com",
        "author": "Miranda Espinoza"
    }
    return json.dumps(value)

@app.route('/users', methods=['GET'])
def test_db_connection():
    try:
        result = db.session.execute(text('SELECT * FROM users'))
        columns = result.keys()

        users = result.fetchall()

        user_list = [dict(zip(columns, row)) for row in users]

        for user in user_list:
            print(user)

        return {"data": user_list}, 200
    except Exception as e:
        return f"Error al conectar a la base de datos: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)