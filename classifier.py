from fastai.vision import load_learner, open_image

def prediction(dir, img):
    Clasificador=load_learner(dir)
    #indices={0: 'ductal', 1: 'lobular'}
    #categoria,tensor,array_prob
    cat,t,arr=Clasificador.predict(img)
    arr=arr*100
    #pred='Lobular: '+str(arr[1])+ ' Ductal: '+ str(arr[0])
    a=arr.numpy()
    adv=advertencia(a[0], a[1])
    return a[0], a[1], adv

def img_load(dir_url):
    img=open_image(dir_url)
    return img

def advertencia(a,b):
    adv='Porcentaje alto.'
    if a<80 and b<80:
        adv='No seguro, se recomienda implementar otra herramienta o fotografía.'
    return adv