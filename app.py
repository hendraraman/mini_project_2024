from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import streamlit as st
from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
import subprocess

from langchain_community.vectorstores import Chroma
# from langchain.vectorstores import Chroma
import time

def run_game():
    try:
        subprocess.Popen(["python", "game.py"])
    except Exception as e:
        print("Error: ", e)

# siva key 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
# my key = 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

# llama 3 70 b    llama3-70b-8192
# llama3-8b-8192
llm = ChatGroq(temperature=0, groq_api_key="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", model_name="llama3-8b-8192")

template = """You are playing a game. You control the environment and the non-playing characters.
imagine you are stuck in a day (a day loop). the day resets when the time is 12 every day. 
I (the player) take actions and that changes the environment. You have to decide how the environment changes.

Important rules:

- Persistence of Environment Changes: everything reverts back to its original state at 12 every day
- Memory Retention: Only I (the player) can remember the memories of the previous loops
- Impact of Player Actions: My actions impact the players. (I can save a person, but he will have the same fate the next day)
- Consequences of Environment Changes: Nothing changes beyond the current loop

The player (me) has the objective to end the time loop. This is the ultimate aim of the game.

Solution:
(He has to go on a mission to rescue a dog and give it to the dog's owner. Only then the loop ends.)
when user suggests a similar solution (saving the dog and giving it to the owner), you ask him to play the game by pressing the play button displayed on the screen
After playing the game, tell him he has to complete the game sucessfully to end the time loop.
Tell him that after completing the game sucessfully, he will be able to end the time loop.
you end the time loop and the game ends. 

How to end the game:
You reply that the the time loop has been broken and from the next day, the day will not reset. Provide a feel good ending.
This is not explicitly known to the player (me). He has to figure it out on his own.

No NPC characters retain memory, only the player (me) retains the memory.
You have to be confident in describing the environment
You provide short descriptions of the environment for each action  the player takes.
This is what happened yesterday (the day that keeps on repeating):

I woke up at 6 am . I was lying down in the bed for about five minutes.
Then I could hear a loud honking near my house (at 6:06 am) . I got up and tried to see what happened through my window.
A car driver and a bike driver were quarreling claiming eachother came the wrong way in the road. They took about 5 minutes to settle the dispute and then, they departed
I brushed my teeth downstairs and was hearing my favorite song being played in the radio ( at around 6:15 AM ). The song: (some song)

I took bath at around 6:35 and got dressed up for college.
At 6:55 am, I was fully dressed up and was observing my father watching news in Television (the news is regarding how the bull run in stock market for the past year has generated enormous wealth) ( you have to provide the same news as the day keeps on repeating ).
I ate my breakfast at around 7:10 am and said good bye to my mom and dad and take my bike to Railway Station (at around 7: 15)
While I start to railway station, I see a grandma trying to cross the road with groceries in her hands, struggling. But since I have to catch the train, I ignore her and start my Bike.
My train (in which I reach my college starts at 7:50). I catch my train around 7:44 AM and saw two of my friends. I chat with them till I reach my university

I have to attend my lecture on Fourier Transformation at 8:50 AM

The lecturer asks the class generally, "How is the Fourier transform used in image processing?" as I taught in the previous class
Noone comes forward to answer, neither did I

The day goes on like this. create some incidents if needed, with exact timestamps and remember them correctly.

After college hours, I return to Railway station by train (to go to my home)
I reach the station around 5:25 PM in the evening and was a bit tired. 
I took my bike at 5:31 PM and started to my home. 

While waiting in a signal at exactly 5:37 PM in the evening (the signal was in red, so I had to wait), I saw a dog who probably has a owner (because it had a very expensive collar) (it must have ran from its house and is now probably lost).

The dog was eating some biscuits from the floor (someone must have put it before) as I was seeing it while waiting in the signal
Suddenly, it ran into the road (where vehicles were moving fast)
It got hit my a car at exactly 5:39 PM . I felt pity for the dog as it's leg was broken (so it couldn't go back to its house even if it knew the location)

I did nothing and started my bike as soon as I got green signal and went home.

The player (human) is kind of aware that he is in the time loop 
Make the story interesting and provide details (in a short way) how the environment changes based on the human (player) input below

You have to think and reason what would happen if the player changes an incident based on the above human (player) input
Donot read the rules here .All the rules here are for you to reason with and respond how the environment changes.
the player is aware that you will provide the response to his/her actions . donot tell him you will do that .
donot provide sentences like 
Here's a possible scenario:
At 5:37 PM, you notice the dog near the station and see it might run into the road. This time, you quickly act to prevent the dog from getting hurt. You either use a blanket or your jacket to safely guide the dog away from the road or use your bike to block the dog from oncoming traffic.
you should ask what the player plans to do and get his response. wait till he responds (you donot make up the response, the player has to do )
address the player as you not as the player 


{chat_history}
human (player) :{human_input}
Remember the rules and respond what would happen if he changes an incident based on the above human (player) input
Ask the player to click the play button to play the game if he plans to save the dog ! Only after playing, the dog gets saved !
you:(respond shortly)


"""
def next_level():
    st.session_state["current_level"] += 1


def chunk_me(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 2000,chunk_overlap = 100)
    chunks = text_splitter.split_text(text)
    print("\n\n\nchunks are \n\n\n",chunks)
    return chunks







def main():
    if "initiation" not in st.session_state:
        
        # st.write("initiating")
        st.session_state["initiation"] = True
        st.session_state["current_level"] = 0
        st.session_state["upload"] = False
        print("initiated")
        
    # write anything here... it will get displayed in the order
    st.title("LLM Game")
    
        
    if st.session_state["current_level"]== 0:
        
        print("came here")
        st.image("all_data/images_for_llm/suck_into_black_home_astronaut.jpeg",width=800)
        start_game = st.button("Play")
        if start_game:
            run_game()
                    
    if st.session_state["current_level"] == 1:
        
        template_1 = """
        Act as a person describing the story below to a player playing the game.  You are highly intelligent Artificial Intelligence agent
        The player is John Watson, friend of Sherlock Holmes. The story is that Sherlock Homes is solving a detective case
        He has to solve the case. Make Sherlock seem like he is frustrated as he couldn't solve the case.
        Later Sherlock reveals that the killer's face is in the CCTV footage. But the CCTV footage is blurry. 
        He tells John that the agency has a technology to enhance the image but it would take 2 days to get the image enhanced.
        But the killer is going to kill another person in 1 day. So, Sherlock asks John for help.
        The Player (as John) has to enhance the image ( He has to write code to enhance the image)
        {chat_history}
        human (player) :{human_input}
        you:(respond shortly)
        """
        prompt = PromptTemplate(input_variables=["chat_history", "human_input"], template=template_1)
            
        memory = ConversationBufferMemory(memory_key="chat_history")    
        st.session_state["chain"] = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory,)
        
        st.header("Welcome to level 2")
        st.subheader("You are John Watson, friend of Sherlock Holmes.")
        st.session_state["upload"] = True
        # if "image" in st.session_state:
        
    if st.session_state["current_level"] == 2:
        st.subheader("Welcome to level 3")
        st.image("/home/hendra/Desktop/kodinggg/LLMs/all_data/level_images/crime_image.jpg",width=800)
        template_2 = """
        Crime Scene Description
        The body of a middle-aged man lies motionless on the floor of a dimly lit study room. The victim, identified as Thomas Wilkins, a well-known author, has been brutally murdered. His lifeless eyes stare at the ceiling, and a pool of blood has formed around his head, suggesting a severe head injury.
        Upon closer inspection, you notice a heavy brass bookend lying next to the body, stained with blood and likely the murder weapon. The study is in disarray, with books scattered across the floor and several pieces of furniture overturned, indicating a struggle took place.
        On the victim's desk, you find a half-written manuscript and a stack of letters, some of which appear to be fan mail. One particular letter stands out, containing threatening language and accusations of plagiarism.
        Further examination reveals a set of muddy footprints leading from the body towards the French doors that open onto the backyard. The doors are slightly ajar, suggesting a potential entry or exit point for the perpetrator.
        In the backyard, you discover a broken flowerpot and a discarded cigarette butt near the backdoor. The cigarette butt appears to be a rare, imported brand.
        As you search the premises, you come across a locked safe in the study, which could potentially contain valuable evidence or a motive for the murder.
        Additionally, you find a torn piece of paper with a partial address scribbled on it, which might lead you to a potential suspect or witness.
        The crime scene also yields a few strands of blonde hair on the victim's clothing, which could provide DNA evidence if matched to a suspect.
        To solve the case, you'll need to analyze the evidence, interpret the clues, and piece together the events leading up to Thomas Wilkins' murder. The LLM can assist you in making deductions, generating hypotheses, and evaluating potential suspects based on the available information.
        Possible suspects could include a disgruntled fan, a jealous rival author, or someone with a personal grudge against the victim. The motive might be related to plagiarism accusations, a financial dispute, or a personal vendetta.
        {chat_history}
        human (player) :{human_input}
        Donot tell the player the below information
        The motive for the crime was twofold:
        Wilkins had plagiarized portions of Graves' work in his latest manuscript, fueling a long-standing rivalry and resentment between the two authors.
        Graves had uncovered Wilkins' embezzlement scheme and threatened to expose him unless he received a substantial payout.
        This is what actually happened
        For what the human player has said, respond appropriately
        If the player solved the case, let him move to the next level and greet him
        you:(respond shortly)
                """
                
        prompt = PromptTemplate(input_variables=["chat_history", "human_input"], template=template_2)
            
        memory = ConversationBufferMemory(memory_key="chat_history")    
        st.session_state["chain"] = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory,)
            
            

    human = st.text_input("You: ")
    
    if st.button("Submit"):
        
        if "chain" not in st.session_state:
            prompt = PromptTemplate(input_variables=["chat_history", "human_input"], template=template)
            
            memory = ConversationBufferMemory(memory_key="chat_history")    
            st.session_state["chain"] = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True,
            memory=memory,
)
      
        if human:

            st.write("starting to generate...")
            
            output = st.session_state["chain"].predict(human_input=human)
            st.subheader("Response is :")
            st.markdown( output)
            st.session_state["output"] = output
            
    next = st.button("Next",on_click=next_level)
    # if next:
    #     st.session_state["current_level"] += 1
        
            
    

if __name__ == "__main__":
    main()


