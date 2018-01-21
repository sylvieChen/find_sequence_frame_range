"""
General Python Test:

    Write a function that finds all animated sequences in a given directory,
    and prints their frame ranges in the following format:
        'name: 1001-2000' if there are no gaps
        'name: 1001, 1003-1500, 1600-2000' if there are gaps

    The format for an animated sequence is name.####.ext
        e.g. /job/.../my_render_v001.1001.jpg
"""
import os
import re


def get_valid_sequence_files(file_path_names):
    file_name_data = dict()
    fileformat = re.compile("\.{1,1}[0-9]{4,4}\.{1,1}")
    for file_path_name in file_path_names:
        file_base_name = os.path.basename(file_path_name)
        if fileformat.search(file_base_name):
            file_name, frame_num, ext = file_base_name.split('.')
            files = file_name_data.setdefault(file_name, list())
            files.append(file_base_name)
    return file_name_data


def get_sequence_frame_range_on_disk(file_dir):
    """
    Finds all animated sequences in a given directory.

    :param file_dir: `str`
    :return:  `dict`
                Dictionary of the sequence frame range.
    """
    sequence_frame_data = dict()
    file_path_names = os.listdir(file_dir)
    valid_sequence_files = get_valid_sequence_files(file_path_names)

    for seq_name, file_base_names in valid_sequence_files.iteritems():
        start_file = sorted(file_base_names)[0]
        end_file = sorted(file_base_names)[-1]
        start_frame = int(start_file.split('.')[1])
        end_frame = int(end_file.split('.')[1])
        continue_frames = sequence_frame_data.setdefault(seq_name, list())

        frames_on_disk = [file_base_name.split('.')[1] for file_base_name in file_base_names]
        frame_padding_start = frames_on_disk[0]
        frame_padding_end = frames_on_disk[-1]
        if (end_frame-start_frame+1) != len(file_base_names):
            for index, frame_padding_name in enumerate(frames_on_disk):
                if index < (len(frames_on_disk) - 1):
                    if int(frame_padding_name) + 1 != int(frames_on_disk[index + 1]):
                        if frame_padding_start!=frame_padding_name:
                            continue_frames.append('{0}-{1}'.format(frame_padding_start, frame_padding_name))
                        else:
                            continue_frames.append('{0}'.format(frame_padding_start))
                        frame_padding_start = frames_on_disk[index + 1]
                        if index == (len(frames_on_disk) - 2):
                            continue_frames.append('{0}'.format(frame_padding_start))
        else:
            if frame_padding_start != frame_padding_end:
                continue_frames.append('{0}-{1}'.format(frame_padding_start, frame_padding_end))
            else:
                continue_frames.append('{0}'.format(frame_padding_start))
    return sequence_frame_data


if __name__ == "__main__":
    from pprint import pprint
    results = get_sequence_frame_range_on_disk(file_dir='C:\Users\yan\Desktop\missing_frame')
    pprint(results, width=1)

