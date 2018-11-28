from app import db


class FeatureRequest(db.Model):
    """This class represent feature_requests table"""
    __tablename__ = 'feature_requests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    priority = db.Column(db.Integer, nullable=False)
    product_area_id = db.Column(db.Integer, db.ForeignKey('product_areas.id'))
    target_date = db.Column(db.Date, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    client = db.relationship('Client', backref='feature_requests', lazy=True)
    product_area = db.relationship('ProductArea', backref='product_areas', lazy=True)

    def __init__(self, title, description, client_id, product_area_id, target_date, priority):
        self.title = title
        self.description = description
        self.client_id = client_id
        self.product_area_id = product_area_id
        self.target_date = target_date
        self.priority = priority

    def __repr__(self):
        return "<FeatureRequest: {}>".format(self.title)

class Client(db.Model):
    """This class represent the clients table """
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Client: {}>".format(self.name)

class ProductArea(db.Model):
    """This class represent the product_areas table """
    __tablename__ = 'product_areas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<ProductArea: {}>".format(self.name)

