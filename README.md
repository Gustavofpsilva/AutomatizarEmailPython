EmailSender - Enviador de E-mails em Python
Este script Python fornece uma classe EmailSender para facilitar o envio de e-mails usando o protocolo SMTP. Ele utiliza a biblioteca smtplib e os módulos email.mime para criar e enviar mensagens de e-mail, além de suportar anexos.

Pré-requisitos
Python 3.x
Uma conta de e-mail com suporte ao protocolo SMTP
Permissões de acesso à conta de e-mail (se necessário)
Como Usar
Configuração Inicial:

Substitua as seguintes variáveis no código com suas próprias informações de e-mail:

meu_smtp_server: O servidor SMTP do seu provedor de e-mail.
meu_smtp_port: A porta SMTP a ser usada (normalmente 587 para STARTTLS).
meu_email: Seu endereço de e-mail.
Execução:

Execute o script e forneça a senha quando solicitado. O script enviará um e-mail com o corpo especificado, o assunto fornecido e os anexos, se fornecidos.

bash
Copy code
python seu_script.py
Detalhes da Classe EmailSender
A classe EmailSender possui os seguintes métodos principais:

__init__(self, smtp_server, smtp_port, sender_email): Inicializa a instância com as configurações do servidor SMTP e o endereço de e-mail do remetente.

enviar_email(self, destinatario, assunto, corpo, anexos=None): Envia um e-mail para o destinatário especificado com o assunto, corpo e anexos (opcional).

Exemplo de Uso
python
Copy code
# Criar uma instância do EmailSender
sender = EmailSender(meu_smtp_server, meu_smtp_port, meu_email)

# Definir detalhes do e-mail
destinatario = "destinatario@example.com"
assunto = "Assunto do E-mail"
corpo = "Corpo do E-mail"
anexos = ["arquivo1.txt", "arquivo2.pdf"]  # Substitua com os caminhos reais dos anexos

# Enviar o e-mail
sender.enviar_email(destinatario, assunto, corpo, anexos)
Notas Importantes
Segurança: Evite armazenar senhas diretamente no código. O script usa a biblioteca getpass para solicitar a senha durante a execução.

Gmail: Se estiver usando o Gmail, certifique-se de permitir o acesso de aplicativos menos seguros nas configurações da sua conta.

Adaptação: Adapte o código conforme necessário para atender aos requisitos específicos do seu projeto.
