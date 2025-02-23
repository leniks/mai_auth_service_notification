def send_welcome_email(email: str):
    # Здесь должна быть логика отправки email
    print(f"Sending welcome email to {email}")

def handle_user_registered_event(event: dict):
    if event['eventType'] == 'UserRegistered':
        send_welcome_email(event['email'])