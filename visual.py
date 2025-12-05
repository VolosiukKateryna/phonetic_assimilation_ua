import gradio as gr
from modulephon import apply_assimilation, check_for_soft_sounds 

with gr.Blocks() as interface:
    gr.HTML("<h1 style='color: #8A2BE2;'>Перші етапи створення фонетичної транскрипції</h1>")
    gr.HTML("<h2 style='color: #BA55D3;'>Впиши слово (може бути фонетичне: прийменник + іменник) → <br>а ми вкажемо на оглушення/одзвінчення або на м'якість/напівпом'якшення!</h2>")

    with gr.Row():
        assimilation_input = gr.Textbox(
            label="Слово для перевірки оглушення/одзвінчення",
            placeholder='Наприклад: "просьба", "зцукром"'
        )
        soft_input = gr.Textbox(
            label="Слово для перевірки м'якості/напівпом'якшення (заберіть, будь ласка, [])",
            placeholder='Наприклад: "кінь", "безвіри"'
        )

    with gr.Row():
        assimilation_output = gr.Textbox(
            label="Результат першої обробки",
            lines=2,
            placeholder='В [] буде звук, який змінився',
            interactive=False
        )
        soft_output = gr.Textbox(
            label="Результат другої обробки",
            lines=2,
            placeholder='...',
            interactive=False
        )

    with gr.Row():
        assimilation_button = gr.Button("ОГЛУШЕННЯ / ОДЗВІНЧЕННЯ")
        soft_hard_button = gr.Button("М'ЯКІСТЬ / НАПІВПОМ'ЯКШЕННЯ")

        assimilation_button.click(
            fn=apply_assimilation,
            inputs=assimilation_input,
            outputs=assimilation_output
        )

        soft_hard_button.click(
            fn=check_for_soft_sounds,
            inputs=soft_input,
            outputs=soft_output
        )

if __name__ == "__main__":
    interface.launch()