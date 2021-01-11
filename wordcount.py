# put your code here.
#define function : count_words
#parameter to be passed in- string of file name
#open the file, store as variable
#Create an empty dictionary to put our word counts
#loop through lines of file and split by " "
    #store that list as variable
    # Loop through the list of words
        # If key exits
            # Increment it by 1
        # If does not exist
            # Set that key value to 1
# Print the unpacked dictionary (loop)

def count_words(file_name):
    text_file = open(file_name)
    result_word_count = {}
    for line in text_file:
        text_line = line.split(" ")
        for word in text_line:
            # if word in result_word_count:
            #     result_word_count[word] += 1
            # else:
            #     result_word_count[word] = 1
            result_word_count[word] = result_word_count.get(word, 0) +1
    for key, value in result_word_count.items():
        print(f"{key} {value}")

count_words('test.txt')