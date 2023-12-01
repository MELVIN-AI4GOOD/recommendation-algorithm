from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": items})

# Route to get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        return jsonify({"item": item})
    else:
        return jsonify({"message": "Item not found"}), 404

# Route to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = {"id": len(items) + 1, "name": request.json.get('name')}
    items.append(new_item)
    return jsonify({"message": "Item added successfully", "item": new_item}), 201

if __name__ == '__main__':
    app.run(debug=True)
