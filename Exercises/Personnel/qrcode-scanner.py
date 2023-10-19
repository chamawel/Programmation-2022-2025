#I think u need to import those with 'pip install' to make it work 

import qrcode as qr
import cv2

#Function use for reading a QRcode

def read(name):

    # the file needs to be in the same directory 

    d=cv2.QRCodeDetector()
    val = d.detectAndDecode(cv2.imread(name))
    print(val)
    main()

#Function use to create a QRcode

def create(content,name):
    img= qr.make(content)
    img.save(name)
    main()



print(""""

####################################################
    QR CODE GENERATOR/READER


        by chamawel using: qrcode and open CV
####################################################

""")


def main():

    #asking user's choice
    c=input("""

        What do you want to do?

        a - Read a Qrcode.

        b - create a Qrcode. 

        c - exit program.

    """ )

    #checking the respond

    if c =="a":
        fn=input("What's the file name? (filename -> .png, jpg, ... <- ) ")
        read(fn)


    elif c=="b":

        # "fn" is the file name and "l" is the link contened in the qrcode

        l=input("Copy/paste your link (needs https://.....) ")
        fn=input("Name your file { filename.png} ")

        create(l,fn)


    elif c=="c":
        print("Bye !")
        exit()

    else:
        print("Invalid anser")
        main()



#
#
main()