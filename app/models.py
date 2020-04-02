from app import db
from app import ma
class Imagedata(db.Model):
    """
    Create an table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'db_concernee'
    id = db.Column('pk', db.Integer, primary_key=True, autoincrement=True)
    startdate = db.Column('startdate', db.String(10), unique=True, nullable=True, primary_key=True)
    enddate = db.Column('enddate', db.String(10), unique=True, nullable=True)
    text = db.Column('text', db.String(255), unique=False, nullable=True)
    path = db.Column('path', db.String(255), unique=True, nullable=True)

    def __repr__(self):
    	return '<Imagedata: {}'.format(self.path)

class Imagedataschema(object):
    class meta:
        fields = ('startdate', 'enddate', 'text')
            
        