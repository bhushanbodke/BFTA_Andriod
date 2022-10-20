import socket
from base64 import decode

def receving():
    IP , HOST = "127.0.0.1" , 54000
    cli_socket= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    
    cli_socket.connect((IP,HOST));
    s = cli_socket.recv(1024)
    a = s.decode("utf-8")
    a = a.rstrip('\x00')
    fileName,fileSize =a.rsplit('&',1)
    file = open(fileName,"wb")
    fs = int(fileSize)
    FS = fs
    done = 0
    while(fs>0):
        data = cli_socket.recv(1024*1000)    
        fs -= 1024000
        done += 1024000;
        file.write(data);
    file.close()
    cli_socket.close()
    return True,FS/1024000,fileName
           

print(receving())
# f = open("C:\\Users\\cracked\\Desktop\\BFTA\\BFTA_PC\\a.jpg","rb")
# fw = open("smple.jpg","wb")
# while(True):
#     bytes = f.read(4096);
#     if(bytes.__len__() > 0):
#         fw.write(bytes)
#     if(bytes.__len__() == 0 ):
#         break;    
# f.close();
# fw.close();


