from flask import Flask,render_template, request
import os
import numpy as np
import tensorflow as tf
from keras.models import load_model
import requests
global result

app = Flask(__name__,template_folder="templates")
model = load_model('C:/Users/Keerthiyogan/Desktop/IBM dummy/Flask/nutrition.h5')
print("Loaded model from disk")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/image',methods=['GET','POST'])
def image1():
    return render_template('imageprediction.html')

# @app.route('/predict',methods=['GET','POST'])
# def launch():
#     if request.method=='POST':
#         f = request.files['file']
#         basepath = os.path.dirname('__file__')
#         filepath = os.path.join(basepath,"uploads",f.filename)
#         f.save(filepath)
        
#         img = tf.keras.utils.load_img(filepath,target_size=(64,64))
#         x = tf.keras.utils.img_to_array(img)
#         x = np.expand_dims(x,axis=0)
        
#         pred = np.argmax(model.predict(x),axis=1)
#         print("prediction",pred)
#         index = ['APPLES','BANANA','ORANGE','PINEAPPLE','WATERMELON']
        
#         result = str(index[pred[0]])
        
#         x = result
#         print(x)
#         result = nutrition(result)
#         print(result) 
#         return render_template("0.html",showcase=(result),showcase1=(x))
#     return "abc"

@app.route('/predict', methods=['GET', 'POST'])# route to show the predictions in a web UI def launch():
def launch():
    if request.method == 'GET':
        f= request.files['file']#requesting the file
        basepath=os.path.dirname(__file__)#storing the file directory 
        filepath=os.path.join(basepath, "uploads", f.filename) #storing the file in uploads folder 
        f.save(filepath) #saving the file
        img=tf.keras.utils.load_img(filepath, target_size=(64, 64)) #load and reshaping the image
        x=tf.keras.utils.img_to_array(img)#converting image to an array 
        x=np.expand_dims (x, axis=0) #changing the dimensions of the image
        pred=np.argmax(model.predict(x), axis=1)
        print("prediction", pred) #printing the prediction 
        index=['APPLES', 'BANANA', 'ORANGE', 'PINEAPPLE', 'WATERMELON']
        result=str(index[pred[0]])
        x=result
        print(x)
        result=nutrition(result)
        print(result)
        return render_template("0.html", showcase=(result), showcase1=(x))
    return "abc"
        
def nutrition(index):
    import requests
    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
    querystring = {"query":"apple"}    
    headers = {
        "X-RapidAPI-Key": "80ad4f850cmshe617b19ac5967a4p156138jsnd7d3d30677c4",
        "X-RapidAPI-Host": "calorieninjas.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    return response.json()['items']



if __name__ == "__main__":
    app.run(debug=True)
        
        