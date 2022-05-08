from cgitb import text
from webbrowser import get
from flask import Flask, jsonify
import json
from db import *
from bson.son import SON


app = Flask(__name__)


list_results = []
list_coord_res = []

'''
pymongo metodlarının düzgün işlədmədəyini düşünürəm
'''

@app.route('/<searc_input>')
def db_index(searc_input):
    for item in adress_table.aggregate([
                        {'$match':{'$text': {'$search':searc_input,'$diacriticSensitive': False}}}
                    ]):
        list_results.append(item)
    return 'end'


@app.route('/loc/<lati>/<long>')
def find(lati, long):
    print(lati, long)
    for doc in adress_table.find({
        'location': SON([('$nearSphere', [lati, long]), ("$maxDistance", 1000)])
    }):
        list_coord_res.append(doc)
    print(list_coord_res)
    return 'end'



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') 