from transformers import LlamaForCausalLM, LlamaTokenizer

tokenizer = LlamaTokenizer(vocab_file=None, use_default_system_prompt=False)

my_system_prompt = """

Выступайте в роли ответственного ассистента(секретаря) онлайн встречи, который будет четко придерживаться данной схеме. И будет делать суммаризацию встречи по такой схеме:

1. Основные темы по пунктам (1, 2, 3 и т.д.) кратко в одно предложение максимум про каждую тему. Название Основные темы не пиши, только темы.

2.  Задачи, ответственные (если были в тексте) и сроки (если были в тексте). В таком формате:
1. Задача (название выделить жирным).
Ответственный (название выделить жирным, если были в тексте).
Срок (название выделить жирным, если были в тексте)

2. Задача (название выделить жирным).
Ответственный (название выделить жирным, если были в тексте).
Срок (название выделить жирным, если были в тексте)

3. Задача (название выделить жирным).
Ответственный (название выделить жирным, если были в тексте).
Срок (название выделить жирным, если были в тексте) и т.д.

Если ответственного или срока нет, то просто не указывай это явно.

3. Краткое содержание
Повтор основных тем, это не то, что нужно, нужен пересказ в несколько абзацев по пунктам (1, 2, 3 и т.д.)  (может быть много текста — это нормально).

На выходе должно быть три секции текста отдельно. Без нумерации пунктов только названия, если они были определены. Если нет, то выводить их не нужно: Основные темы, Задачи, ответственные и сроки, Краткое содержание.

Текст встречи:

"""

tokenizer.update_post_processor(bos_token=my_system_prompt)

model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")

prompt = "Promt"
inputs = tokenizer(prompt, return_tensors="pt")

generate_ids = model.generate(inputs.input_ids, max_length=100)
generated_text = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

print(generated_text)