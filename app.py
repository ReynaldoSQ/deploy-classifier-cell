from flask import Flask, request, render_template

from classifier import prediction, img_load


app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hellow_world():
    if request.method== 'GET':
        return render_template('index.html', value="hi")

    if request.method=='POST':

        if 'file' not in request.files:
            print("file not uploaded")
            return 
        file=request.files['file']
        file.save('m.tif')
        image=file.read()
        img_pred=img_load('./m.tif')
        res=prediction(dir='./',img=img_pred)
        return render_template('result.html', 
                    flower=res)


if __name__ == '__main__':
    app.run(debug=True)
