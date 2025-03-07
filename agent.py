import os
import openai
import git

# Opsæt OpenAI API-nøgle
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Funktion til at generere kode
def generate_code(prompt):
    response = client.chat.completions.create(
        model='gpt-4',
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0.5,
    )
    return response.choices[0].message.content

# Generer en simpel React-komponent
code = generate_code('Lav en simpel React-komponent for en login-formular')

# Opret fil med genereret kode
file_path = 'generated/LoginForm.js'
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, 'w') as f:
    f.write(code)

print(f'✅ Fil oprettet: {file_path}')

# Commit og push til GitHub
repo = git.Repo('.')
repo.git.add(A=True)
repo.index.commit('Auto-genereret React komponent: LoginForm')
repo.remote().push()
print('🚀 Kode pushet til GitHub!')
