import qrcode
import os

def generate_qr_code(data, file_name="qrcode.png"):
    
    # define path where QR codes will be saved
    fixed_folder_path = "D:\qrcodepython\QRCodes"
    os.makedirs(fixed_folder_path, exist_ok=True) # making sure that the path where we save exists, otherwise we create it
    full_path = os.path.join(fixed_folder_path, file_name) # combine the fixed folder path and name of the file

    qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 4) # QR code object with dimensions and error correction


    qr.add_data(data) # adding data to QR code
    qr.make(fit = True) # fitting the QR code to the provided data


    # create an image from the QR code instance
    img = qr.make_image(fill_color = "black", back_color = "white") 

    # save the image to the path
    img.save(full_path)
    print(f"QR code saved under name {file_name}")


if __name__ == "__main__":
    user_data = input("Input data to turn into a QR code (e.g. link): ")

    file_name = input("Name the file (e.g. wifipass.png): ")

    generate_qr_code(user_data, file_name) # generate the QR code and save it to the fixed directory