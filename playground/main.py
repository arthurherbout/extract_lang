import langextract as lx

def main():
    print("Hello from playground!")
    
    result = lx.extract(
        text_or_documents=input_text,
        prompt_description=prompt,
        examples=examples,
        model_id="gemma2:2b",  # Automatically selects Ollama provider
        model_url="http://localhost:11434",
        fence_output=False,
        use_schema_constraints=False
    )
    print(result)


if __name__ == "__main__":
    main()
