"""
Create two functions for loading and saving pickled data.

The data that has been pickled is a dictionary.  The pickle file is in a folder just underneath this question in Moodle.

The code that is on slide 26

write_binary_mode = "wb"
the_file = open(file_name, write_binary_mode)
pickle.dump(lines, the_file)
the_file.close()

and slide 27

read_binary_mode = "rb"
the_file = open(file_name, read_binary_mode)
lines = pickle.load(the_file)
the_file.close()

of Presentation 9-2 only needs a slight modification in each case.

"""
# Student: Michael Devenport
# Email: croxleyway@gmail.com

import pickle


def load_room_data(data_file):

    """Load pickled file binary mode"""

    read_binary_mode = "rb"
    file = open(data_file, read_binary_mode)
    lines = pickle.load(file)
    file.close()
    return lines


# Specify the file in the current working directory
# room_file = "room_data.p"

# Get the data from the file
# room_data = load_room_data(room_file)

# Show the object type
# print(type(room_data))

# Show the data
# print(room_data)


def save_room_data(room_data, data_file):

    """write binary to pickle file"""

    write_binary_mode = "wb"
    file = open(data_file, write_binary_mode)
    pickle.dump(room_data, file)
    file.close()
    return None


room_info = {
    "person1": "room1",
    "person2": "room2"
}

# Save the dictionary
room_file = "few_staff.p"
return_value = save_room_data(room_info, room_file)
print(type(return_value))
# Load the dictionary
imported_info = load_room_data(room_file)
reqd_user = "person2"
print(imported_info[reqd_user])