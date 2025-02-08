import os
import subprocess
import sys

def convert_mkv_to_mp4(input_file):
    output_file = os.path.splitext(input_file)[0] + '.mp4'
    try:
        subprocess.run(['ffmpeg', '-i', input_file, '-codec', 'copy', output_file], check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python mkv2mp4.py <path_to_video.mkv>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.isfile(input_file) or not input_file.endswith('.mkv'):
        print("Please provide a valid .mkv file.")
        sys.exit(1)

    convert_mkv_to_mp4(input_file)

if __name__ == "__main__":
    main()