# Given a title and an optional list of minor words not to be titleized
# return a title with the correct capitalization
def title_case(title, minor_words=''):
    # split the minor words into an all lowercase list so that
    # the words in the title can be easily checked for list membership
    minor_words = [word.lower() for word in minor_words.split()]
    # split the words given in the title into a dictionary for easy
    # iteration, and all lower case for normalization for comparison with
    # minor words
    words_in_title = [word.lower() for word in title.split()]
    for index, word in enumerate(words_in_title):
        # titleize in place every word in the title that is not found in the 
        # minor words exception group, or if it is the first word since that is
        # always capitalized
    	words_in_title[index] = word.title() if word not in minor_words or index == 0 else word
    return ' '.join(words_in_title)
