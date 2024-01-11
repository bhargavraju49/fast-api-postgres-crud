import copy

def generateprompts(data,template):
    for i in data:
        print(i)
    for i in template.keys():
        print(template[i])
    prompts = template.values()
    prompts_og = []
    for i1 in prompts:
        for ip in data:
            i = i1
            i = i.replace('{fst}',ip['holidays']) if '{fst}' in i else i
            i = i.replace('{sc}',ip['Bussiness Sub Category']) if '{sc}' in i else i
            i = i.replace('{n}',str(ip['Number'])) if '{n}' in i else i
            i = i.replace('{gl}',ip['Goal']) if '{gl}' in i else i
            i = i.replace('{lc}',ip['Location']) if '{lc}' in i else i
            i = i.replace('{bc}',ip['Bussiness Category']) if '{bc}' in i else i
            prompts_og.append(i)
    return list(set(prompts_og))

def flatten_dict(d):
    output_list = []
    for i in d.keys():
        if type(d[i])==type([]):
            op = []
            for j in d[i]:
                og = copy.deepcopy(output_list)
                for k in og:
                    k.update({i:j})
                for i1 in og:
                    op.append(i1)
            output_list = op
        else:
            if not output_list:
                output_list.append({i:d[i]})
            else:
                for i3 in output_list:
                    i3.update({i:d[i]})
    return output_list

# z = generateprompts([{'Bussiness Category': 'software development', 'Location': 'Hyderabad', 'Goal': 'generating leads', 'Number': 4, 'Bussiness Sub Category': 'mobile app development', 'holidays': 'New Year'}, {'Bussiness Category': 'software development', 'Location': 'Hyderabad', 'Goal': 'generating leads', 'Number': 4, 'Bussiness Sub Category': 'mobile app development', 'holidays': 'Lohri'}, {'Bussiness Category': 'software development', 'Location': 'Hyderabad', 'Goal': 'generating leads', 'Number': 4, 'Bussiness Sub Category': 'mobile app development', 'holidays': 'Pongal'}, {'Bussiness Category': 'software development', 'Location': 'Hyderabad', 'Goal': 'generating leads', 'Number': 4, 'Bussiness Sub Category': 'mobile app development', 'holidays': 'Makar Sankranti'}, {'Bussiness Category': 'software development', 'Location': 'Hyderabad', 'Goal': 'generating leads', 'Number': 4, 'Bussiness Sub Category': 'mobile app development', 'holidays': 'Republic Day'}],{
#     "Special day - Single Prompt":"Create {fst} ad for a {bc} company in {lc}. Title  should be 'Happy {fst}' only description-90 chars with a goal of {gl}.",
#     "Special day - Bach Prompt":"Create {n} {fst} ads for a {bc} company in {lc}. Title  should be 'Happy {fst}' only description-90 chars with Goal of {gl}",
#     "Techinical - Single prompts": "write a title and description with a goal of {gl} for a {bc} company focused on {sc}",
#     "Techinical - Batch Prompts":"write {n} types of a title and description with a goal of {gl} for a {bc} company focused on {sc}"
#     })
# print(z)