import requests
import string
import gensim
import json

from bs4 import BeautifulSoup

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# TODO: consider lowercase?

def generate_faculty_info_dict(Faculty, link):
    currFaculty = Faculty("https://profiles.stanford.edu" + link)
    currFaculty.get_info()
    cur_dict = currFaculty.__dict__
    return cur_dict

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
        self.title = None
        self.url = url
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
        hasAwards = False
        hasEmail = False
        hasCurResearch = False
        hasTeaching = False 
        teachingTab = soup.find_all("a", {"id": "teachingTabLink"})
        for tab in teachingTab:
            if "Teaching" in tab.text:
                hasTeaching = True

        all_h3 = soup.find_all("h3")
        for h3 in all_h3:
            if "Bio" in h3.text:
                hasBio = True
            if "All Publications" in h3.text:
                hasPublications = True
            if "Honor & Awards" in h3.text:
                hasAwards = True
            # slightly misleading, as you can have contact but not email, can fix later
            if "Contact" in h3:
                hasEmail = True
            if "Current Research and Scholarly Interests" in h3.text: 
                hasCurResearch = True

        all_p = soup.find_all("p")

        # Adds faculty bio
        if hasBio:
            bio_class = soup.find_all("div", {"id": "bioContent"})
            try:
                self.bio = [bio.find("p").get_text() for bio in bio_class][0]
            except:
                self.bio = None

        if hasPublications:
            self.publications = {}
            # Adds publication titles
            publications = soup.find_all("li", {"class": "publication inproceedings"}) + soup.find_all("li", {"class": "publication article"}) 
            for publication in publications:
                try: 
                    title = publication.find("span", {"class": "title"}).find("span").get_text().replace("\n", "")
                    abstract = ""
                    abstract_html = publication.find("p", {"class": "abstract"})
                    if abstract_html is not None:
                        abstract = abstract_html.get_text()
                    self.publications[title] = abstract
                except:
                    continue

        if hasAwards:
            # Adds faculty awards
            awardID = soup.find_all("div", {"id": "honorsAndAwardsContent"})
            self.awards = [awardID.find_all("div" , {"class": "description bulleted"}).get_text()] # don't think I need this award

        # if hasEmail:
        #     # Adds faculty email
        #     botPadList = soup.find_all("div", {"class": "extra-bottom-padding"})
        #     # print(botPadList)
        #     t = [w.find("a") for w in botPadList]
        #     self.email = t
            # print(self.email)

        # Adds faculty teaching
        if hasTeaching:
            class_course = soup.find_all("li", {"class", "course"})
            self.teaching = list(set([c.find("a").text for c in class_course]))

        if hasCurResearch: 
            divID = soup.find("div", {"id": "currentResearchAndScholarlyInterestsContent"})
            self.current_research = divID.find("p").get_text()

        # Adds faculty image
        image_holder = soup.find_all("div", {"class": "image-holder"})
        self.image = [i.find("img") for i in image_holder][0].get('src')
        
        # Adds faculty name
        nameAndTitle = soup.find_all("div", {"class": "nameAndTitle"})
        self.name = [name.find("h1").get_text() for name in nameAndTitle][0]

        # Adds faculty title
        self.title = [title.find("h2").get_text() for title in nameAndTitle][0]

with open('scraping/output-files/profiles-links.json') as f:
    data = json.load(f)

chunks = [data[x:x+200] for x in range(0, len(data), 200)]
i = 0
for chunk in chunks:
    prof_info = []
    for prof in chunk:
        print(prof)
        t = generate_faculty_info_dict(Faculty, prof)
        prof_info.append(t)
    file_path = "scraping/output-files/prof-info-" + str(i) +".json"
    with open(file_path, "w") as f:
        json.dump(prof_info, f)
    print('chunk ', i)
    i += 1
