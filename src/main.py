from models.SpamClassifier import SpamClassifier

if __name__ == "__main__":

    dataset_url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"

    classifier = SpamClassifier()

    classifier.train(dataset_url)

    # Testa com novas mensagens
    new_messages_to_test = [
        "Congratulations! You've won a $1,000 Walmart gift card. Go to http://bit.ly/1234 to claim now.",
        "Hey, are you free for lunch tomorrow?",
        "URGENT: Your account has been suspended. Please log in to reactivate.",
        "Obrigado pelo seu email, retornaremos em breve."
    ]

    predictions = classifier.predict(new_messages_to_test)
    
    if predictions:
        for message, prediction in zip(new_messages_to_test, predictions):
            print(f'Mensagem: "{message}"\nPrevisão: {prediction}\n')