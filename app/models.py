from app import db

class Imagedata(db.Model):
    """
    Create an table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'imagedatas'
    id = db.Column(db.Integer, primary_key=True)
    startdate = db.Column('startdate', db.String(10), unique=True, nullable=True, primary_key=True)
    enddate = db.Column('enddate', db.String(10), unique=True, nullable=True)
    text = db.Column('text', db.String(255), unique=False, nullable=True)
    path = db.Column('path', db.String(255), unique=True, nullable=True)

    def __repr__(self):
    	return '<Imagedata: {}'.format(self.path)