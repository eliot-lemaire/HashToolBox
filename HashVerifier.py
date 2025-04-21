import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import hashlib

def compute_file_hash( firstFile, algorithm='sha256'):
            firstFileHash = hashlib.new(algorithm)
            
            with open(firstFile, 'rb') as file:
                # Read the file in chunks of 8192 bytes
                while chunk := file.read(8192):
                    firstFileHash.update(chunk)

            return firstFileHash

def hashCalculateButton():
    file_path = filedialog.askopenfilename()
    if file_path:
        hash_value = compute_file_hash(file_path).hexdigest()
        messagebox.showinfo(f"Hash Value", f"Hash of file {hash_value}")
    else:
        messagebox.showwarning("No File", "You didn’t choose a file.")

def compareTwoFilesButton():
    file_path = filedialog.askopenfilename()
    file_path2 = filedialog.askopenfilename()

    hash_value = compute_file_hash(file_path).hexdigest()
    hash_value2 = compute_file_hash(file_path2).hexdigest()

    if hash_value == hash_value2:
        messagebox.showinfo(f"Hash Value", f"files have not been tampered with")
    else:
        messagebox.showinfo(f"Hash Value", f"NOT SAFE, FILE HAS BEEN TAMPERED WITH")

def compareFileHash():
    file_path = filedialog.askopenfilename()
    user_hash = simpledialog.askstring("Input", "Enter the expected hash to compare:")

    hash_value = compute_file_hash(file_path).hexdigest()
    if hash_value == user_hash:
        messagebox.showinfo(f"Hash Value", f"files have not been tampered with")
    else:
        messagebox.showinfo(f"Hash Value", f"NOT SAFE, FILE HAS BEEN TAMPERED WITH")
    


root = tk.Tk() # Creates a window
root.title("Hash tool kit") 
root.geometry("300x150")    # set window size

buttonHashCalculate = tk.Button(root, text="Compute the hash of a file.", command=hashCalculateButton)
buttonHashCalculate.pack(pady=20)

buttonCompareFiles = tk.Button(root, text="Compare 2 files.", command=compareTwoFilesButton)
buttonCompareFiles.pack(pady=20)

buttonHashFileCompare = tk.Button(root, text="Compare a file and a hash.", command=compareFileHash)
buttonHashFileCompare.pack(pady=20)

root.mainloop() # Keeps the window open and waits for input
