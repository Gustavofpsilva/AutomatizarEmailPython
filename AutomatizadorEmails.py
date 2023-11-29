import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import getpass

class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email

    def enviar_email(self, destinatario, assunto, corpo, anexos=None):
        mensagem = MIMEMultipart()
        mensagem['From'] = self.sender_email
        mensagem['To'] = destinatario
        mensagem['Subject'] = assunto

        # Adicionar corpo à mensagem
        mensagem.attach(MIMEText(corpo, 'plain'))

        # Adicionar anexos, se fornecidos
        if anexos:
            for anexo in anexos:
                with open(anexo, 'rb') as arquivo_anexo:
                    anexo_mime = MIMEApplication(arquivo_anexo.read())
                    anexo_mime.add_header('Content-Disposition', f'attachment; filename={anexo}')
                    mensagem.attach(anexo_mime)

        try:
            senha = getpass.getpass(prompt='Digite a senha do seu e-mail: ')
            servidor = smtplib.SMTP(self.smtp_server, self.smtp_port)
            servidor.starttls()
            servidor.login(self.sender_email, senha)

            # Enviar a mensagem
            servidor.sendmail(self.sender_email, destinatario, mensagem.as_string())
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
        finally:
            # Encerrar a conexão com o servidor SMTP
            servidor.quit()

def main():
    # Substitua com suas informações de e-mail
    meu_smtp_server = "smtp.gmail.com"
    meu_smtp_port = 587
    meu_email = "seu_email@gmail.com"

    # Criar uma instância do EmailSender
    sender = EmailSender(meu_smtp_server, meu_smtp_port, meu_email)

    destinatario = "destinatario@example.com"
    assunto = "Assunto do E-mail"
    corpo = "Corpo do E-mail"
    anexos = ["arquivo1.txt", "arquivo2.pdf"]  # Substitua com os caminhos reais dos anexos

    sender.enviar_email(destinatario, assunto, corpo, anexos)

if __name__ == "__main__":
    main()
