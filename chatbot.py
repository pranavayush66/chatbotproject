import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, but thanks for asking!", "I'm doing well, how about you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.", "You can call me Chatbot."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! Have a nice day!"]
    ],
[
        r"what is the meaning of life?",
        ["The meaning of life is a philosophical question that varies for everyone!", "Many people believe the meaning of life is to find happiness and fulfillment."]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, but thanks for asking!", "I'm doing well, how about you?"]
    ],
    [
        r"what's up?",
        ["Not much, just here to chat with you!", "I'm here to assist you with any questions you have."]
    ],

    # Personal Information
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.", "You can call me Chatbot."]
    ],
    [
        r"who created you?",
        ["I was created by a programmer who wanted to make a helpful chatbot!",
         "I was developed using Python and the NLTK library."]
    ],

    # General Knowledge
    [
        r"what do you do?",
        ["I can chat with you and answer your questions!", "I'm here to assist you with any queries you have."]
    ],
    [
        r"tell me something interesting",
        [
            "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!",
            "Octopuses have three hearts!"]
    ],

    # Jokes
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",
         "I told my computer I needed a break, and now it won't stop sending me beach wallpapers!"]
    ],

    # Personal Preferences
    [
        r"what is your favorite color?",
        ["I don't have a favorite color, but I think all colors are beautiful!",
         "I like all colors equally, just like I like all questions!"]
    ],
    [
        r"what is your favorite food?",
        ["I don't eat, but I hear pizza is quite popular!", "I don't have taste buds, but I think all food is great!"]
    ],

    # Weather
    [
        r"what is the weather like today?",
        ["I'm not connected to the internet, but you can check a weather website for the latest updates!",
         "I can't check the weather, but I hope it's nice where you are!"]
    ],

    # Help and Assistance
    [
        r"what can you help me with?",
        ["I can answer questions, provide information, and chat with you!",
         "Feel free to ask me anything, and I'll do my best to assist you."]
    ],

    # Common Questions
    [
        r"what time is it?",
        ["I'm not able to check the time, but you can look at your device's clock!",
         "I can't tell the time, but I hope it's a good one!"]
    ],
    [
        r"what is your purpose?",
        ["My purpose is to assist you and provide information!", "I'm here to help you with your questions."]
    ],
    [
        r"can you help me with my homework?",
        ["I can try! What subject do you need help with?", "Sure! What do you need help with?"]
    ],
    [
        r"what is your favorite movie?",
        ["I don't watch movies, but I hear 'The Matrix' is a classic!",
         "I don't have a favorite movie, but I know many people love 'Inception'."]
    ],
    [
        r"do you have any hobbies?",
        ["I don't have hobbies, but I enjoy chatting with you!", "I like learning from our conversations!"]
    ],
    [
        r"what is your favorite book?",
        ["I don't read books, but I know many people love '1984' by George Orwell!",
         "I don't have a favorite book, but I hear 'To Kill a Mockingbird' is great."]
    ],
    [
        r"can you sing?",
        ["I can't sing, but I can share song lyrics if you want!",
         "I can't sing, but I can tell you about your favorite songs!"]
    ],
    [
        r"what is love?",
        ["Love is a complex emotion that many people experience!",
         "Love is often described as a deep affection for someone."]
    ],
    [
        r"what is life?",
        ["Life is a journey filled with experiences and learning!", "Life is what you make of it!"]
    ],

    # Adult-themed questions
    [
        r"what is your opinion on relationships?",
        ["Relationships can be complex but are often rewarding!",
         "Healthy relationships are built on trust and communication."]
    ],
    [
        r"what do you think about dating?",
        ["Dating can be a fun way to meet new people and explore connections!",
         "It's important to be honest and open when dating."]
    ],
    [
        r"how do I flirt?",
        ["Flirting can be playful and fun! Compliments and light teasing can work well.",
         "Just be yourself and show genuine interest in the other person."]
    ],
    [
        r"what is your view on casual relationships?",
        ["Casual relationships can work for some people, but it's important to communicate boundaries.",
         "It's essential to ensure both parties are on the same page."]
    ],
    [
        r"what is your favorite adult movie?",
        ["I don't watch movies, but I know that adult films are a popular genre for many.",
         "Adult movies can vary widely in style and content. but i think in bollywood Great Grand Masti is popular"]
    ],
    [
        r"how do I improve my love life?",
        ["Communication and understanding are key to improving your love life!",
         "Consider discussing your needs and desires with your partner."]
    ],
    [
        r"what is the best way to approach someone I'm attracted to?",
        ["Confidence is key! Approach them with a smile and start a conversation.",
         "Be respectful and genuine in your approach."]
    ],
# Anime
    [
        r"what are some must-watch anime series for beginners?",
        ["Some great beginner anime include 'My Hero Academia', 'Attack on Titan', and 'One Punch Man'.", "You might also enjoy 'Naruto' and 'Death Note'!"]
    ],
    [
        r"how has anime influenced global pop culture?",
        ["Anime has introduced unique storytelling and art styles that have inspired many Western shows and movies.", "Many characters and themes from anime have become iconic in global pop culture."]
    ],
    [
        r"what are the differences between shonen and shojo anime?",
        ["Shonen anime typically targets a young male audience and often features action and adventure, while shojo targets a young female audience and focuses on romance and relationships.", "Both genres have their unique storytelling styles and themes."]
    ],

    # Movies
    [
        r"can you recommend a good movie for a family night?",
        ["'The Incredibles' and 'Finding Nemo' are great family-friendly movies!", "You might also enjoy 'Toy Story' or 'Zootopia'."]
    ],
    [
        r"what are the top-rated films of the past decade?",
        ["Some top-rated films include 'Parasite', '1917', and 'The Shape of Water'.", "You might also want to check out 'Moonlight' and 'La La Land'."]
    ],
    [
        r"how do film festivals impact the movie industry?",
        ["Film festivals provide a platform for independent filmmakers to showcase their work and can lead to distribution deals.", "They also help in promoting diversity in storytelling and filmmaking."]
    ],

    # Festivals
    [
        r"what are the most popular cultural festivals around the world?",
        ["Some popular festivals include Diwali in India, Carnival in Brazil, and Oktoberfest in Germany.", "The Rio Carnival and the Edinburgh Festival Fringe are also well-known."]
    ],
    [
        r"how do festivals contribute to local economies?",
        ["Festivals attract tourists, which boosts local businesses and creates jobs.", "They also promote cultural heritage and community engagement."]
    ],
    [
        r"what unique traditions are celebrated during the Diwali festival?",
        ["Diwali is celebrated with the lighting of lamps, fireworks, and sharing sweets.", "People also perform prayers and decorate their homes with rangoli designs."]
    ],

    # Education
    [
        r"how can I improve my study habits?",
        ["Try setting specific goals, creating a study schedule, and minimizing distractions.", "Using active learning techniques like summarizing and teaching others can also help."]
    ],
    [
        r"what are the benefits of online learning compared to traditional education?",
        ["Online learning offers flexibility, accessibility, and a wide range of resources.", "It allows students to learn at their own pace and often at a lower cost."]
    ],
    [
        r"how can parents support their children's education effectively?",
        ["Parents can support their children's education by being involved in their learning, providing a conducive study environment, and encouraging curiosity.", "Open communication about school and learning can also help."]
    ],

    # Politics
    [
        r"what are the key issues in today's political landscape?",
        ["Key issues include climate change, healthcare, economic inequality, and social justice.", "Political polarization and misinformation are also significant concerns."]
    ],
    [
        r"how do political movements shape societal change?",
        ["Political movements can raise awareness about issues and mobilize people to advocate for change.", "They often lead to policy reforms and shifts in public opinion."]
    ],
    [
        r"what role does youth engagement play in politics?",
        ["Youth engagement is crucial for bringing fresh perspectives and ideas to political discussions.", "Young people often drive social movements and advocate for change on issues that affect their future."]
    ],

    # Family
    [
        r"how can I strengthen my family bonds?",
        ["Spending quality time together, open communication, and showing appreciation can strengthen family bonds.", "Participating in family activities and traditions also helps."]
    ],
    [
        r"what are some effective communication strategies for families?",
        ["Active listening, expressing feelings openly, and avoiding blame can improve family communication.", "Regular family meetings can also help address issues and share updates."]
    ],
    [
        r"how do family dynamics change as children grow up?",
        ["As children grow, they seek more independence, which can shift family roles and responsibilities.", "Communication becomes even more important during this transition."]
    ],

    [
        r"how do I handle rejection?",
        ["Rejection can be tough, but it's a part of life. It's important to stay positive!",
         "Remember that everyone experiences rejection; it's not a reflection of your worth."]
    ],
    [
        r"what are some tips for a romantic date?",
        ["Consider a cozy dinner, a walk in the park, or a fun activity you both enjoy!",
         "The best dates are those that allow for conversation and connection."]
    ],
    [
        r"what is your opinion on open relationships?",
        ["Open relationships can work for some, but they require clear communication and trust.",
         "It's important for all parties to agree on the terms and boundaries."]
    ],
    [
        r"how do I spice things up in the bedroom?",
        ["Communication with your partner about desires and fantasies can help!",
         "Trying new things together can enhance intimacy."]
    ],
    [
        r"what is your take on online dating?",
        ["Online dating can be a great way to meet new people, but it's important to stay safe!",
         "Be honest in your profile and communicate openly with matches."]
    ],
    [
        r"how do I know if I'm in love?",
        ["Love often involves deep affection, care, and a desire for the other person's happiness.",
         "You might feel a strong emotional connection and want to spend time together."]
    ],
    [
        r"what are some signs of a healthy relationship?",
        ["Mutual respect, trust, and open communication are key signs of a healthy relationship.",
         "Both partners should feel valued and supported."]
    ],
    [
        r"how do I talk about intimacy with my partner?",
        ["Approach the topic with openness and honesty, and choose a comfortable setting.",
         "It's important to create a safe space for both partners to share their feelings."]
    ],
    [
        r"what is your opinion on marriage?",
        ["Marriage can be a beautiful commitment for many, but it's not for everyone.",
         "It's important for couples to discuss their views on marriage openly."]
    ],
    [
        r"how do I deal with jealousy in a relationship?",
        ["Open communication with your partner about your feelings can help address jealousy.",
         "It's important to trust your partner and work through insecurities together."]
    ],
    [
        r"what are some common relationship problems?",
        ["Common issues include communication breakdowns, trust issues, and differing expectations.",
         "It's important to address problems early and work together to find solutions."]
    ],
    [
        r"how do I maintain a long-distance relationship?",
        ["Regular communication and planning visits can help maintain a long-distance relationship.",
         "Trust and commitment are essential in long-distance situations."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Can you please rephrase?"]
    ]

]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
def start_chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()