from flask import Flask, request, jsonify, redirect, url_for, render_template, flash
from deep_translator import GoogleTranslator
import os, cv2
from werkzeug.utils import secure_filename
from database import database_connection

app = Flask(__name__)


@app.route('/testing', methods = ['POST'])
def api_practice():
    data = request.json['input_text']
    print(data)
    translated = GoogleTranslator(source='auto', target= 'hi').translate(data)
    c, mydb = database_connection()
    c.execute("INSERT INTO text_input (input_text, translated_text) values (%s, %s)", (data, translated))
    c.execute("select * from text_input;")
    mydb.commit()
    row = c.fetchall()
    print(row)
    c.close()
    mydb.close()
    return jsonify({'output' : translated})
    
if __name__ == '__main__':
    app.run(debug=True)