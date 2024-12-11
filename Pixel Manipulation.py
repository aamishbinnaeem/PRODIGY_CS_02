from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Perform encryption by adding the key to pixel values (mod 256 to avoid overflow)
    encrypted_array = (img_array + key) % 256

    # Convert back to an image and save
    encrypted_img = Image.fromarray(np.uint8(encrypted_array))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Perform decryption by subtracting the key from pixel values (mod 256 to avoid underflow)
    decrypted_array = (img_array - key) % 256

    # Convert back to an image and save
    decrypted_img = Image.fromarray(np.uint8(decrypted_array))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Simple Image Encryption/Decryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return

    input_path = input("Enter the input image file path: ").strip()
    output_path = input("Enter the output image file path: ").strip()

    try:
        key = int(input("Enter an integer key for encryption/decryption: ").strip())
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
