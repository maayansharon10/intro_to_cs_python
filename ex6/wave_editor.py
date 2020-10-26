import math
import os
import copy
import wave_helper as wh

# max and min values are constant, as defined in exercise
MAX_VOLUME = 32767
MIN_VOLUME = -32768
SAMPLES_PER_UNIT = 125


##############################################################################
# Main Menu Functions:


def display_main_menu():
    """ this func prints the main menu """
    print("welcome to wave_editor!\n"
          "what would you like to do? \n"
          "1. change wav file\n"
          "2. marge wav files\n"
          "3. compose in format which suits wav\n"
          "4. exit program\n"
          "please choose your preference 1,2,3 or 4")


def get_menu_input(mode):
    """input: mode: main, wav or transition
    this func asks the user for an input.
    Checks if:
    1. input is a number
    2. input value is in set of valid choices
    returns: user_input or None"""

    user_input = input(" ")
    # Some tests can't work without a string
    choices = {"main": {1, 2, 3, 4}, "wav": {1, 2, 3, 4, 5, 6},
               "transition": {1, 2}}
    # sets with int according to the mode's menu.

    if not user_input.isnumeric() or int(user_input) not in choices[mode]:
        # If input is not a number, or input is not in set of valid choices:
        print("user input is not valid")
        return None

    return int(user_input)
    # In case value is valid


def check_file_exists(file):
    """check if arg is an existing file.
    input - a string with name of the file.
    output -True if file  exists / False if not"""
    if os.path.exists(file):
        return True
    else:
        print("File path does not exist.")
        return False


def get_file_to_change():
    """func asks user for filename or directory, if the input is valid,
    returns filename or directory"""
    result = False
    while result is False:
        # as long as input is not valid, while loop continues
        file_name = input("please insert a file name or a valid directory \n")
        result = check_file_exists(file_name)
        if result is True:
            return file_name


##############################################################################
# Change Wav Functions:


def display_change_wav_menu():
    """ this func prints the change-wave menu """
    print("### Change Wave Menu ###\n"
          "Welcome to change wave file menu! \n"
          "1. reverse file\n"
          "2. speed up file\n"
          "3. slow down file\n"
          "4. turn volume up\n"
          "5. turn volume down\n"
          "6. lowpass filter\n"
          "Please choose your preferece from 1 to 6:")


def reverse_wav(original_list):
    """input: list
    Returns a reversed list"""
    reversed_audio_data = original_list[::-1]
    return reversed_audio_data


def fast_forward(original_list):
    """input: a list
    Returns a list contains only the even index items
    from original list"""
    double_speed_audio_data = original_list[::2]

    return double_speed_audio_data


def average_item(original_list1, i, original_list2=None):
    """input a list, index i and lst2
    Returns a list of two items, after calculating average.
    Has two modes: one list entered or two."""

    # one list mode:
    # If only one audio data entered, calculates the average of the
    # first/second item in the i index, and the first/second item in the
    # i-1 index.

    if original_list2 is None:
        # if there are 2 lists, append the average
        first_value = int(
            (original_list1[i - 1][0] + original_list1[i][0]) / 2)
        second_value = int(
            (original_list1[i - 1][1] + original_list1[i][1]) / 2)

    # two lists mode:
    # Calculates the average of two items in different lists, first and first,
    # second and second.
    else:
        first_value = int((original_list1[i][0] + original_list2[i][0]) / 2)
        second_value = int((original_list1[i][1] + original_list2[i][1]) / 2)

    return [first_value, second_value]


def low_pass_average(original_list, i):
    """Calc average of 3 items in a list.
    Returns a list of two items, one for each channel.
    Each item in list is the average of 3 values:
    previous, current and next audio data"""

    average = []
    for channel in (0, 1):
        prev = original_list[i - 1][channel]
        curr = original_list[i][channel]
        next = original_list[i + 1][channel]
        # append the average of 3 items into list
        average.append(int((prev + curr + next) / 3))

    return average


def slow_down(original_list):
    """Adds between every two sample rates in original list,
    an average sample rate of their values.
    Uses create_average_item() function"""

    if original_list == []:
        # Empty list case
        return original_list

    slower_audio_data = []
    slower_audio_data.append(original_list[0])

    for i in range(1, len(original_list)):
        # using average_items in mode 1 - one list
        new_item = average_item(original_list, i)
        # add the average item between two original items
        slower_audio_data.append(new_item)
        slower_audio_data.append(original_list[i])

    return slower_audio_data
    # returned modified list


def volume_up(original_list):
    """Raise the values of all sample rates by multiplying them by 1.2.
    Special cases are for greater or lower then MAX_VOLUME/MIN_VOLUME
    (defined in the beginning of code)"""
    
    # deep copy for original list so we could change this list only
    new_audio_data = copy.deepcopy(original_list)
    len_new_audio_data = len(new_audio_data)
    for i in range(len_new_audio_data):
        # go through all items in new_audio_data
        for channel in range(0, 2):
            # in sub list of 2 [L,R]
            if new_audio_data[i][channel] > MAX_VOLUME / 1.2:
                new_audio_data[i][channel] = MAX_VOLUME
                # if the channel after multiplying is larger then MAX_VOLUME
                # - append MAX_VOLUME
            elif new_audio_data[i][channel] < MIN_VOLUME / 1.2:
                new_audio_data[i][channel] = MIN_VOLUME
                # if channel after multiplying is smaller them MIN_VOLUME -
                # append MIN_VOLUME
            else:
                # if channel is between MIN and MAX volume -
                # calc regularly
                new_audio_data[i][channel] = \
                    int(new_audio_data[i][channel] * 1.2)
    return new_audio_data


def volume_down(original_list):
    """Lower the values of all sample rates by dividing them by 1.2.
    Special cases are for greater or lower then MAX_VOLUME/MIN_VOLUME
    (defined in the beginning of code)"""

    new_audio_data = copy.deepcopy(original_list)
    len_audio_data = len(new_audio_data)
    for i in range(len_audio_data):
        for channel in range(0, 2):
            # go through sub lists [L,R]:
            # first 2 if's cover cases when channel exceeds MAX or MIN volume
            if new_audio_data[i][channel] > MAX_VOLUME * 1.2:
                new_audio_data[i][channel] = MAX_VOLUME
            elif new_audio_data[i][channel] < MIN_VOLUME * 1.2:
                new_audio_data[i][channel] = MIN_VOLUME
            else:
                # if does not exceed - clac regularly
                new_audio_data[i][channel] = \
                    int(new_audio_data[i][channel] / 1.2)
    return new_audio_data


def low_pass_filter(original_list):
    """Returns a list where each audio data value is the
    average of next, current and previous data.
    For first and last item - calculates next/previous item.
    Uses faded average() and create_average_item()"""
    faded_audio_data = []
    
    # if the list has up until 2 items - return list as is
    if len(original_list) < 2:
        return original_list
    len_original_list = len(original_list)
    for i in range(len_original_list):
        if i == 0:
            faded_audio_data.append(average_item(original_list, i + 1))
        elif i == len(original_list) - 1:
            faded_audio_data.append(average_item(original_list, i))
        else:
            faded_audio_data.append(low_pass_average(original_list, i))

    return faded_audio_data


def change_wav_file_main(original_list=None, frame_rate=None):
    """This function gets an audio file, and make changes on it's audio data.
    Mode 1: no file has been entered. Asks for file, gets its data first.
    Mode 2: File has already been loaded (as argument), no need to get file
    Returns an modified list."""

    choice = None
    if original_list is None:  # mode 1
        audio_file_name = get_file_to_change()
        frame_rate, original_list = wh.load_wave(audio_file_name)

    while choice is None:
        # Displays menu until input is correct
        display_change_wav_menu()
        choice = get_menu_input("wav")

    if choice == 1:
        # user requested to reverse file
        modified_list = reverse_wav(original_list)

    elif choice == 2:
        # # user requested to fast forward file
        modified_list = fast_forward(original_list)

    elif choice == 3:
        # user requested to slow down file
        modified_list = slow_down(original_list)

    elif choice == 4:
        # user requested to turn volume up in file
        modified_list = volume_up(original_list)

    elif choice == 5:
        # user requested to turn volume down in file
        modified_list = volume_down(original_list)

    elif choice == 6:
        # user requested to low pass filtet on file
        modified_list = low_pass_filter(original_list)

    return frame_rate, modified_list
    # frame rate can change once new file is loaded.
    # both are returned so user can choose to keep edit same data


##############################################################################

# Merge Functions:
def display_merge_menu():
    """this func prints merge menu - the instructions for merging"""
    print("### Merge 2 Files ###\n"
          " welcome merging files!\n "
          "Here you can choose two files to merge.\n"
          "Enter them one by the other.")


def which_sample_rate_higher(lst1, sample_rate1, lst2, sample_rate2):
    """this func checks which sample rate (num) is higher.
    input - 2 num, output- (higher_sample_lst, higher_sample,
    lower_sample_lst, lower_sample).
    assuming sample rate in the correct range"""
    if sample_rate1 >= sample_rate2:
        return lst1, sample_rate1, lst2, sample_rate2
    else:
        return lst2, sample_rate2, lst1, sample_rate1


def convert_lst_sample_rate(lst1, sample_rate1, sample_rate2):
    """input - lst1, sample_rate (of lst1), sample_rate (of lst2)
      func convert lst1 to a new lst according to the 2nd sample rate.
      output - new lst
      we assume sample_rate1>=sample_rate2"""
    new_lst = []
    # calc the gcd of sample rates in order to know which num to append to
    # new_lst
    gcd_val = find_gcd(sample_rate1, sample_rate2)
    # knowing sample_rate1>= sample_rate2 we know that x>=y
    x = sample_rate1 / gcd_val
    y = sample_rate2 / gcd_val
    # len of the list with higher sample_rate - the one we need to convert
    len_lst1 = len(lst1)
    # we check for all index of higher_sample_lst, we will append only the
    # first items in higher_sample_lst to new lst, according to the calc

    for i in range(len_lst1):
        # for every index of len lst1
        if i % x < y:
            # we take only the y num of items from every x items in lst and
            # append them to new lst
            new_lst.append(lst1[i])
    # now new lst has lst1 items, modified according to sample_rate2
    # this way we have two audio data with same sample rate, the lower one
    return new_lst


def find_gcd(num1, num2):
    """inout - 2 numbers from type int.
    output - greatest common divider, euclid's algorithm as we saw in class"""
    if num2 == 0:
        return num1
    return find_gcd(num2, num1 % num2)


def merge_same_samplerate_lsts(lst1, lst2):
    """this func merges two lists of wave files into one.
     input - 2 lsts with same sample rate
     output - one merged lst
     we assume the frame rate of both lists are the same """
    new_lst = []
    len_lst1 = len(lst1)
    len_lst2 = len(lst2)
    max_list = max(len_lst1, len_lst2)
    # we want the range to be longest of both lists so we could have all
    # items over all
    for i in range(max_list):
        if len_lst1 > i and len_lst2 > i:
            # if both lists are longer then i, meaning we item[i] in both
            # lists - we will calculate average and append to new list as
            # sublist with 2 items from this form [[1,1],[1,1],...]

            new_lst.append(average_item(lst1, i, lst2))

        elif len_lst1 > i:
            # if we have more items on first list - append them to new list
            # (now in lst2 ran out of items)
            new_lst += (lst1[i:])
            break
        else:
            # if len_lst2<i, so if we have more items on 2nd lst -
            # append them to the new list
            new_lst += (lst2[i:])
            break
    return new_lst  # the merge of lst1 and lst2 as requested


def merging_wave_files(lst1, sample_rate1, lst2, sample_rate2):
    """input: lst1, sample_rate1, lst2, sample_Rate2
    (sample_rate are int )
    func check if sample rates are not the same, if so orgenize them and
    convert the list with higher sample rate to a lower sample rate"""
    # check if lists doesn't have same sample rate and if so - organize them
    #  and convert the list with highest sample rate
    if sample_rate1 != sample_rate2:
        # if not equal - organize sample rate and lst in this order
        # (higher_sample_lst, higher_sample, lower_sample_lst, lower_sample)
        lst1, sample_rate1, lst2, sample_rate2 = which_sample_rate_higher(
            lst1, sample_rate1, lst2, sample_rate2)
        # now we know for sure lst1 has the same or higher sample rate then
        # lst 2 (sample_rate1 >= sample_rate2) so we will convert lst 1
        lst1 = convert_lst_sample_rate(lst1, sample_rate1, sample_rate2)
    # if sample_rate1 == sample_rate2 - merge 2 lists.
    merged_lst = merge_same_samplerate_lsts(lst1, lst2)
    return sample_rate2, merged_lst


def merge_wave_files_main():
    """ this func asks user for input, once valid, it load the audio
    data and then merge the two files.
    :return final_sample_rate, merged_file"""
    # print out instructions
    display_merge_menu()
    # get a valid file name from user
    audio_file_name1 = get_file_to_change()  # File name is now valid
    audio_file_name2 = get_file_to_change()  # File name is now valid
    # get data from files - int, list of lists:
    sample_rate1, original_list1 = wh.load_wave(audio_file_name1)
    sample_rate2, original_list2 = wh.load_wave(audio_file_name2)

    # Returns them into a list of merged audio with same sample rate:

    final_sample_rate, merged_audio = merging_wave_files(original_list1,
                                                         sample_rate1,
                                                         original_list2,
                                                         sample_rate2)
    return final_sample_rate, merged_audio


##############################################################################

# Compose functions:


def samples_per_cycle(musical_note):
    """Calculates part of the formula used in calculate_single_sample().
    Gets a musical note and returns sample_rate divided by it's frequency"""

    sample_rate = 2000 # Default for composing
    frequencies = {"A": 440, "B": 494, "C": 523, "D": 587, "E": 659, "F": 698,
                   "G": 784}
    return sample_rate / frequencies[musical_note]


def calculate_single_sample(musical_note, i):
    """Calculates the data for one sample rate by a known formula.
    Gets a musical note and the i (current sample index)"""

    if musical_note == "Q":
        return 0
    formula_in_sinus = math.pi * 2 * i / samples_per_cycle(musical_note)
    return int(MAX_VOLUME * math.sin(formula_in_sinus))


def data_for_single_note(musical_note, length):
    """Gets a musical note and it's duration (length),
    returns a data list of samples.
    Time is given in product of 1/16 seconds, which has 125 samples each"""

    audio_data = []
    for i in range(length * SAMPLES_PER_UNIT): # Defined in top of file: 125
        current_sample = calculate_single_sample(musical_note, i)
        audio_data.append([current_sample, current_sample])

    return audio_data


def read_data_from_file(music_data_file):
    """Gets a text file, includes musical notes and durations in pattern:
    <spaces> note <spaces> duration.
    Returns a list of tuples: (Musical note, duration)"""

    data_from_file = ""
    with open(music_data_file) as data_file:
        for line in data_file:
            if line[-1] == "\n": # Ignoring the \n
                data_from_file += line[:-1]
                data_from_file += " " # Make sure a space exists
            else: # last line case
                data_from_file += line

    data_list = data_from_file.split() # only data, no spaces
    data_sets_list = []
    number_of_tones = int(len(data_list))
    for i in range(0, number_of_tones, 2): # create a list of tuples
        musical_note = data_list[i]
        length = data_list[i + 1]
        data_sets_list.append((musical_note, length))

    return data_sets_list


def compose_audio_data(instructions_data_file):
    """Gets a name of instructions file, and returns the musical data (list of
    sample rates)"""

    data_to_compose = read_data_from_file(instructions_data_file)
    audio_data = []

    for music_tone in data_to_compose:
        audio_data += data_for_single_note(music_tone[0], int(music_tone[1]))
    return audio_data


def compose_display():
    """func display compose instructions"""
    print("### Compose a composition ###\n"
          "Here you can choose a file with composing instruction.\n"
          "Our function will compose it for you.")


def compose_main():
    """func display compose instructions, get input from user, once valid,
    modified the audio data as lists of lists and returns the modified list"""

    compose_display()
    # asks user for input until valid
    instructions_file_name = get_file_to_change()  # File name is now valid
    modified_list = compose_audio_data(instructions_file_name)
    # modified list contains composition according to user's input
    return modified_list


##############################################################################

# Transition Menu functions:

def save_file(frame_rate, modified_list):
    """user chose filename or directory and func save file there. func saves
    file there.
    input - audio list
    output - file in the directory the user chose"""
    filename = input("how would you like to call your file?")
    # since input always returns a string, file same doesn't require check up
    wh.save_wave(frame_rate, modified_list, filename)
    # file is save in directory


def display_transition_menu():
    """ func displays transition menu """
    print("### Transition Menu ###\n"
          "Welcome to transition menu! \n"
          "what would you like to do?\n"
          "1. save audio\n"
          "2. change audio\n"
          "Please choose your preference from 1 or 2:")


def transition_menu(frame_rate, modified_list):
    """func display transition menu, asks user for input, and returns
    transition value"""

    display_transition_menu()
    user_input = get_menu_input("transition")  # mode transition
    # user input can only be 1 or 2.

    if user_input == 1:
        # User chose SAVE.
        save_file(frame_rate, modified_list)  # Save list as audio file
        return 0  # In order for Main Menu to reset file in use
        # (modified_list=None)

    # User chose CHANGE.
    return 1  # In order for Main Menu to reset file in use
    # (modified_list=None)


##############################################################################

# main menu function:

def main_menu():
    """display menu to user, ask for input and direct to
     the relevant function"""

    choice = -1  # default value to enter loop
    modified_list = None
    frame_rate = None
    while choice != 4:
        # if 4, exit

        if choice!=1:
            display_main_menu()
            choice = get_menu_input("main")

        if choice is None:
            continue

        if choice == 1:
            frame_rate, modified_list = change_wav_file_main(modified_list,
                                                             frame_rate)
            choice = transition_menu(frame_rate, modified_list)

        elif choice == 2:
            frame_rate, modified_list = merge_wave_files_main()
            choice = transition_menu(frame_rate, modified_list)

        elif choice == 3:
            frame_rate = 2000  # by default
            modified_list = compose_main()
            choice = transition_menu(frame_rate, modified_list)

        if choice == 0:  # file as saved in transition menu
            modified_list = None


if __name__ == '__main__':
    main_menu()
