# Project2 - Develope a Chatbot which gives answers of a specific quetions

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faqs = {
    "Hi" : "Hey There!",
    "What is your name?" : "I am Miski a chatbot.",
    "How does this work?" : "You ask questions and I provide answers.",
    "Hey,Tell me about google": "Google was founded on September 4, 1998, by American computer scientists Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together, they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet..",
    "You konw chatgpt?" : "ChatGPT is a chatbot and virtual assistant developed by OpenAI and launched on November 30, 2022. Based on large language models (LLMs), it enables users to refine and steer a conversation towards a desired length, format, style, level of detail, and language. Successive user prompts and replies are considered at each conversation stage as context.",
    "Thank You Miski" : "My Pleasure",
    "Ok bye" : "Bye!!! Have a nice day"
   }

# Preprocessing
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return " ".join(tokens)

# Vectorization
corpus = [preprocess(question) for question in faqs.keys()]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Model
def get_response(query):
    query = preprocess(query)
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec,X)
    idx = similarities.argmax()
    return list(faqs.values())[idx]

# Chat Interface
print("Welcome! Ask me anything related to Any topic. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = get_response(user_input)
    print("Bot:",response)
    
   