from pytube import YouTube

try:
    yt = YouTube(input("Enter link :"))
except:
    print("Connection Error")

myFile = yt.streams.first()
 
try:  
    myFile.download('/Users/sarjhana/Documents/')  
except:  
    print("Some Error!")  
print('Task Completed!')
