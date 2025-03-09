from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    """Encrypts an image by modifying pixel values using XOR operation."""
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply XOR operation on every pixel value with the key
    encrypted_array = img_array ^ key

    # Convert back to image
    
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    """Decrypts an encrypted image by applying the same XOR operation."""
    encrypt_image(image_path, key, output_path)  # Since XOR is reversible

if __name__ == "__main__":
    option = input("Choose operation (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter the path of the image: ").strip()
    key = int(input("Enter a numeric key (0-255): "))  # Key must be within valid pixel value range
    output_path = input("Enter the output file name (e.g., output.png): ").strip()

    if option == "encrypt":
        encrypt_image(image_path, key, output_path)
    elif option == "decrypt":
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid option. Choose 'encrypt' or 'decrypt'.")
