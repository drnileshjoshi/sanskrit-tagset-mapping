import pandas as pd
import argparse

def load_mappings(csv_path="mapping_words.csv"):
    df = pd.read_csv(csv_path)
    return df

def convert_word(word_surface, src_scheme, tgt_scheme, df_mappings):
    match = df_mappings[df_mappings['word_surface'] == word_surface]
    if not match.empty:
        return match.iloc[0][tgt_scheme]
    else:
        return "UNK"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sanskrit Multi-Tagset POS Converter")
    parser.add_argument("--word", type=str, required=True, help="Sanskrit word token")
    parser.add_argument("--src", type=str, default="word_surface", choices=["word_surface", "il_post", "bis", "ud_upos", "tsl_tag"])
    parser.add_argument("--tgt", type=str, required=True, choices=["il_post", "bis", "ud_upos", "ud_features", "tsl_tag"])
    
    args = parser.parse_args()
    df = load_mappings()
    
    result = convert_word(args.word, args.src, args.tgt, df)
    print(f"[Conversion] Word: '{args.word}' | Target ({args.tgt}): {result}")