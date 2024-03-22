import cv2
import numpy as np

def encrypt_image(image_path, key):
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    np.random.seed(key)
    permutation = np.random.permutation(height * width)

    flattened_img = img.reshape(-1, 3)

    encrypted_img = flattened_img[permutation]

    encrypted_img = encrypted_img.reshape(height, width, 3)

    return encrypted_img

def decrypt_image(encrypted_image, key):
    height, width, _ = encrypted_image.shape

    np.random.seed(key)
    permutation = np.random.permutation(height * width)

    flattened_encrypted_img = encrypted_image.reshape(-1, 3)

    decrypted_img = flattened_encrypted_img[np.argsort(permutation)]

    decrypted_img = decrypted_img.reshape(height, width, 3)

    return decrypted_img

def save_image(image, output_path):
    cv2.imwrite(output_path, image)
    print("Image saved successfully.")

def main():
    image_path = input("Enter the path to the image: ")
    action = input("Do you want to encrypt (E) or decrypt (D) the image? ").upper()
    
    if action == 'E':
        action_text = "encryption"
    elif action == 'D':
        action_text = "decryption"
    else:
        print("Invalid action. Please choose 'E' for encryption or 'D' for decryption.")
        return
    
    key = input(f"Enter the key for {action_text}: ")
    output_path = input(f"Enter the path to save the {action_text} image: ")

    if action == 'E':
        encrypted_image = encrypt_image(image_path, int(key))
        save_image(encrypted_image, output_path)
    elif action == 'D':
        encrypted_image = cv2.imread(image_path)
        decrypted_image = decrypt_image(encrypted_image, int(key))
        save_image(decrypted_image, output_path)

if __name__ == "__main__":
    main()

