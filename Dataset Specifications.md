## Dataset Specifications
* **Primary Source Text:** *Sanskrit Vachanamala 1*, Sanskrit Bhasha Sanstha, Mumbai.
* **Surface Words Extracted:** 1,027 tokens.
* **Mapped Unique Types:** 150 high-frequency lemmas.
* **Full Benchmark Parallel Corpus:** 50,234 tokens.

## Quick Start
To test word conversion across schemes:
```bash
python convert_tagsets.py --word "सूर्यकोटिसमप्रभ" --tgt "tsl_tag"
# Output: [Conversion] Word: 'सूर्यकोटिसमप्रभ' | Target (tsl_tag): adj-m-s-8