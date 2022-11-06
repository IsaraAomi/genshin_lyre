import time, sys, itertools
from tqdm import tqdm
import pyautogui


PON = "----"  # time of newline
SHORT_PROGRESS_BAR="{l_bar}{bar:10}{r_bar}{bar:-10b}"
pyautogui.PAUSE = 0.075


def load_notes(file_path:str)->list:
    """
    - Args:
        - file_path
    - Returns:
        - notes_2char_pack
    """
    notes = []
    notes_2char_pack = []
    char_list_2d = []
    with open(file_path) as f:
        lines = f.readlines()
        # print(lines)
    for i, line in enumerate(lines):
        line = line.strip()
        line = line + PON
        lines[i] = line
    # print(lines)
    for line in lines:
        char_list = list(line)
        char_list_2d.append(char_list)
    notes = list(itertools.chain.from_iterable(char_list_2d))
    # print(notes)
    skip = False
    for i in range(len(notes)-1):
        if (notes[i] != "-" and notes[i+1] != "-"):
            notes_2char_pack.append(notes[i]+notes[i+1])
            skip = True
        else:
            if (skip == True):
                skip = False
                continue
            notes_2char_pack.append(notes[i])
    # print(notes_2char_pack)
    return notes_2char_pack


def debug_by_memo(notes:list):
    """
    - Args:
        - notes
    - Returns:
    """
    # open memo
    pyautogui.press('win')
    pyautogui.write('note')
    time.sleep(1)
    pyautogui.press('enter')

    # input contents
    play(notes)

    # delete contents
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')

    # close memo
    pyautogui.hotkey('alt', 'f4')


def play(notes:list):
    """
    - Args:
        - notes
    - Returns:
    """
    for i in range(3):
        print("\r{}".format(3-i), end='', flush=True)
        time.sleep(1)
    print("\r", end='', flush=True)
    for note in tqdm(notes, bar_format=SHORT_PROGRESS_BAR):
        if (len(note) == 1):
            pyautogui.press(note)
            # print(note)
        elif (len(note) == 2):
            pyautogui.hotkey(note[0], note[1])
            # print(note)
        else:
            print("[ERROR] len(note)=={}".format(len(note)))
            exit(1)        


def main():
    """
    - Args:
    - Returns:
    """
    args = sys.argv
    notes = load_notes(args[1])
    # debug_by_memo(notes)
    play(notes)


if __name__ == '__main__':
    main()
