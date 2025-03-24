from flask import Flask, render_template
from flask_restx import Api, Resource, fields
import psycopg2
import os

app = Flask(__name__)
api = Api(app, doc='/docs')

ns = api.namespace('alumnos', description='Operaciones con alumnos')

alumno_model = api.model('Alumno', {
    'nombre': fields.String(required=True, description='Nombre del alumno')
})

def get_db_connection():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )

@ns.route('/')
class AlumnoResource(Resource):
    def get(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS alumnos (id SERIAL PRIMARY KEY, nombre TEXT)")
        cur.execute("SELECT id, nombre FROM alumnos")
        alumnos = [{"id": row[0], "nombre": row[1]} for row in cur.fetchall()]
        cur.close()
        conn.close()
        return alumnos, 200

    @ns.expect(alumno_model)
    def post(self):
        data = api.payload
        nombre = data.get('nombre')
        if not nombre:
            api.abort(400, "El campo 'nombre' es obligatorio")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS alumnos (id SERIAL PRIMARY KEY, nombre TEXT)")
        cur.execute("INSERT INTO alumnos (nombre) VALUES (%s)", (nombre,))
        conn.commit()
        cur.close()
        conn.close()
        return {"mensaje": f"El alumno {nombre} fue agregado correctamente"}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
