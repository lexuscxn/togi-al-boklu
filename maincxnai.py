from google import genai

client = genai.Client(api_key="AQ.Ab8RN6L8qoleFnzM6AFSrdmTchxHTOovQb1JAf_qZvPCKMhg6A")

while True:
    quuestion = input("Siz: ")
    if quuestion.lower () == "exit":
        break
    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = quuestion
    )
    print("Gemini: ",response.text)