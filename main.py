from tkinter.ttk import Progressbar
from kivy.app import App
import kivy
import socket
from kivy.uix.tabbedpanel import TabbedPanel
from threading import Thread
from kivy.clock import Clock

kivy.require('1.9.0')

dir = "/storage/emulated/0/Download/"

result = False

class MainWidget(TabbedPanel):
    def change(self):
        self.ids.start.text = "Connected to PC"
        Thread(target=self.server).start();

    def progressbar(self,progress,total):
        percent = (progress/float(total))*100
        percent = round(percent)
        if(percent % 10 == 0):
            current = self.ids.progress.value
            current+=percent
            self.ids.progress.value = current
        self.ids.connect.text = f"{percent} % Received"

    
    def receving(self):
        IP , HOST = "127.0.0.1" , 54000
        cli_socket= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        
        cli_socket.connect((IP,HOST));
        s = cli_socket.recv(1024)
        a = s.decode("utf-8").rstrip('\x00')
        fileName,fileSize =a.rsplit('&$&',1)
        file = open(fileName,"wb")
        fs = int(fileSize)
        FS = fs
        done = 0
        while(fs>0):
            data = cli_socket.recv(1024*1000)    
            fs -= 1024000
            done += 1024000;
            self.progressbar(done,FS)
            file.write(data);
        file.close()
        cli_socket.close()
        return True,FS/1024000,fileName    
            
    def server(self):
        result,fs,filename = self.receving()
        self.connect.text = f"File Received : {filename}  {round(fs,3)} Mb"

class mainApp(App):
    def build(self):
        return MainWidget()

    



mainApp().run()

