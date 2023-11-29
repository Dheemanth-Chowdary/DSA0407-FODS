import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

# Download NLTK resources (if not already downloaded)
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def calculate_word_frequency(reviews):
    # Tokenize the reviews into words
    words = [word.lower() for review in reviews for word in word_tokenize(review)]

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    filtered_words = [word for word in words if word not in stop_words]

    # Calculate word frequency distribution
    freq_dist = FreqDist(filtered_words)

    return freq_dist

if __name__ == "__main__":
    # Assuming you have a dataset with a 'Reviews' column
    # Load your dataset into a DataFrame
    # df = pd.read_csv('your_dataset.csv')

    # Example DataFrame structure:
    df = pd.DataFrame({
        'Reviews': ['The product is great!', 'Not satisfied with the quality.', 'Amazing product and service.']
    })

    # Calculate word frequency distribution
    reviews = df['Reviews'].tolist()
    word_frequency = calculate_word_frequency(reviews)

    # Display the top 10 most frequent words
    print("Top 10 Most Frequent Words:")
    for word, frequency in word_frequency.most_common(10):
        print(f"{word}: {frequency}")
