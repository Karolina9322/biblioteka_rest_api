from flask import Flask, jsonify, abort, make_response, request
from modelsapi import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/books/", methods=["GET"])
def books_list_api_v1():
    return jsonify(books.all())

@app.route("/api/v1/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book": book})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.route("/api/v1/books/", methods=["POST"])
def create_book():
    if not request.json or not "book_title" in request.json:
        abort(400)
    book = {
        "book_title": request.json["book_title"],
        "book_author": request.json["book_author"],
        "book_year": request.json["book_year"],
        "book_publishing_house": request.json["book_publishing_house"],
        "book_number_of_pages": request.json["book_number_of_pages"],
        "book_category": request.json["book_category"],
        "book_description": request.json.get("book_description", ""),
        "book_id": books.all()[-1]["book_id"] + 1
    }
    books.create(book)
    return jsonify({'book':book}), 201

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

@app.route("/api/v1/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    result = books.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route("/api/v1/books/<int:book_id>", methods=["PATCH"])
def update_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        "book_title" in data and not isinstance(data.get("book_title"), str),
        "book_author" in data and not isinstance(data.get("book_author"), str),
        "book_year" in data and not isinstance(data.get("book_year"), int),
        "book_publishing_house" in data and not isinstance(data.get("book_publishing_house"), str),
        "book_number_of_pages" in data and not isinstance(data.get("book_number_of_pages"), int),
        "book_category" in data and not isinstance(data.get("book_category"), list),
        "book_description" in data and not isinstance(data.get("book_description", ""),str),
        "book_id" in data and not isinstance(data.get("book_id"), int)
    ]):
        abort(400)
    book = {
        "book_title": data.get("book_title", book["book_title"]),
        "book_author": data.get("book_author", book["book_author"]),
        "book_year": data.get("book_year", book["book_year"]),
        "book_publishing_house": data.get("book_publishing_house", book["book_publishing_house"]),
        "book_number_of_pages": data.get("book_number_of_pages", book["book_number_of_pages"]),
        "book_category": data.get("book_category", book["book_category"]),
        "book_description": data.get("book_description", book["book_description"]),
        "book_id": data.get("book_id", book["book_id"])
    }
    books.update(book_id, book)
    return jsonify({'book': book})

if __name__ == "__main__":
    app.run(debug=True)