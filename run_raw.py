from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)


@app.route('/create_tag', methods=["POST"])
def create_tag():
    body = request.json
    product_code = body.get('product_code')

    tag = Code128(product_code, writer=ImageWriter())
    tag_path = f'{tag}'
    tag.save(tag_path)

    return jsonify({"tag_path": tag_path})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
