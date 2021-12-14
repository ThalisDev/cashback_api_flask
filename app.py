import json
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from validate_docbr import CPF

app = Flask("calculate_cashback")

#   initialize firebase
cred = credentials.Certificate('ServiceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/calculate", methods=['POST'])
def calculate_cashback():
    # request from a json
    body = request.get_json()
    global val1
    val1 = True
    global val2
    val2 = True
    # date of purchase
    date = body['sold_at']
    # document of the client
    document = body['document']
    # validate CPF
    cpf = CPF()
    cpf_validate = cpf.validate(document)

    if cpf_validate is False:
        return "The CPF is Invalid"
        val1 = False

    # value of product
    value = body['value']
    # name of the client
    name = body['name']
    # quantity of items
    qty = body['qty']
    # request the type of cashback
    type_cashback = body['type_cashback']
    # request the total of buy
    total = body['total']
    # validate total
    float(qty)
    float(value)
    sumtotal = value * qty

    if total != sumtotal:
        return "The sum is incorrect"
        val2 = False

    # comparing the types of cashbacks
    if type_cashback == 'A':
        cashback = total * 0.05

    if type_cashback == 'B':
        cashback = total * 0.2

    # insert the data in firestore database
    if val1 and val2 is True:
        data = {
            u'cpf': document,
            u'date': date,
            u'name': name,
            u'qty': qty,
            u'total': sumtotal,
            u'type_cashback': type_cashback,
            u'value': value
        }
        db.collection(u'cashback').add(data)

    return jsonify({"cashback": cashback,
                    "sold_at": date,
                    "document": document,
                    "name": name,
                    "total": total,
                    "products": [{
                        "qty": qty,
                        "value": value,
                        "type": type_cashback
                    }],
                    })


if __name__ == '__main__':
    app.run()
