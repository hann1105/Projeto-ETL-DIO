import pandas as pd

# Simulando extração de dados devido à indisponibilidade da API

users=[{'id':1,'name':'Paola','news':[]},
       {'id':2, 'name':'Lucas','news':[]},
       {'id':3, 'name':'João','news':[]},
       {'id':4,'name':'Maria','news':[]},
       {'id':5,'name':'Heitor','news':[]}]

# =========================
# TRANSFORM
# =========================
# Geração de mensagens de marketing

def generate_news(user):
    return f"{user['name']}, investir hoje é garantir um futuro financeiro mais seguro!"

for user in users:
    news = generate_news(user)
    user['news'].append({
        "icon": "credit.svg",
        "description": news
    })

# =========================
# LOAD (opção 2 - CSV)
# =========================

rows = []
for user in users:
    for news in user['news']:
        rows.append({
            "id": user['id'],
            "name": user['name'],
            "news": news['description']
        })

df = pd.DataFrame(rows)
df.to_csv("users_with_news.csv", index=False)