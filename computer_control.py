import subprocess
import webbrowser
import os

def open_application(app_name):

    app_name=app_name.lower().strip()

    # safe application for windows
    if app_name in ["calculator","calc"]:
        subprocess.Popen("calc.exe")
        return "calculator is open,Owner :)"
    elif app_name in ["notepad","editor"]:
        subprocess.Popen("notepad.exe")
        return "notepad is open,Owner :)"
    elif app_name in ["paint"]:
        subprocess.Popen("mspaint.exe")
        return "Paint is open,Owner :)"

    # ==============================
    # WEBSITES
    # ==============================

    elif app_name in ["youtube", "you tube"]:
        webbrowser.open("https://www.youtube.com")
        return "YouTube is opening, Owner."

    elif app_name in ["spotify"]:
        webbrowser.open("https://open.spotify.com")
        return "Spotify is opening, Owner."

    elif app_name in ["chatgpt", "chat gpt"]:
        webbrowser.open("https://chatgpt.com")
        return "ChatGPT is opening, Owner."
    elif app_name in ["gemini", "google gemini"]:

        webbrowser.open("https://gemini.google.com")
        return "Gemini is opening, Owner."
    elif app_name in [
        "whatsapp",
        "whatsapp web"
        ]:

        webbrowser.open(
            "https://web.whatsapp.com"
        )

        return "WhatsApp is opening, Owner."
    elif app_name in ["google"]:

        webbrowser.open(
            "https://www.google.com"
        )

        return "Google is opening, Owner."


    elif app_name in [
        "instagram",
        "insta"
         ]:
        webbrowser.open(
            "https://www.instagram.com"
        )

        return "Instagram is opening, Owner."


    elif app_name in ["facebook"]:

        webbrowser.open(
            "https://www.facebook.com"
        )

        return "Facebook is opening, Owner."
    elif app_name in [
        "gmail",
        "google mail"
    ]:

        webbrowser.open(
            "https://mail.google.com"
        )

        return "Gmail is opening, Owner."


    elif app_name in ["github"]:

        webbrowser.open(
            "https://github.com"
        )

        return "GitHub is opening, Owner."
    elif app_name in [
        "google drive",
        "drive"
         ]:

        webbrowser.open(
            "https://drive.google.com"
        )

        return "Google Drive is opening, Owner."


    # ==============================
    # CHROME
    # ==============================

    elif app_name in ["chrome", "google chrome"]:

        try:
            subprocess.Popen(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            )

        except FileNotFoundError:

            try:
                subprocess.Popen(
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                    )
            except FileNotFoundError:

                return "I couldn't find Google Chrome."

        return "Google Chrome is opening, Owner."

    return (
        "I don't have permission to open "
        f"{app_name}."
    )

def open_favorite(favorite_type, favorite):
    def search_youtube(query):

     query = query.strip()

     if not query:
        return "Owner, what should I search for?"

     search_url = (
        "https://www.youtube.com/results?search_query="
        + query.replace(" ", "+")
     )

     webbrowser.open(search_url)

     return (
        f"Searching YouTube for {query}, Owner."
     )
    def search_google(query):

     query = query.strip()

     if not query:
        return "Owner, what should I search for?"

     search_url = (
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
     )

     webbrowser.open(search_url)

     return (
        f"Searching Google for {query}, Owner."
    )

    if not favorite:
        return (
            f"Owner, I don't have your favorite "
            f"{favorite_type} saved yet."
        )

    # ----------------------------------
    # If memory returns dictionary
    # ----------------------------------

    if isinstance(favorite, dict):

        name = favorite.get(
            "name",
            f"favorite {favorite_type}"
        )

        link = favorite.get(
            "link"
        )

    # ----------------------------------
    # If memory returns direct URL
    # ----------------------------------
    elif isinstance(favorite, str):

        name = f"favorite {favorite_type}"
        link = favorite

    else:

        return (
            f"Owner, your favorite {favorite_type} "
            f"has an invalid format."
        )

    # ----------------------------------
    # Check link
    # ----------------------------------

    if not link:
        return (
            f"Owner, I found {name}, "
            f"but there is no link saved for it."
        )

    # ----------------------------------
    # Open browser
    # ----------------------------------

    try:

        webbrowser.open(link)

        return (
            f"Opening your favorite "
            f"{favorite_type}: {name}."
        )

    except Exception as error:
         print("❌ Favorite opening error:", error)

         return (
            f"Sorry Owner, I couldn't open "
            f"your favorite {favorite_type}."
        )