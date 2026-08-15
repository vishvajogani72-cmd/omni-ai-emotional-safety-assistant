def detect_language(text):

    text = text.lower().strip()

    # Gujarati
    gujarati_words = [
        "mane", "maru", "maro", "mari",
        "shu", "kem", "che", "chhe",
        "karvu", "karavjo", "kyare",
        "kya", "tame", "tamne", "aaje",
        "kaam", "yaad", "joie"
    ]
     # Hindi
    hindi_words = [
        "mujhe", "mera", "meri", "mere",
        "kya", "kaise", "kab", "hai",
        "karna", "karni", "chahiye",
        "aaj", "kal", "yaad",
        "batao", "mujhko", "tum"
    ]
    gujarati_score=0
    hindi_score=0
    words=text.split()

    for word in gujarati_words:

        if word in words:
            gujarati_score += 1

    for word in hindi_words:

        if word in words:
            hindi_score += 1

    if gujarati_score > hindi_score and gujarati_score > 0:

            return "gujarati"

    if hindi_score > gujarati_score and hindi_score > 0:
            
            return "hindi"

    return "english"