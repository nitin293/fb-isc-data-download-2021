import os

try:
    option = int(input("\nOptions :\n\t(1) Download All\n\t(2) Download Subset\n\t(3) Download Specific Image : \n\nEnter Option : "))
    imageopt = int(input("\nOptions :\n\t(1) Query Images\n\t(2) Reference Images\n\t(3) Training Images\n\nEnter Option : "))
    img_dirs = ['query_images', 'reference_images', 'training_images']

    imageset = img_dirs[imageopt-1]

    if option in range(1,4):
        downloaddir = input("Enter path you want to save image : ")

        if option == 1:
            cmd = f"aws s3 cp s3://drivendata-competition-fb-isc-data/all/{imageset}/ {downloaddir} --recursive --no-sign-request"
            os.system(cmd)

        elif option == 2:
            print("To download the images in the query set, eg- \n(Q01000.jpg to Q01999.jpg) you enter value : Q01*")
            subset = input("\nEnter query set : ")

            cmd = f"aws s3 cp s3://drivendata-competition-fb-isc-data/all/{imageset}/ {downloaddir} --recursive --exclude='*' --include='{subset}*' --no-sign-request"
            os.system(cmd)

        elif option == 3:
            image = input("Enter image name [eg. Q00123.jpg]: ")
            cmd = f"aws s3 cp s3://drivendata-competition-fb-isc-data/all/{imageset}/{image} {downloaddir} --no-sign-request"
            os.system(cmd)

        else:
            exit()

    else:
        print("[-] Invalid Input !")

except KeyboardInterrupt:
    print("\nCtrl + C detected !")
    
except:
    pass
