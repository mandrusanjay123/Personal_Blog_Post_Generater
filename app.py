import os
import streamlit as st
import google.generativeai as genai
from apikey import GEMINI_API_KEY, openai_api_key,HUGGING_FACE_API_KEY
# from huggingface_hub import InferenceClient
# client = InferenceClient("black-forest-labs/FLUX.1-dev", token=HUGGING_FACE_API_KEY)



genai.configure(api_key=GEMINI_API_KEY)



st.set_page_config(layout="wide")
 
st.title('🤖✍🏻 BlogCraft: Your AI blog Generation Companion')

st.subheader("Create and craft your Own Blog using GEN AI Companion here ")
blog= "As the publishing world has evolved, and more of it has moved online, blogs have come to occupy a central position in this digital content world. Blogs are a source of knowledge, opinion and concrete advice. While not yet posed to replace journalism as an art form, people increasingly look to trusted blogs to find answers to their questions, or to learn how to do something. "
with st.sidebar:
    st.title("Input Your Blog Details here")
    st.subheader("Enter Details of Blog you want to generate")

    blog_title=st.text_input("Blog Title")

    keywords=st.text_area("Keywords (comma-separated)")

    num_words=st.slider("Number of words", min_value=250, max_value=1000, step=250)

    num_images=st.number_input("Number of Images",min_value=1, max_value=5, step=1)

    submit_button=st.button("Generate Blog")


# output is a PIL.Image object
# image= client.text_to_image("Astronaut riding a horse")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="Generate a comprehensive, engaging blog post based on given title and keywords, make sure the blog is orginal and relvant to the tilte  and keywords which is suitable for online audience and this blog should be approximately of {num_words} length",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Generate a comprehensive, engaging blog post based on  Title : Mars Mission and keywords \"Life, adaptation,4.5 billion years ago,water\", make sure the blog is orginal and relvant to the tilte  and keywords which is suitable for online audience and this blog should be approximately of {500} length",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, here's a blog post designed to be engaging, original, and relevant to the title \"Mars Mission\" and the keywords \"Life, adaptation, 4.5 billion years ago, water\", while aiming for approximately 500 words:\n\n**Title: The Red Planet's Siren Song: Chasing Life's Echoes on Mars**\n\nFor decades, Mars has been more than just a rusty speck in our night sky. It’s been a siren, calling to us with the tantalizing possibility of extraterrestrial life, past or present. Our missions to the Red Planet aren't simply scientific exercises; they’re a deep dive into our own origins, a search for answers to the fundamental question: Are we alone?\n\nThe keywords surrounding this quest - life, adaptation, 4.5 billion years ago, and water - are the threads that weave the intricate narrative of Mars’ potential to harbor life. The story begins, much like our own, approximately 4.5 billion years ago, with the birth of our solar system. At this time, Mars was a dramatically different place. Evidence points to a warmer, wetter world, possibly boasting a thick atmosphere and vast oceans, lakes, and rivers. This is where the ‘water’ keyword becomes crucial. Water, as we know it, is the lifeblood of all organisms on Earth, and the presence of liquid water on early Mars makes it a prime candidate for supporting microbial life.\n\nBut what about ‘life’ itself? We're not expecting to find Martian dinosaurs roaming the canyons. What scientists are primarily searching for are the fossilized remains of microscopic life or, even more exciting, signs of extant microbial life in protected niches. These would likely be single-celled organisms, perhaps similar to extremophiles we find thriving in harsh conditions on Earth. This connects to our ‘adaptation’ keyword. The ability of life to adapt is remarkable, and if life arose on Mars, it would have had to adapt to dramatically changing conditions as the planet cooled and its atmosphere thinned. This very concept of adaptation, the resilience of life, is a key aspect of what makes the Mars mission so captivating.\n\nThe search isn't just about finding a fossil or a microbe; it's about understanding the processes of abiogenesis - how life arose from non-living matter. If we find evidence that life arose independently on Mars, it would suggest that life may not be as rare in the universe as we think. It would fundamentally alter our perspective, indicating that the building blocks of life are widespread and that the emergence of life is a more common occurrence than a lucky coincidence.\n\nCurrent Mars missions, like the Perseverance rover, are designed to collect samples from ancient lakebeds and river deltas. These samples, when brought back to Earth for detailed analysis, could contain the evidence we are seeking. The analysis will focus on identifying bio-signatures – chemical traces that point to past or present life.\n\nThe Mars mission is more than just about rockets and rovers. It's about our yearning to understand our place in the cosmos. It's about the human spirit of exploration, the relentless pursuit of knowledge, and the quiet hope that, perhaps, we'll find we're not alone. Mars, with its ancient history and potential to have harbored life billions of years ago, offers us a chance to unravel one of the universe’s greatest mysteries. And that, perhaps more than anything else, is why we keep looking up at the Red Planet.\n",
      ],
    },
  ]
)

prompt_parts=[f"Generate a comprehensive, engaging blog post based on given title \"{blog_title}\" and the keywords \"{keywords}\", make sure the blog is orginal and relvant to the tilte and keywords which is suitable for online audience and this blog should be approximately of {num_words} length"]



# print(response.text)# print(response.text)


if submit_button:
    response = chat_session.send_message(prompt_parts)
#     image_response = client.images.generate(
#     model="dall-e-3",
#     prompt="a white siamese cat",
#     size="1024x1024",
#     quality="standard",
#     n=1,
# )
    # image_url=image_response.data[0].url
    # st.image(image_url)
    # st.title("Your Blog Post")
    st.write(response.text)
# print(image)


