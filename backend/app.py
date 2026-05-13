from flask import Flask, request, jsonify

app = Flask(__name__)

patients =[
    {"id":1,"name":"ali hassan","condition":"flu"},
    {"id":2,"name":"sara khan","condition":"diabetes"}
]
next_id=3

@app.route('/api/health',methods=['GET'])
def health():
    return jsonify({"status":"ok"}),200

@app.route('/api/patients',methods=['GET'])
def get_patients():
    return jsonify(patients),200

@app.route('/api/patients/<int:sid>',methods=['GET'])
def get_a_patient(sid):
    for p in patients:
        if p["id"]==sid:
            return jsonify(p),200
    return jsonify({"error":"patient not found"}),404

@app.route('/api/patients',methods=['POST'])
def post_patient():
    global next_id
    data = request.get_json()
    if not data or "name" not in data or "condition" not in data:
        return jsonify({"error":"provide full info"}),400
    newpatient = {
        "id":next_id,
        "name":data["name"],
        "condition":data["condition"]
    }

    patients.append(newpatient)
    next_id +=1
    return jsonify(newpatient),201


@app.route('/api/patients/<int:sid>',methods=['PUT'])
def update_patient(sid):
    data = request.get_json()
    p = [p for p in patients if p["id"]==sid]
    if p:
        p["name"] = data.get("name",p["name"])
        p["condition"] = data.get("condition",p["condition"])
        return jsonify(p),200
    return jsonify({"error":"patient not found"}),403


@app.route('/api/patients/<int:sid>',methods=['DELETE'])
def delete_patient(sid):
    global patients
    origlen  = len(patients)
    patients = [p for p in patients if p["id"]!=sid]
    if origlen==len(patients):
        return jsonify({"error":"patient not found"}),404
    return jsonify({"status":"successfully delted"}),200

if __name__=="__main__":
    app.run(debug=True,port=5000,host='0.0.0.0')




