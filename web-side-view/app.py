import get_responce as gr
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)
qnas=[]

@app.route('/',methods=["post",'get'])
def index():
    
    

    return render_template('index.html')

@app.route('/chat',methods=["post",'get'])
def chat():
    
    question=""
    responce=''
    if request.method=='POST':
        question=request.form.get('question')
        responce=gr.get_chatbot_response(question)
        qnas.append([question,responce])
    return render_template('index.html',qnas=qnas)


if __name__ == '__main__':


    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)