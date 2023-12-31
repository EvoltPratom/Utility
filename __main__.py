import argparse
import os
from howto import help_strings

def test1():
    print("Test1. It works")

from util1 import organize, flatten
from multimedia import img2pdf, pdf2img, convert_music, mp4tomp3, ytmp3, yt_playlist_mp3, combine_music

parser = argparse.ArgumentParser(description="PyUtils")

# Add subparsers for each function
subparsers = parser.add_subparsers(dest="function_name", help="Choose a function to run")

# Subparser for Organize
parser_function1 = subparsers.add_parser("organize", help=help_strings["organize"])
parser_function1.add_argument("--path", type=str, default=os.getcwd(), help="folder_path")
parser_function1.add_argument("--config", default=None, help="Config defaults to config.json")

# Subparser for flatten
parser_function2 = subparsers.add_parser("flatten", help=help_strings["flatten"])
parser_function2.add_argument("--path", type=str, default=os.getcwd(), help="folder_path")

# Subparser for img2pdf
parser_function3 = subparsers.add_parser("img2pdf", help=help_strings["img2pdf"])
parser_function3.add_argument("--path", type=str, default=os.getcwd(), help="folder_path")
parser_function3.add_argument("--output", type=str, default=None, help="output PDF")
parser_function3.add_argument("--dimg", type=bool, default=False, help="Delete Images")

# Subparser for pdf2img
parser_function3 = subparsers.add_parser("pdf2img", help=help_strings["pdf2img"])
parser_function3.add_argument("path", type=str, help="pdf_path")
parser_function3.add_argument("--output", type=str, default=os.getcwd(), help="output path")

# Subparser for convert_music
parser_function3 = subparsers.add_parser("convert_music", help=help_strings["convert_music"])
parser_function3.add_argument("--path", type=str, default=None ,help="audio folder")
parser_function3.add_argument("--format", type=str, default=None, help="output format")
parser_function3.add_argument("--daudio", type=bool, default=False, help="Delete originals")

#Subparser for yt mp3 download
parser_function4 = subparsers.add_parser("ytmp3", help=help_strings["ytmp3"])
parser_function4.add_argument("uri", type=str, help="yt uri")
parser_function4.add_argument("--title", type=str, default=None, help="title in mp4 format")


#Subparser for mp4tomp3 download
parser_function5 = subparsers.add_parser("mp4tomp3", help=help_strings["mp4tomp3"])
parser_function5.add_argument("path", type=str, help="Path of the video")

#Subparser for test download
parser_function6 = subparsers.add_parser("test1", help="Yess")
parser_function6.add_argument("--path", default="sd", type=str, help="test")

#subparser for yt playlist
parser_function7 = subparsers.add_parser("yt_playlist_mp3", help=help_strings["yt_playlist_mp3"])
parser_function7.add_argument("uri", type=str, help="playlist url")

# Subparser for combine_music
parser_function8 = subparsers.add_parser("combine_music", help=help_strings["combine_music"])
parser_function8.add_argument("--path", type=str, default=None ,help="audio folder")

# Parse command line arguments
args = parser.parse_args()
func_name = args.function_name
func = globals()[func_name]

if func_name == "organize":
    func(args.path,args.config)
elif func_name == "flatten":
    func(args.path)
elif func_name == "img2pdf":
    func(args.path,args.output,args.dimg)
elif func_name == "pdf2img":
    func(args.path, args.output)
elif func_name == "convert_music":
    func(args.path,args.format,args.daudio)
elif func_name == "ytmp3":
    func(args.uri)
elif func_name == "mp4tomp3":
    func(args.path)
elif func_name == "test1":
    test1()
elif func_name == "yt_playlist_mp3":
    func(args.uri)
elif func_name == "combine_music":
    func(args.path)


