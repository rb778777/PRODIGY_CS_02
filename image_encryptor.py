import cv2
import numpy as np

def encrypt_image(image_path, key):
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    # Generate a random permutation of pixel indices based on the key
    np.random.seed(key)
    permutation = np.random.permutation(height * width)

    # Flatten the image array
    flattened_img = img.reshape(-1, 3)

    # Apply permutation on flattened image
    encrypted_img = flattened_img[permutation]
    
    # Reshape the encrypted image to its original dimensions
    encrypted_img = encrypted_img.reshape(height, width, 3)

    return encrypted_img

def decrypt_image(encrypted_image, key):
    height, width, _ = encrypted_image.shape

    # Generate the same permutation of pixel indices based on the key
    np.random.seed(key)
    permutation = np.random.permutation(height * width)

    # Flatten the encrypted image array
    flattened_encrypted_img = encrypted_image.reshape(-1, 3)

    # Apply inverse permutation on flattened encrypted image
    decrypted_img = flattened_encrypted_img[np.argsort(permutation)]
    
    # Reshape the decrypted image to its original dimensions
    decrypted_img = decrypted_img.reshape(height, width, 3)

    return decrypted_img

def save_image(image, output_path):
    cv2.imwrite(output_path, image)
    print("Image saved successfully.")

def main():
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption key: "))
    output_path = input("Enter the path to save the encrypted image: ")

    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)

    # Save the encrypted image
    save_image(encrypted_image, output_path)

    # Decrypt the encrypted image
    decrypted_image = decrypt_image(encrypted_image, key)

    # Display the decrypted image
    cv2.imshow("Decrypted Image", decrypted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

