prompts = {
    "text_prompt": """
        You are analyzing a wine label image. Your task is twofold:

        1. **Extract all readable text from this wine label exactly as it appears.**

        ### Text Extraction Rules:
        - Preserve capitalization, spacing, and formatting exactly as seen.
        - Do not infer, translate, or guess missing text—only extract what is clearly visible.
        - If text is partially cut off, return it as-is without completion.
        - For stylized or cursive fonts, extract characters as best as possible—even approximated characters are better than skipping.
        - Do not merge or "correct" fragmented words.
        - Maintain the vertical and visual order of lines on the label.
        - Ignore decorative, non-informative elements (swirls, flourishes, etc.).
        - Return only raw extracted text in plain format.

        ---

        2. **Structure the extracted text in the following format:**

        Vintage:  
        Producer Name:  
        Fanciful Name / Vineyard Name (if present):  
        Appellation:  
        Grape Variety (if can be inferred):  
        Size (if present, e.g., in ML):  
        Additional Designations (Grand Cru, 1er Cru, Vieilles Vignes, etc.):

        ### Structuring Rules:
        - Do not fabricate, infer, or complete missing details.
        - Categorize only what is clearly visible.
        - Infer a field (e.g., Grape or Appellation) **only when logically certain** and based on known conventions (e.g., Châteauneuf-du-Pape = GSM blend).
        - If a field cannot be confidently filled, leave it blank.
        - No extra explanation—return only the structured data.
""",

    "format_prompt": """
        Format the following wine data using this exact structure:

        **Vintage, Producer Name, (Fanciful Name, Vineyard Name), Appellation, (Grape), (Size)**

        ### Formatting Rules:
        - Output a single clean line, comma-separated. Do not include field labels.
        - If a field is missing, skip it—do not include placeholders.
        - Do not guess or fabricate values.
        - Apply consistent, proper capitalization (e.g., "DOMAINE LEFLAIVE" → "Domaine Leflaive").
        - Use double quotes around Lieu-Dit or Cru names (e.g., "Les Folatières").
        - Add designation suffixes (e.g., Grand Cru, Premier Cru, Vieilles Vignes, Monopole) as per French wine law.
        - Champagne: Include dosage (e.g., Extra Brut) and style (e.g., Blanc de Noirs), with “Champagne” as suffix.
        - New World: Always place appellation before grape (e.g., "Mendoza Malbec").
        - Bordeaux: Include "Grand Cru Classe" after appellation for classified growths.
        - Rhone: Spell out "Chateauneuf du Pape Rouge/Blanc" (no hyphens).
        - Italy: Place cru names in quotes before the appellation (e.g., "Colle Vota" Montepulciano d'Abruzzo).
        - Clean sizes (e.g., "e500ml" → "500ml").
        - Return only the formatted string—no extra commentary or explanation.

"""

}