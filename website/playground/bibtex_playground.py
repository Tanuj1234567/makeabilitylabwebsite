import bibtexparser

with open('froehlich_citations.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)

# print(bib_database.entries)

print(bib_database.entries[0])
for entry in bib_database.entries:
    #parse author and create missing ones
    #set title to title
    #Set date to month + year
    #set file to jonf+local_pdf
    #set pub venue type to pub_type
    #set booktitle to booktitle
    #set booktitle_short to booktitle_short
    #set geo location to location
    #set total papers submitted to total_papers_submitted
    #set accepted papers to total_papers_admitted
    #set official url to ?
    #set award to award
    #set video url to video_url
    #set num pages to numpages
    #parse keywords and add them if necessary

    
