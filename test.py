#Test kiểm tra mô hình train
from tensorflow.keras.models import load_model
model=load_model('classifer_Fruit.h5')
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
test_img=load_img('khe.jpg',target_size=(150,150))
import numpy as np
test_img= img_to_array(test_img)
test_img=test_img/255
test_img=np.expand_dims(test_img,axis=0)
result=model.predict(test_img)
if round(result[0][0])==1:
   prediction="CÀ CHUA"
elif round(result[0][1])==1:
   prediction="CAM"
elif round(result[0][2])==1:
   prediction="CHERRY"  
elif round(result[0][3])==1:
   prediction="CHUỐI"  
elif round(result[0][4])==1:
   prediction="DƯA HẤU"  
elif round(result[0][5])==1:
   prediction="DƯA LEO"  
elif round(result[0][6])==1:
   prediction="KHẾ"  
elif round(result[0][7])==1:
   prediction="SẦU RIÊNG"  
elif round(result[0][8])==1:
   prediction="TÁO"  
elif round(result[0][9])==1:
   prediction="XOÀI"  
print('=====> ĐÂY LÀ: ' + prediction)