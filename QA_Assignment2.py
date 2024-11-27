def findTotalArticlesByLanguages(languages, data):

    total_articles = 0
    for lang in languages:
        if lang in data:
            total_articles += data[lang]
        else:
            print(f"Language {lang} not found in the data.")
    return total_articles


wikipedia_data = {
    "English": 6562386,
    "German": 2733833,
    "French": 2441600,
    "Japanese": 1325200,
    "Russian": 1824300,
    "Japanese": 1325200,
    "Russian": 1824300,

}


languages = ["English", "German"]
total_articles = findTotalArticlesByLanguages(languages, wikipedia_data)
print(f"Total articles for {languages}: {total_articles}")
