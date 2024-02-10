from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)

empnvDB=[
 {
 'id':'561',
 'name':'Aman',
 'age' : 23,
 'department':'SDE'
 },
 {
 'id':'159',
 'name':'Emma',
 'age' : 23,
 'department':'ML'
 },
 {
 'id':'341',
 'name':'Winter',
 'age' : 42,
 'department':'SDE'
 },
 {
 'id':'101',
 'name':'Siraj',
 'age' : 32,
 'department':'AI'
 },
 {
 'id':'201',
 'name':'Raj',
 'age' : 52,
 'department':'HR'
 }
 ]

@app.route('/empnvDB/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empnvDB})

@app.route('/empnvDB/employee/<empId>', methods=['GET'])
def get_emp(empId):
    usr = [emp for emp in empnvDB if emp['id'] == empId]
    return jsonify({'emp': usr})

@app.route('/empnvDB/employee/<empId>', methods=['PUT'])
def update_emp(empId):
    em = [emp for emp in empnvDB if emp['id'] == empId]

    if len(em) == 0:
        return jsonify({'error': 'Employee not found'}), 404

    if 'name' in request.json:
        em[0]['name'] = request.json['name']

    if 'department' in request.json:
        em[0]['department'] = request.json['department']

    return jsonify({'emp': em[0]})
 

@app.route('/empnvDB/employee', methods=['POST'])
def create_emp():
    data = {
        'id': request.json['id'],
        'name': request.json['name'],
        'department': request.json['department']
    }
    empnvDB.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)