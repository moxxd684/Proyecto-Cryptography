# Import necessary libraries
import streamlit as st
import os

# Import required functions from the cryptography library
from cryptography.fernet import Fernet, InvalidToken

# Define the title
st.title("Moaad Cryptography - Encoding and Decoding")

# If the variable texto_cifrado does not exist, create it with a null value
if "st.session_state.texto_cifrado" not in st.session_state:
    st.session_state.texto_cifrado = ""  # Initialize a variable to store the encrypted text

# If the variable clave does not exist, generate a key within that variable using Fernet
if "st.session_state.clave" not in st.session_state:
    st.session_state.clave = Fernet.generate_key()

# Store the uploaded file in the variable archivo
archivo = st.file_uploader("Upload a TXT file", type=["txt"], key="file_uploader_2")

# If the file is present, display the following
if archivo:
    texto = archivo.read().decode("utf-8")  # Read the content of the file and decode it in UTF-8 format
    st.text_area("File content:", texto, height=200)  # Display the content in a text area
    st.session_state.texto_cifrado = texto  # Store the file text in the variable texto_cifrado

# Create the encrypt button
    if st.button("Encrypt"):
        st.session_state.cipher = Fernet(st.session_state.clave)  # Store the key in the variable cipher
        st.session_state.cifrado = st.session_state.cipher.encrypt(texto.encode())  # Encrypt the text using the key and texto.encode()

# If the folder archivos does not exist, create it to store the files with the encrypted and decrypted text
        if not os.path.exists("archivos"):
            os.makedirs("archivos")

        with open("archivos/cifrado.txt", "wb") as f:
            f.write(st.session_state.cifrado)
        st.markdown(f"**Encrypted text:** `{st.session_state.cifrado}`")

# Create the decrypt button
    if st.button("Decrypt"):
        if st.session_state.texto_cifrado:  # If the variable texto_cifrado exists, execute the following
            st.session_state.cipher_dec = Fernet(st.session_state.clave)  # Store the decryption key in the variable cipher_dec

# If the above was successful, then try the following
            try:
                st.session_state.texto_descifrado = st.session_state.cipher_dec.decrypt(st.session_state.cifrado).decode()  # Store the decrypted text in the variable texto_descifrado using the cipher_dec variable with the encryption algorithm

# Create the file descifrado.txt and store the decrypted text
                with open("archivos/descifrado.txt", "w", encoding="utf-8") as f:
                    f.write(st.session_state.texto_descifrado)
                st.markdown(f"**Decrypted text:** `{st.session_state.texto_descifrado}`")

# If the try block was not successful, indicate the specified error
            except (InvalidToken, TypeError) as e:  # type: ignore
                st.error(f"Error: The encrypted text is not valid or the key is incorrect. Details: {e}")

# If the variable texto_cifrado did not exist, show the following error
        else:
            st.warning("There is no valid encrypted text to decrypt. Encrypt a text first")