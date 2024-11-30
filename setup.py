import json

def place(list_dic,):
    file = './webhooks/config.go'
    tmp = ""
    for dic in list_dic:
        hooks = r'''    {
        		Name: "var_name",
        		URL:  "var_URL",
       	},
'''
        hooks = hooks.replace("var_name",dic.get('name'))
        hooks = hooks.replace("var_URL",dic.get('URL'))
        tmp += hooks

    with open(file) as r:
        config = r.read()
        config = config.replace("var_webhooks",tmp)
    with open(file,'w') as w:
        print(config)
        w.write(config)

place(json.load(open('hooks.json')))

