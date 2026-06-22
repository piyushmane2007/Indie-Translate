from translate import Translator
from flask import Flask,render_template,request

app = Flask(__name__)

def translation(from_lang,to_lang,text):
    translator = Translator(from_lang=from_lang, to_lang=to_lang) 
    return translator.translate(text)

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/translate", methods=["GET","POST"]) 
def translate():
    if request.method == "POST":
        source_lang=request.form.get("sourcelan") 
        target_lang=request.form.get("targetlan")
        text_to_tranlate=request.form.get("texttotranslate") 
        translated_text=translation(source_lang,target_lang,text_to_tranlate) 
        return render_template("home.html",translated_text=translated_text)


app.run(port=5000,debug=True)
