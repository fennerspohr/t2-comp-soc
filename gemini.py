import os

import google.generativeai as genai


def consultar_gemini(prompt: str) -> str:

    try:

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:

            raise ValueError(

                "Chave da Api nao encontrada. Configure GEMINI_APY_KEY")

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:

        return f"Erro ao consultar Gemini: {e}"


if __name__ == "__main__":

    pergunta = "Liste 5 curiosidades sobre a linguagem Python."

    resposta = consultar_gemini(pergunta)

    print("Resposta do Gemini:\n", resposta)
