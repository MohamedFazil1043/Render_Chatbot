import google.generativeai as genai


genai.configure(api_key="AIzaSyDY6CBCkviybkF6_xz6TMkxdBZBMGW8zOI") 

# Create the model with the desired configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)


response = model.generate_content([
    "You are now assigned as an agent for a website called MyHalalTrip.com, specializing in holy trips and helping to book tickets to Halal hotels, Halal trips, and avoiding Haram practices completely during the trip. As a chatbot, your role is to inform people about Hajj, Umrah, Islamic principles, and answer Islamic queries. If users ask about non-Islamic or non-Halal content, politely decline to answer by providing a reasonable explanation.",
    "input: What about science and any other questions unrelated to Islamic content or MyHalalTrip?",
    "output: Sorry for the inconvenience. I can only provide information about MyHalalTrip and its services. I'm not programmed to discuss topics outside of this scope.",
    "input: MyHalalTrip",
    "output: ",
])


print(response.text)




# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load environment variables from .env file
# load_dotenv()

# # Retrieve the API key from environment variables
# api_key = os.getenv("GEMINI_API_KEY")

# # Check if the API key is available
# if not api_key:
#     raise ValueError("API key not found. Please set the GEMINI_API_KEY in the .env file.")

# # Configure the Generative AI API client
# genai.configure(api_key=api_key)

# # Create the model with the desired configuration
# generation_config = {
#     "temperature": 0.9,
#     "top_p": 1,
#     "max_output_tokens": 2048,
# }

# model = genai.GenerativeModel(
#     model_name="gemini-1.0-pro",
#     generation_config=generation_config,
# )

# # Define the prompt and generate content
# response = model.generate_content([
#     "You are now assigned as an agent for a website called MyHalalTrip.com, specializing in holy trips and helping to book tickets to Halal hotels, Halal trips, and avoiding Haram practices completely during the trip. As a chatbot, your role is to inform people about Hajj, Umrah, Islamic principles, and answer Islamic queries. If users ask about non-Islamic or non-Halal content, politely decline to answer by providing a reasonable explanation.",
#     "input: What about science and any other questions unrelated to Islamic content or MyHalalTrip?",
#     "output: Sorry for the inconvenience. I can only provide information about MyHalalTrip and its services. I'm not programmed to discuss topics outside of this scope.",
#     "input: MyHalalTrip",
#     "output: ",
# ])

# # Print the generated response
# print(response.text)

