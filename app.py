from flask import Flask, request, render_template

from classifier import prediction, img_load


app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hellow_world():
    if request.method== 'GET':
        return render_template('index.html',
                    duct='', lob='', adv='')

    if request.method=='POST':

        if 'file' not in request.files:
            print("file not uploaded")
            return 
        file=request.files['file']
        file.save('m.tiff')
        img_pred=img_load('./m.tiff')
        duct, lob, adv=prediction(dir='./',img=img_pred)
        return render_template('index.html', 
                    duct=duct, lob=lob, adv=adv)


if __name__ == '__main__':
    app.run(debug=True)
