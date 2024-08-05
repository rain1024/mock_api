from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for demonstration purposes
restaurants = [
    {
        "keywords": ["bún chả", "bun cha"],
        "restaurant_name": "Bun Cha Huong Lien",
        "opening": "9:00 AM - 9:00 PM",
        "menu": ["Bún chả", "Nem rán", "Bún nem"]
    },
    {
        "keywords": ["phở", "pho"],
        "restaurant_name": "Pho 10",
        "opening": "6:00 AM - 10:00 PM",
        "menu": ["Phở bò", "Phở gà", "Phở cuốn"]
    }
]

# Default restaurant information
default_restaurant = {
    "restaurant_name": "Quán Bún Chả Hà Nội",
    "opening": "7:00 AM - 10:00 PM",
    "menu": ["Bún chả", "Nem rán"]
}

@app.route('/search_restaurant', methods=['POST'])
def search_restaurant():
    data = request.get_json()
    dish_name = data.get("dish_name", "").lower()

    # Search for the restaurant based on dish name keywords
    for restaurant in restaurants:
        if any(keyword in dish_name for keyword in restaurant["keywords"]):
            return jsonify({
                "restaurant_name": restaurant["restaurant_name"],
                "opening": restaurant["opening"],
                "menu": restaurant["menu"]
            })

    # Return the default restaurant if no match is found
    return jsonify(default_restaurant), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')