import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

class SpamClassifier:

    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.is_trained = False # Checa se o modelo foi treinado ou não

    def prepareData(self, url):
        df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])
        df['label'] = df['label'].map({'ham': 0, 'spam':1})
        return df['message'], df['label']
    
    def evaluatePerfomance(self, X_test, y_test):
        """
        Avalia o desempenho do modelo no conjunto de teste.
        """
        if not self.is_trained:
            print('Erro: O modelo precisa ser treinado antes de ser avaliado.')
            return

        X_test_counts = self.vectorizer.transform(X_test)
        predictions = self.model.predict(X_test_counts)
        
        accuracy = accuracy_score(y_test, predictions)
        print(f'\nAcurácia do modelo: {accuracy * 100:.2f}%')
        
        print('\nRelatório de Classificação:')
        print(classification_report(y_test, predictions, target_names=['Ham (Não-Spam)', 'Spam']))

    def train(self, data_url):
        """
        Args:
            data_url(string): A URL do dataset de treinos
        """
        X, y = self.prepareData(data_url)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        X_train_counts = self.vectorizer.fit_transform(X_train)

        self.model.fit(X_train_counts, y_train)
        self.is_trained = True
        print('Treino concluido!')

        self.evaluatePerfomance(X_test, y_test)

    def predict(self, messages):
        """
        Prevê se uma lista de novas mensagens é spam ou não.

        Args:
            messages (list): Uma lista de strings contendo as mensagens a serem classificadas.
        """
        if not self.is_trained:
            print('Erro: O modelo precisa ser treinado antes de fazer previsões.')
            return None
        
        messages_counts = self.vectorizer.transform(messages)
        
        predictions_numeric = self.model.predict(messages_counts)
        
        # Mapeia os resultados de volta para texto
        results = ["Spam" if pred == 1 else "Ham (Não-Spam)" for pred in predictions_numeric]
        return results
