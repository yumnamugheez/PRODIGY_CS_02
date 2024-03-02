from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    pixels = img.load()

    # Encrypt the image using XOR operation
    for i in range(img.width):
        for j in range(img.height):
            pixel = pixels[i, j]
            encrypted_pixel = tuple(component ^ key for component in pixel[:3])
            pixels[i, j] = encrypted_pixel

    # Save the encrypted image
    img.save(output_image_path)

def decrypt_image(encrypted_image_path, decrypted_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    pixels = img.load()

    # Decrypt the image using XOR operation
    for i in range(img.width):
        for j in range(img.height):
            pixel = pixels[i, j]
            decrypted_pixel = tuple(component ^ key for component in pixel[:3])
            pixels[i, j] = decrypted_pixel

    # Save the decrypted image
    img.save(decrypted_image_path)

def main():
    input_image_path = input("Enter the path of the input image: ")
    output_image_path = input("Enter the path for the encrypted image: ")
    decrypted_image_path = input("Enter the path for the decrypted image: ")
    key = int(input("Enter the encryption/decryption key: "))

    
    encrypt_image(input_image_path, output_image_path, key)
    print("Image Encrypted Successfully!")

    decrypt_image(output_image_path, decrypted_image_path, key)
    print("Image Decrypted Successfully!")

if __name__ == "__main__":
    main()
