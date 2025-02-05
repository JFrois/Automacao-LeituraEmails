
  <h1>Automação de Leitura de E-mails</h1>
    <p>Este projeto consiste em uma automação para leitura de e-mails utilizando Python e a biblioteca <code>imbox</code>. Ele se conecta à conta de e-mail e marca as mensagens não lidas como lidas.</p>
        <h2>📌 Tecnologias Utilizadas</h2>
    <ul>
        <li>Python</li>
        <li>Google Colab</li>
        <li>Imbox (para acessar a caixa de entrada via IMAP)</li>
    </ul>
    
<h2>🚀 Instalação</h2>
    <p>Para utilizar este projeto, siga os passos abaixo:</p>
    <ol>
        <li>Clone este repositório:</li>
        <pre><code>git clone https://github.com/seu-usuario/seu-repositorio.git</code></pre>
        <li>Instale as dependências necessárias:</li>
        <pre><code>pip install imbox</code></pre>
    </ol>      
<h2>⚙️ Configuração</h2>
<p>Edite o script e insira seu e-mail e senha no código:</p>
    <pre><code>
    host = 'imap.gmail.com' # Servidor IMAP
    email = ['seuemail']
    password = ['suasenha']
    </code></pre>
    <p><strong>Atenção:</strong> Recomenda-se o uso de variáveis de ambiente para armazenar credenciais com segurança.</p>
<h2>📌 Como Usar</h2>
    <p>Execute o script para conectar ao e-mail e marcar mensagens não lidas como lidas.</p>
    <pre><code>
    with Imbox(host, username=email[0], password=password[0]) as imbox:
        if unread_messages := imbox.messages(unread=True):
            for uid, msg in unread_messages:
                imbox.mark_seen(uid)
    </code></pre>
<h2>🎥 Demonstração</h2>

[screen-capture.webm](https://github.com/user-attachments/assets/997d8240-06cd-4a95-a746-0dc1fa9fd185)


