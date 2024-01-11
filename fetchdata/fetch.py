from datetime import datetime
def getpromptstemplate():
    #fetch from apis later
    resp = {
    "Special day - Single Prompt":"Create {fst} ad for a {bc} company in {lc}. Title  should be 'Happy {fst}' only description-90 chars with a goal of {gl}.",
    "Special day - Bach Prompt":"Create {n} {fst} ads for a {bc} company in {lc}. Title  should be 'Happy {fst}' only description-90 chars with Goal of {gl}",
    "Techinical - Single prompts": "write a title and description with a goal of {gl} for a {bc} company focused on {sc}",
    "Techinical - Batch Prompts":"write {n} types of a title and description with a goal of {gl} for a {bc} company focused on {sc}"
    }
    return resp

def getfestivals(location):
    current_date = datetime.now()
    current_month = current_date.month
    print(location,current_month)
    resp = {"holidays":["New Year","Lohri","Pongal","Makar Sankranti","Republic Day"]}
    return resp