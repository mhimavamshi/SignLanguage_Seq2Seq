from flask import Flask
import tensorflow as tf
reloaded = tf.saved_model.load('./Translator/translator')
_ = reloaded.translate(tf.constant(["how are you"]))
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello World"
@app.route('/<english>')
def translate(english,model=reloaded):
    pred=model.translate([english.lower()])[0].numpy().decode()
    return {"english":english,"predict":pred}
if __name__=='__main__':
    app.run(debug=True)