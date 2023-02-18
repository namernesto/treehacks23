import requests
import string
import gensim
import json

from bs4 import BeautifulSoup

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# TODO: consider lowercase?

def process_sentence(words):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    a = []
    tokens = word_tokenize(words)
    for token in tokens:
        lemmetized_word = lemmatizer.lemmatize(token)
        if lemmetized_word not in stop_words and lemmetized_word not in string.punctuation:
            a.append(lemmetized_word)
    return a

class Faculty:
    def __init__(self, url):
        self.name = None
        self.bio = None
        self.publication_titles = None
        self.publication_abstracts = None
        self.title = None
        self.url = url

    def get_info(self):
        result = requests.get(self.url)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        # Checks if a bio and/or pulications exists
        hasPublications = False
        hasBio = False
        all_h3 = soup.find_all("h3")
        for h3 in all_h3:
            if "Bio" in h3.text:
                hasBio = True
            if "All Publications" in h3.text:
                hasPublications = True

        all_p = soup.find_all("p")

        # Adds faculty bio
        if hasBio:
            bio_class = soup.find_all("div", {"id": "bioContent"})
            # self.bio = process_sentence([bio.find("p").get_text() for bio in bio_class][0])
            self.bio = [bio.find("p").get_text() for bio in bio_class][0]

        if hasPublications:
            # Adds publication titles
            publications = soup.find_all("li", {"class": "publication inproceedings"}) + soup.find_all("li", {"class": "publication article"}) 
            temp_pub_titles = [title.find("span", {"class": "title"}).find("span").get_text().replace("\n", "") for title in publications]
            # self.publication_titles = [process_sentence(temp_title) for temp_title in temp_pub_titles]
            self.publication_titles = [temp_title for temp_title in temp_pub_titles]
            # Adds publication abstracts
            temp_pub_abstracts = [pub.get_text() for pub in soup.find_all("p", {"class": "abstract"})]
            # self.publication_abstracts = [process_sentence(temp_abstracts) for temp_abstracts in temp_pub_abstracts]
            self.publication_abstracts = [temp_abstracts for temp_abstracts in temp_pub_abstracts]

        # Adds faculty name
        nameAndTitle = soup.find_all("div", {"class": "nameAndTitle"})
        self.name = [name.find("h1").get_text() for name in nameAndTitle][0]

        # Adds faculty title
        # self.title = process_sentence([title.find("h2").get_text() for title in nameAndTitle][0])
        self.title = [title.find("h2").get_text() for title in nameAndTitle][0]



currFaculty = Faculty("https://profiles.stanford.edu/maneesh-agrawala")
currFaculty.get_info()

# word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('/Documents/word2vec_pre-trained/GoogleNews-vectors-negative300.bin.gz', binary=True)
# for w_title, w_bio, s_pub_titles, s_pub_abstracts in currFaculty.title, currFaculty.bio, currFaculty.publication_titles, currFaculty.publication_abstracts:
#     w_title = word2vec_model.wv[w_title]
    # for i in range(len(s_pub_titles)):
    #     words = row[i].split()
    #     row[i] = [word2vec_model.wv[word] for word in words]
# print(currFaculty.publication_abstracts)


# test_list_faculty.append(currFaculty)