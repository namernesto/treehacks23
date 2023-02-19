import json
import csv

with open('prof-info-0.json') as json_file:
    data = json.load(json_file)

def get_formatted_section():

full_prof_info = {}

for prof_info in data:
    formatted_prof_info = {}
    formatted_prof_info['name'] = {'texts':[prof_info.name if prof_info.name != null else ""], "weights": 1.0}
    formatted_prof_info['bio'] = {'texts':[prof_info.bio if prof_info.bio != null else ""], "weights": 1.0}

    publications = prof_info.publications
    publications_titles = []
    publications_abstract = []

    if publications != null:
        for key, val in publications.items():
            publications_titles.append(key)
            publications_abstract.append(val)

        formatted_prof_info['publications_title'] = {'texts':[sub_pub_title for sub_pub_title in publications_titles], "weights": 1.0}
        formatted_prof_info['publications_abstract'] = {'texts':[sub_pub_abstract for sub_pub_abstract in publications_abstract], "weights": 1.0}

    formatted_prof_info['title'] = {'texts':[prof_info.title if prof_info.title != null else ""], "weights": 1.0}
    formatted_prof_info['url'] = {'texts':[prof_info.url if prof_info.url != null else ""], "weights": 0.0}
    formatted_prof_info['awards'] = {'texts':[prof_info.awards if prof_info.awards != null else ""], "weights": 0.8}
    formatted_prof_info['current_research'] = {'texts':[prof_info.current_research if prof_info.current_research != null else ""], "weights": 0.8}
    formatted_prof_info['teaching'] = {'texts':[prof_info.teaching if prof_info.teaching != null else ""], "weights": 0.8}


    
cur_prof = {
    "name": {
        "texts": [
            "This is the bio section of the document.",
            "It contains information about the person's background.",
            "There may be multiple sentences in each section.",
        ],
        "weight": 2.0
    },
    "bio": {
        "texts": [
            "These are the publications listed in the document.",
            "They include papers, articles, and books.",
            "Each publication has a title, author, and publication date."
        ],
        "weight": 0.5
    },
    "publications_title": {
        "": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "publications_abstract": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "title": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "awards": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "current_research": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "teaching": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 1.0
    },
    "url": {
        "texts": [
            "This is the summary section of the document.",
            "It provides a brief overview of the main points.",
            "It is often the first section that readers will read."
        ],
        "weight": 0.0
    },
}



{"name": "Dr. Jessica Nagel", 
"bio": null, 
"publications": null, 
"title": "Clinical Assistant Professor, Psychiatry and Behavioral Sciences - Child & Adolescent Psychiatry and Child Development", 
"url": "https://profiles.stanford.edu/jessica-nagel", 
"image": "", 
"email": null, 
"awards": null, 
"current_research": null, 
"teaching": null},
{"name": "Dr. Jessica Nagel", 
"bio": null, "publications": null, 
"title": "Clinical Assistant Professor, Psychiatry and Behavioral Sciences - Child & Adolescent Psychiatry and Child Development", 
"url": "https://profiles.stanford.edu/jessica-nagel", 
"image": "", 
"email": null, 
"awards": null, 
"current_research": null, 
"teaching": null},
{"name": "Dr. Jessica Nagel", 
"bio": null, "publications": null, 
"title": "Clinical Assistant Professor, Psychiatry and Behavioral Sciences - Child & Adolescent Psychiatry and Child Development", 
"url": "https://profiles.stanford.edu/jessica-nagel", 
"image": "", 
"email": null, 
"awards": null, 
"current_research": null, 
"teaching": null}

