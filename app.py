from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup the database
DATABASE_URL = 'sqlite:///crud_app.db'  # Use SQLite for simplicity

app = Flask(__name__)

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Model for the database
class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Create tables
Base.metadata.create_all(engine)

@app.route('/')
def index():
    entries = session.query(Entry).all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    email = request.form['email']
    
    new_entry = Entry(name=name, email=email)
    session.add(new_entry)
    session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['GET'])
def delete_entry(id):
    entry = session.query(Entry).get(id)
    session.delete(entry)
    session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
