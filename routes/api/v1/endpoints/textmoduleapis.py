from fastapi import APIRouter
from typing import Dict, Any
from fetchdata.fetch import getpromptstemplate, getfestivals
from modules.Textmodule.generateprompts import flatten_dict, generateprompts
tm_router = APIRouter()

@tm_router.post("/getprompts")
async def get_prompts(data: Dict[str, Any]):
    template = getpromptstemplate()
    festivals = getfestivals(data['Location'])
    data.update(festivals)
    ptemp = flatten_dict(data)
    print(ptemp)
    # print(template)
    prompts = generateprompts(ptemp,template)
    # print(prompts)
    res = {}
    for i in range(len(prompts)):
        res[i] = prompts[i]
    return res