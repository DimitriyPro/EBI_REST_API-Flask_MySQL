from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('mysql+pymysql://anonymous:@ensembldb.ensembl.org:3306/ensembl_website_97', echo=True)
app = Flask(__name__)
api = Api(app)


class GeneSuggest(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        species = request.args.get('species', default='homo_sapiens', type=str)
        label = request.args.get('label', default='BRC%%', type=str)
        limit = request.args.get('limit', default='2', type=str)
        query = "SELECT * from gene_autocomplete WHERE species = '{species}' and display_label LIKE '{label}' LIMIT {limit}".format(
            species=species, label=label, limit=limit)
        result = conn.execute(query)  # This line performs query and returns json result
        return {'search': [dict(zip(tuple(result.keys()), i)) for i in result.cursor]}  # Fetches column


api.add_resource(GeneSuggest, '/gene_suggest')  # Add route Gene_suggest

if __name__ == '__main__':
    app.run(port='5000')
