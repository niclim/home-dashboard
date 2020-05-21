from . import routes


@routes.route("/example", methods=["GET"])
def example():
    return {"data": "hello"}, 200
