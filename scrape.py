import requests
import string
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
        self.publications = None

        self.publication_titles.publication_abstracts 
        self.title = None
        self.url = url

        # new
        self.image = None
        self.email = None
        self.awards = None
        self.current_research = None
        self.teaching = None

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

            # TODO: check if have abstract

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

with open('profiles-link.json') as f:
    profile_link = json.load(f)

def generate_faculty_info_dict(Faculty, link):
    cur_dict = {}
    currFaculty = Faculty("https://profiles.stanford.edu" + link)
    currFaculty.get_info()
    cur_dict
    return cur_dict



faculty_info_dict = {}
    for link in profile_link:
        cur_faculty_info = generate_faculty_info_dict()
        # add cur faculty info to facullty info dict 
        faculty_info_dict[link] = cur_faculty_info
        
# attrs = vars(currFaculty)
# print('\n\n '.join("%s: %s" % item for item in attrs.items()))

# word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('/Documents/word2vec_pre-trained/GoogleNews-vectors-negative300.bin.gz', binary=True)
# for w_title, w_bio, s_pub_titles, s_pub_abstracts in currFaculty.title, currFaculty.bio, currFaculty.publication_titles, currFaculty.publication_abstracts:
#     w_title = word2vec_model.wv[w_title]
    # for i in range(len(s_pub_titles)):
    #     words = row[i].split()
    #     row[i] = [word2vec_model.wv[word] for word in words]
# print(currFaculty.publication_abstracts)


# test_list_faculty.append(currFaculty)