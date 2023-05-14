import os
import sys
import fnmatch


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if sys.platform == 'linux':
    command_ffmpeg = 'ffmpeg'
else:
    # command_ffmpeg = os.path.join(BASE_DIR, 'ffmpeg', 'ffmpeg.exe')
    command_ffmpeg = 'ffmpeg.exe'


def convert_file(source_path: str, destination_path: str, ext='avi', debug='-ss 00:00:00 -to 00:00:10'):
    # setting up convertion variables
    codec_video = '-c:v libx264'
    crf = '-crf 23'
    preset = '-preset ultrafast'
    codec_audio = '-c:a aac'
    bitrate_audio = '-b:a 320k'


    for root, _, files in os.walk(source_path):
        for file in files:
            if not fnmatch.fnmatch(file, '*.mkv'):
                continue

            fullpath_file = os.path.join(root, file)
            file_name, _ = os.path.splitext(fullpath_file)
            subtitle_path = file + '.srt'

            if os.path.isfile(subtitle_path):
                input_subtitle = f'-i "{subtitle_path}"'
                map_subtitle = '-c:s srt -map v:0 -map a -map 1:0'
            else:
                input_subtitle = ''
                map_subtitle = ''
            print(file)
            # output file
            output_file = f'{destination_path}/{file[:-4]}.{ext}'

            command = \
                f'{command_ffmpeg} -i "{fullpath_file}" {input_subtitle} '\
                f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} '\
                f'{debug} {map_subtitle} "{output_file}"'

            print(f'Comando: {command}')
            os.system(command)
            print('Files successeful converted!')


if __name__ == '__main__':
    # path
    # linux
    source_path = '/mnt/c/Users/leleu/Videos/English_Casses' 
    destination_path = '/mnt/c/Users/leleu/Videos/English_Classes_AVI' 
    # windows
    # r'C:\Users\leleu\Videos\English_Casses'
    # r'C:\Users\leleu\Videos\English_Classes_AVI'

    debug = ''

    # convertion
    convert_file(source_path=source_path, destination_path=destination_path,
                 ext='avi', debug=debug)
