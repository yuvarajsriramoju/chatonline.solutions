# scripts/ingest_persona_chat.py

from datasets import load_dataset
import pandas as pd
import os

def load_persona_chat():
    # Load the dataset
    dataset = load_dataset("AlekseyKorshuk/persona-chat", split="train")
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(dataset)
    
    # Display sample data
    print("Sample Data:")
    print(df.head())
    
    # Save to CSV for future use
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/persona_chat.csv", index=False)
    print("Dataset saved to data/persona_chat.csv")

if __name__ == "__main__":
    load_persona_chat()
