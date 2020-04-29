#coding: UTF8

import ftplib
import os
import time
from transliterate import translit,  get_available_language_codes

host='Адрес Вашего FTP'
user='Логин для входа'
passwd="Пароль для входа"
port=5190#Порт для подключения
filename = ""
FTP = ftplib.FTP()
u_name= os.getlogin()

#Funktions

def upload(path,file):
    FTP.storbinary("STOR "+ path.split('/')[-1], f)


def create ():
    try:
        os.mkdir("C:/users/{}/desktop/Auto_copy_folder".format(u_name))
    except OSError as e:
        print("Folder at PC server olredy exists")

def ftp_login ():
    FTP.connect(host, port)
    FTP.login(user,passwd)



if __name__ == "__main__":
    try:
        create()
    except OSError as e:
        print("Folder olredy exist")



    while True:
        if os.listdir("C:/users/{}/desktop/Auto_copy_folder".format(u_name)):
            file_date = os.listdir("C:/users/{}/desktop/Auto_copy_folder".format(u_name))
            for x in file_date:
                filename=('C:/users/{}/desktop/Auto_copy_folder/{}'.format(u_name,x))
                try:
                    ftp_login()
                except ftplib.Error as e:
                    print("Нет подключения")
                else:
                    FTP.cwd('/media/disk1/Auto_copy_folder')
                    f = open (filename, "rb")
                    try:
                        upload(filename,f)
                    except ftplib.Error as e:
                        print("Ошибка отправки файла", e)
                        f.close()
                        FTP.close()
                    except UnicodeEncodeError as codec:
                        f.close()
                        file = translit(x, reversed = True)
                        new_filename =('C:/users/{}/desktop/Auto_copy_folder/{}'.format(u_name,file))
                        os.rename(filename, new_filename)
                        pass
                    else:
                        if FTP.size(filename.split('/')[-1]) == os.path.getsize(filename):
                            f.close()
                            FTP.close()
                            os.remove(filename)

                        else:
                            print("Данные переданы с ошибкой")
        else:
            time.sleep(5)
