import openai

# Установите ваш ключ API OpenAI
openai.api_key = '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'


def summarize_text(input_file, output_file):
    # Чтение текста из входного файла
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Запрос на генерацию короткой версии текста с помощью GPT-3
    response = openai.Completion.create(
        engine="davinci",  # Можно выбрать другой движок, если требуется
        prompt=input_text,
        max_tokens=150,  # Можно настроить максимальное количество токенов в ответе
        temperature=0.7,  # Можно настроить температуру для разнообразия ответов
        stop="\n"
    )

    # Получение суммаризованного текста из ответа
    summarized_text = response.choices[0].text.strip()

    # Запись суммаризованного текста в выходной файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(summarized_text)


# Пример использования
input_file = 'input.txt'
output_file = 'output.txt'
summarize_text(input_file, output_file)
print(f"Суммаризованный текст сохранен в файл '{output_file}'")
