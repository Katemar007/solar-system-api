from flask import abort, make_response, Response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = {"message": f"{cls.__name__} {model_id} invalid"}
        abort(make_response(response, 400))
    
    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"message": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404))

    return model

def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
        
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201

# work in progress
def delete_model(cls, model_id):
    model = db.session.scalar(db.select(cls).where(cls.id == model_id))    
    
    db.session.delete(model)
    db.session.commit()

    return Response(status=204, mimetype ="application/json")
