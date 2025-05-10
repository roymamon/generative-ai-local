import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-12-01-preview" 
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

def generate_text(prompt, temperature=0.5, max_tokens=4096):
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    filters = {
        "1": "vegetarian",
        "2": "gluten-free",
        "3": "high-protein",
        "4": "low-carb"
    }

    print("Choose a recipe type:")
    for key, value in filters.items():
        print(f"{key}. {value}")

    choice = input("Enter your choice (1-4): ")
    recipe_type = filters.get(choice, "vegetarian")

    ingredients = "carrots, chickpeas, and garlic"
    prompt = f"Generate a {recipe_type} recipe using the following ingredients: {ingredients}."

    generated_text = generate_text(prompt)
    print("\nGenerated Recipe:\n")
    print(generated_text)