import pandas as pd

# =========================
# EXTRACT
# =========================

alunos = [
    {'id': 1, 'nome': 'Paola', 'nota': 10, 'mensagem': []},
    {'id': 2, 'nome': 'Lucas', 'nota': 9, 'mensagem': []},
    {'id': 3, 'nome': 'João', 'nota': 8.5, 'mensagem': []},
    {'id': 4, 'nome': 'Maria', 'nota': 6, 'mensagem': []},
    {'id': 5, 'nome': 'Heitor', 'nota': 7, 'mensagem': []}
]

# =========================
# TRANSFORM
# =========================

def gerar_mensagem(aluno):
    if aluno['nota'] < 7:
        return f"{aluno['nome']}, você não passou. Está em recuperação."
    elif aluno['nota'] < 8:
        return f"{aluno['nome']}, você passou, mas pode melhorar sua nota."
    else:
        return f"{aluno['nome']}, parabéns! Você passou com ótimo desempenho."

for aluno in alunos:
    mensagem = gerar_mensagem(aluno)
    aluno['mensagem'].append({
        "descricao": mensagem
    })

# =========================
# LOAD
# =========================

linhas = []
for aluno in alunos:
    for msg in aluno['mensagem']:
        linhas.append({
            "ID": aluno['id'],
            "Nome": aluno['nome'],
            "Nota": aluno['nota'],
            "Mensagem": msg['descricao']
        })

df = pd.DataFrame(linhas)
df.to_csv("Alunos_mensagem.csv", index=False)

print("ETL finalizado com sucesso! Arquivo 'Alunos_mensagem.csv' gerado.")
