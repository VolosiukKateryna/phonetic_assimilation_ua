# ДЛЯ ОГЛУШЕННЯ/ОДЗВІНЧЕННЯ
VOICED_SET = ["б", "д", "ж", "з", "ґ", "г", "дз", "дж"]
VOICELESS_SET = ["т", "к", "ц", "ч", "ф", "с", "ш", "п", "х"]

PHONETIC_PAIRS1 = {'т': 'д', 'п': 'б', 'с': 'з', 'к': 'ґ',
                   'ш': 'ж', 'ч': 'дж', 'ц': 'дз',}
PHONETIC_PAIRS2 = {'б': 'п', 'д': 'т', 'з': 'с', 'ґ': 'к',
                   'ж': 'ш', 'дж': 'ч', 'дз': 'ц'}

EXCEPTIONS = {
    "кігт": "кі[х]т",
    "нігт": "ні[х]т",
    "легк": "ле[х]к",
    "вогк": "во[х]к",
    "дьогт": "дьо[х]т",
    "дігт": "ді[х]т"
}

# ДЛЯ М'ЯКОСТІ
straight_quote = "'"
curly_quote = "’"
SOFTENING_MARKERS = {'я': 'а', 'ю': 'у', 'є': 'е', 'ь': '', 'ї': 'і', 'і': 'і'}
STRAIGHT = ["д", "т", "з", "с", "ц", "л", "дз", "н", "р"]
CURLY = ["б", "п", "в", "м", "ф", "дж", "ш", "х", "ґ", "г", "к"]

def checking_exc(word):
    for old, new in EXCEPTIONS.items():
      word = word.replace(old, new)
    return word


def apply_assimilation(word):
    temp_for_check = word.replace(straight_quote, 'X').replace(curly_quote, 'X')
    if not temp_for_check.isalpha() or not word:
        return "⚠️Будь ласка, введіть одне слово, що містить лише літери та апострофи."
    clean_word = word.strip().lower()
    exc_word = checking_exc(clean_word)
    if exc_word != clean_word:
        return exc_word
    phonetic_word = list(clean_word)

    if len(clean_word)>1:
      first_char = clean_word[0]
      second_char = clean_word[1]

      if first_char in PHONETIC_PAIRS2 and second_char in VOICELESS_SET:
        phonetic_word[0] = f"[{PHONETIC_PAIRS2[first_char]}]"

      if first_char in PHONETIC_PAIRS1 and second_char in VOICED_SET:
        phonetic_word[0] = f"[{PHONETIC_PAIRS1[first_char]}]"

    for i in range(len(clean_word)-1):
      current_char = clean_word[i]
      next_char = clean_word[i+1]

      if current_char in PHONETIC_PAIRS1 and next_char in VOICED_SET:
        phonetic_word[i] = f"[{PHONETIC_PAIRS1[current_char]}]"

      if next_char == "ь" and i + 2 < len(clean_word):
        after_soft = clean_word[i + 2]
        if current_char in PHONETIC_PAIRS1 and after_soft in VOICED_SET:
          phonetic_word[i] = f"[{PHONETIC_PAIRS1[current_char]}]"

    return "".join(phonetic_word)


def check_for_soft_sounds(word2):
  temp_for_check = word2.replace(straight_quote, 'X').replace(curly_quote, 'X')
  if not temp_for_check.isalpha() or not word2:
    return "⚠️Будь ласка, введіть одне слово, що містить лише літери та апострофи."
  clean_word2= word2.strip().lower()
  new_phonetic_word = list(clean_word2)
  for i in range(len(clean_word2)-1):
    current_char = clean_word2[i]
    next_char = clean_word2[i+1]
    
    if current_char in STRAIGHT and next_char in SOFTENING_MARKERS:
      new_phonetic_word[i] = f"{current_char}{straight_quote}"
      new_phonetic_word[i+1] = SOFTENING_MARKERS[next_char]
    
    if current_char in CURLY and next_char in SOFTENING_MARKERS:
      new_phonetic_word[i] = f"{current_char}{curly_quote}"
      new_phonetic_word[i+1] = SOFTENING_MARKERS[next_char]

  return "".join(new_phonetic_word)