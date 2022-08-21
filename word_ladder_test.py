from word_ladder import WordLadder


def test_make_ladder():
    english_words = load_words()

    # Test set containing all the word with given length
    word_length = 27
    assert english_words[word_length] == {'electroencephalographically',
                                          'microspectrophotometrically',
                                          'hydroxydesoxycorticosterone'}

    # Test two words: data and code
    wl_1 = WordLadder("data", "code", english_words[len("data")])
    assert wl_1.make_ladder().items == ["data", "dada", "dade", "cade", "code"]

    # Test two words: cat and hat
    wl_2 = WordLadder("cat", "hat", english_words[len("cat")])
    assert wl_2.make_ladder().items == ["cat", "hat"]

    # Test two words: love and hate
    wl_3 = WordLadder("love", "hate", english_words[len("love")])
    assert wl_3.make_ladder().items == ["love", "hove", "have", "hate"]

    # Test two words: angel and devil
    wl_4 = WordLadder("angel", "devil", english_words[len("angel")])
    assert wl_4.make_ladder().items == ["angel", "anger", "aeger",  "leger",
                                        "lever", "level", "devel", "devil"]
    # Test two words: earth and ocean
    wl_5 = WordLadder("earth", "ocean", english_words[len("earth")])
    assert wl_5.make_ladder().items == ["earth", "barth", "barih",  "baris",
                                        "batis", "bitis", "aitis", "antis",
                                        "antas", "antal", "ontal", "octal",
                                        "octan", "ocean"]

    # Test two same words: hello and hello
    wl_6 = WordLadder("hello", "hello", english_words[len("hello")])
    assert wl_6.make_ladder() is None

    # Test two different length words
    wl_7 = WordLadder("dog", "hate", english_words[len("dog")])
    assert wl_7.make_ladder() is None


def load_words():
    """Load words from complete wordlist file"""
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words
