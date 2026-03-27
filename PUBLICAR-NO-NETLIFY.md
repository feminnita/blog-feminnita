# Como publicar o Blog Feminnita no Netlify

Siga este passo a passo uma única vez. Depois disso, editar artigos é só entrar em `/admin`.

---

## Passo 1 — Criar repositório no GitHub

1. Acesse [github.com](https://github.com) e crie uma conta gratuita (se não tiver)
2. Clique em **New repository**
3. Nome: `blog-feminnita`
4. Marque **Private** (opcional, mas recomendado)
5. Clique em **Create repository**
6. Suba os arquivos desta pasta para o repositório

---

## Passo 2 — Conectar ao Netlify

1. Acesse [netlify.com](https://netlify.com) e crie uma conta gratuita
2. Clique em **Add new site → Import an existing project**
3. Selecione **GitHub** e autorize o acesso
4. Escolha o repositório `blog-feminnita`
5. Configurações de build:
   - **Build command**: `npm run build`
   - **Publish directory**: `_site`
6. Clique em **Deploy site**

O site será publicado automaticamente em um endereço tipo `feminnita-blog.netlify.app`.

---

## Passo 3 — Ativar Netlify Identity (login do admin)

1. No painel do Netlify, vá em **Site configuration → Identity**
2. Clique em **Enable Identity**
3. Em **Registration**: selecione **Invite only** (só você terá acesso)
4. Em **Services → Git Gateway**: clique em **Enable Git Gateway**
5. Vá em **Identity → Invite users** e insira o seu e-mail
6. Você receberá um e-mail de convite — clique no link e defina a senha

---

## Passo 4 — Acessar o painel de edição

1. Acesse `https://seu-site.netlify.app/admin`
2. Faça login com o e-mail e senha que você criou
3. Clique em **Artigos** para editar ou criar artigos

Cada artigo salvo no CMS gera automaticamente um commit no GitHub e o Netlify publica a atualização em 1–2 minutos.

---

## Domínio personalizado (opcional)

Para usar `blog.feminnita.com.br`:

1. No Netlify: **Domain management → Add domain**
2. Digite `blog.feminnita.com.br`
3. No painel do seu provedor DNS (onde o domínio feminnita.com.br está registrado):
   - Adicione um registro CNAME apontando `blog` para o endereço do Netlify
4. O SSL (https://) é ativado automaticamente pelo Netlify

---

## Resumo do fluxo de edição

```
Você entra em /admin
    → Faz login com e-mail e senha
    → Edita ou cria um artigo
    → Clica em Publicar
    → O Netlify reconstrói o site automaticamente
    → Em ~2 minutos o artigo aparece no blog
```
