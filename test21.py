# -*- coding: UTF-* -*-
from music21 import converter, instrument, note, chord,stream
import pickle,glob
def print_notes():
    # 读取 MIDI 文件, 输出 Stream 流类型
    stream = converter.parse("feeling.mid")

    # 获得所有乐器部分
    parts = instrument.partitionByInstrument(stream)

    if parts: # 如果有乐器部分，取第一个乐器部分
        notes = parts.parts[0].recurse()
    else:
        notes = stream.flat.notes

    # 打印出每一个元素
    for element in notes:
        print(str(element))

# converter用于转换的，instrument处理乐器部分。
# 音符与和弦的类


def get_notes():
    """
    从 music_midi 目录中的所有 MIDI 文件里提取 note（音符）和 chord（和弦）
    Note 样例： A, B, A#, B#, G#, E, ...
    Chord 样例: [B4 E5 G#5], [C5 E5], ...
    因为 Chord 就是几个 Note 的集合，所以我们把它们简单地统称为“Note”
    """
    notes = []

    # glob : 匹配所有符合条件的文件，并以 List 的形式返回
    for file in glob.glob("*.mid"):
        # 生成流数据
        stream = converter.parse(file)

        # 获取所有乐器部分
        parts = instrument.partitionByInstrument(stream)

        if parts: # 如果有乐器部分， 取第一个乐器部分
            notes_to_parse = parts.parts[0].recurse()
        else:
            notes_to_parse = stream.flat.notes

        for element in notes_to_parse:
            # 如果是Note类型，那么取它的音调
            if isinstance(element, note.Note):
                # 格式例如： E6
                notes.append(str(element.pitch))
            # 如果是Chord类型，那么取它各个音调的序号
            elif isinstance(element, chord.Chord):
                # 转换后格式例如： 4.15.7
                notes.append('.'.join(str(n) for n in element.normalOrder))

    print(notes)

    # 将数据写入 data/notes 文件
    with open('data/notes', 'wb') as filepath:
        pickle.dump(notes, filepath)

    return notes

if __name__ == "__main__":
    get_notes()

