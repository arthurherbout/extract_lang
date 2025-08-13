import langextract as lx
import textwrap

def main():
    print("Hello from playground!")

    prompt = textwrap.dedent("""\
    Extract characters, emotions, and relationships in order of appearance.
    Use exact text for extractions. Do not paraphrase or overlap entities.
    Provide meaningful attributes for each entity to add context.""")

    examples = [
    lx.data.ExampleData(
        text="ROMEO. But soft! What light through yonder window breaks? It is the east, and Juliet is the sun.",
        extractions=[
            lx.data.Extraction(
                extraction_class="character",
                extraction_text="ROMEO",
                attributes={"emotional_state": "wonder"}
            ),
            lx.data.Extraction(
                extraction_class="emotion",
                extraction_text="But soft!",
                attributes={"feeling": "gentle awe"}
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="Juliet is the sun",
                attributes={"type": "metaphor"}
            ),
        ]
    )
    ]

    input_text = "Lady Juliet gazed longingly at the stars, her heart aching for Romeo"

    result = lx.extract(
        text_or_documents=input_text,
        prompt_description=prompt,
        examples=examples,
        model_id="mistral:latest",  # Automatically selects Ollama provider
        model_url="http://localhost:11434",
        fence_output=False,
        extraction_passes=3,
        max_workers=20,
        use_schema_constraints=False
    )

    lx.io.save_annotated_documents([result], output_name="extraction_results.jsonl", output_dir=".")
    
    html_content = lx.visualize("extraction_results.jsonl")
    with open("visualization.html", "w") as f:
        f.write(html_content)


if __name__ == "__main__":
    main()
