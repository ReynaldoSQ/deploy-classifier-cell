from fastai.vision import load_learner, open_image

def prediction(dir, img):
    Clasificador=load_learner(dir)
    indices={0: 'ductal', 1: 'lobular'}
    #categoria,tensor,array_prob
    cat,t,arr=Clasificador.predict(img)
    arr=arr*100
    pred='Lobular: '+str(arr[1])+ ' Ductal: '+ str(arr[0])
    
    return pred 

def img_load(dir_url):
    img=open_image(dir_url)
    return img