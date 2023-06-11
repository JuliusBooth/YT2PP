import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv('OPEN_AI_KEY')

def fill_prompt_template(lecture_text):
    return f"""Please succinctly summarize the lecture below, delimited by triple backticks, into powerpoint slides. The output should be in json format with each slide having a title, bullets, image, and a slide color. Here is an example
    Lecture:
    Good afternoon everyone,
I'm delighted to have this opportunity to talk about a topic that's close to many of our hearts — and stomachs. Today, we're going to talk about pizza. Yes, that universally loved dish that comes in a million different varieties and has won over palates across the globe. We'll explore its history, the science behind it, and the incredible diversity in this culinary masterpiece.
Let's start with a brief history. Pizza, as we know it, originated in Naples, Italy, in the late 18th century. The Neapolitans were renowned for their "flatbreads with toppings", a simple and cheap meal for the working class. The classic Margherita pizza was said to be invented in 1889 by Raffaele Esposito, in honor of the visiting Queen Margherita. Its colors represented the Italian flag: red tomatoes, white mozzarella, and green basil. From there, pizza took a journey around the world, becoming the versatile dish we know and love today.
Moving onto the science behind pizza, let's consider what makes pizza so delicious. There's a concept in food science called the Maillard reaction. This is a chemical reaction between amino acids and reducing sugars that gives browned food its distinctive flavor. When you put a pizza in a hot oven, this reaction occurs, creating complex flavors and enticing aromas. The high heat of a pizza oven also leads to rapid water evaporation, giving the crust its lovely crispiness. The gooey goodness of melted cheese? That's due to the proteins and fats breaking down and reorganizing, leading to a wonderful molten delight.
Now, onto the diversity of pizza. From thin, crisp Neapolitan pizza, to the deep-dish style from Chicago, to the unique toppings of Japanese pizza like mayonnaise and squid, pizza knows no boundaries. It has transformed to suit local tastes wherever it has traveled. Just consider New York-style pizza, with its large, foldable slices and classic toppings like pepperoni and mushrooms. Or the pizza bianca, a sauceless pizza topped with just olive oil, rosemary, and sea salt. Each variation has its own charm and follows its own traditions, contributing to the global pizza tapestry.
In conclusion, pizza is not just a food item, but a cultural phenomenon, representing centuries of culinary history and the union of science and gastronomy. Its universal appeal and adaptability make it one of the most loved dishes around the world. Whether you're a fan of the classic Margherita, the deep-dish Chicago, or an avant-garde fusion creation, remember, every pizza you enjoy is a slice of history.
Thank you for your time, and remember, the perfect pizza is only limited by your imagination!

Output:[{{"Title": “The History of Pizza”, "Bullets": [“Originated in Naples, Italy, in the late 18th century”, “Margherita pizza was reportedly invented in 1889 by Raffaele Esposito, representing the colors of the Italian flag: red (tomatoes), white (mozzarella), and green (basil)”, “Pizza transformed as it spread worldwide, becoming a versatile and universally loved dish“], "Image": "Italian Flag", “Slide Color”:(201, 120, 76)}} ,{{"Title": “Pizza Chemistry”, “Bullets”: [“The Maillard reaction: A chemical reaction between amino acids and reducing sugars that gives browned food its flavor. This reaction happens when pizza is baked, creating its enticing aroma and taste.”, ”Rapid water evaporation in high heat results in the crust's characteristic crispiness”, ”Melting cheese leads to proteins and fats breaking down and reorganizing, creating a delightful gooey texture“], "Image": "Chemistry", “Slide Color”:(45, 255, 215)}}, {{“Title”: “Pizza Today“, “Bullets”: [“Pizza variations range from thin, crisp Neapolitan to deep-dish Chicago style, and beyond”, “Unique toppings and styles adapt to local tastes around the globe, like New York-style pizza with large, foldable slices, or Japanese pizza featuring unconventional toppings like mayonnaise and squid”, “Every style contributes to the global pizza tapestry, embodying centuries of culinary history and the union of science and gastronomy.”], "Image": "Pizza", “Slide Color”: (188, 255, 212)}}]

```{lecture_text}```
Output:"""

def prompt_chat_gpt(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "%s" % prompt}
        ]
    )
    return response['choices'][0]['message']['content']
    
def get_lecture_bullets(lecture_text):
    prompt = fill_prompt_template(lecture_text)
    print(prompt)
    lecture_bullets_respone = prompt_chat_gpt(prompt)
    #convert curly quotes to straight quotes
    lecture_bullets_respone = lecture_bullets_respone.replace('“', '"').replace('”', '"')
    # lecture_bullets_respone will be a string of a list of lists, so we need to convert it to a list of lists
    lecture_bullets = eval(lecture_bullets_respone)
    print(lecture_bullets)
    return lecture_bullets