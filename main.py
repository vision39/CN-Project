import os
import zlib

def compress_file(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' not found.")
        return
    with open(input_file, 'rb') as f:
        data = f.read()
    compressed_data = zlib.compress(data)
    with open(output_file, 'wb') as f:
        f.write(compressed_data)

def decompress_file(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' not found.")
        return
    with open(input_file, 'rb') as f:
        compressed_data = f.read()
    decompressed_data = zlib.decompress(compressed_data)
    with open(output_file, 'wb') as f:
        f.write(decompressed_data)

# Example usage
input_file = input("Enter the name of the file to compress: ")
output_compressed_file = input("Enter the name for the compressed file: ")
compress_file(input_file, output_compressed_file)

input_compressed_file = input("Enter the name of the file to decompress: ")
output_decompressed_file = input("Enter the name for the decompressed file: ")
decompress_file(input_compressed_file, output_decompressed_file)
