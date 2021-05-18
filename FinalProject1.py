import os

def rename_file():

    i=0

    for file_name in  os.listdir(r"C:\\Users\\fc\\Desktop\\Marriottspractice"):
        dst="hotel" + str(i) + ".jpg"
        src='Marriottspractice' + file_name
        dst='Marriottspractice' + dst
        
        os.rename(r'C:/Users/fc/Desktop/Marriotts/Marriott_Chicago.jpg',r'C:/Users/fc/Desktop/Marriottspractice\hotel_Chicago.jpg') 
        os.rename(r'C:/Users/fc/Desktop/Marriotts/Marriott_LA.jpg',r'C:/Users/fc/Desktop/Marriottspractice\hotel_LA.jpg')
        os.rename(r'C:/Users/fc/Desktop/Marriotts/Marriott_miami.jpg',r'C:/Users/fc/Desktop/Marriottspractice\hotel_miami.jpg') 
        os.rename(r'C:/Users/fc/Desktop/Marriotts/Marriott_NewOrleans.jpg',r'C:/Users/fc/Desktop/Marriottspractice\hotel_NewOrleans.jpg') 
        os.rename(r'C:/Users/fc/Desktop/Marriotts/Marriott_stlouis.jpg',r'C:/Users/fc/Desktop/Marriottspractice\hotel_stlouis.jpg') 


        i += 1
    print("All files has been renamed successfully...")

rename_file()