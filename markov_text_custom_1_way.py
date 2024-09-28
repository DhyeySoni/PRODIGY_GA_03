import random
from collections import defaultdict

# Define the training text first
training_text = """hi dhyey

this is line one

you got here by markov!!!

what you can do

Avengers: Endgame is a 2019 American superhero film based on the Marvel Comics 
superhero team the Avengers. Produced by Marvel Studios and distributed by Walt
 Disney Studios Motion Pictures, it is the direct sequel to Avengers: Infinity War
  (2018) and the 22nd film in the Marvel Cinematic Universe (MCU). Directed by Anthony 
  and Joe Russo and written by Christopher Markus and Stephen McFeely, the film features
   an ensemble cast which includes Robert Downey Jr., Chris Evans, Mark Ruffalo,
    Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Don Cheadle, Paul Rudd, 
    Brie Larson, Karen Gillan, Danai Gurira, Benedict Wong, Jon Favreau, Bradley Cooper,
     Gwyneth Paltrow, and Josh Brolin. In the film, the surviving members of the Avengers
      and their allies attempt to reverse Thanos's actions in Infinity War which erased 
      half of all life in the universe.

The film was announced in October 2014 as Avengers: Infinity War – Part 2, 
but Marvel Studios later removed this title. The Russo brothers joined as 
directors in April 2015, with Markus and McFeely signing on to write the 
script a month later. It is a conclusion to the story of the MCU up to that
 point, ending the story arcs of several main characters. The film's plot 
 revisits several moments from earlier films, bringing back actors and settings
  from throughout the franchise. Filming began in August 2017 at Pinewood Atlanta 
  Studios in Fayette County, Georgia, shooting back-to-back with Infinity War, and
   ended in January 2018. Additional filming took place in the Metro and downtown
    Atlanta areas, New York State, Scotland, and England. The official title was 
    announced in December 2018. With an estimated budget of $356–400 million, the
     film is one of the most expensive films ever produced.

Avengers: Endgame premiered at the Los Angeles Convention Center on April 22,
 2019, and was released in the United States on April 26 as part of Phase 
 Three of the MCU. The film received praise for its direction, acting, musical 
 score, action scenes, visual effects, and emotional weight, with critics
  lauding its culmination of the 22-film story. It grossed $2.799 billion
   worldwide, surpassing Infinity War's entire theatrical run in eleven days
    and setting a number of box-office records; it was the highest-grossing
     film of all time from July 2019 to March 2021. The film was nominated 
     for Best Visual Effects at the 92nd Academy Awards, among numerous other
      accolades. Two further films, Avengers: Doomsday and Avengers: Secret Wars, 
      are scheduled for release in 2026 and 2027, respectively.

Plot
In 2018, 23 days after Thanos erased half of all life in the universe,[a]
 Carol Danvers rescues Tony Stark and Nebula from deep space. They reunite
  with the remaining Avengers—Bruce Banner, Steve Rogers, Thor, Natasha Romanoff,
   and James Rhodes—and Rocket on Earth. Locating Thanos on an uninhabited planet,
    they plan to use the Infinity Stones to reverse his actions but find that Thanos
     has destroyed them. Enraged, Thor decapitates Thanos.


"""

# Function to build the Markov chain model


def build_markov_chain(text, n=1):
    words = text.split()
    markov_chain = defaultdict(list)

    # Loop through the words and create the chain
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])  # Create a tuple for the current state
        next_word = words[i+n]     # The next word in the sequence
        markov_chain[key].append(next_word)

    return markov_chain


# Create a Markov chain with word sequences of length 1 (unigram model)
markov_chain = build_markov_chain(training_text)

# Function to generate text based on the Markov chain model


def generate_text(markov_chain, start_word, length=20):
    current_state = start_word
    output = list(current_state)

    for _ in range(length):
        next_word_candidates = markov_chain.get(current_state, None)
        if not next_word_candidates:
            break

        # Choose the next word randomly from the list of candidates
        next_word = random.choice(next_word_candidates)
        output.append(next_word)

        # Update the current state (sliding window)
        current_state = (*current_state[1:], next_word)

    return ' '.join(output)


# Start with the word 'The'
generated_text = generate_text(markov_chain, start_word=('The',), length=30)
print(generated_text)
