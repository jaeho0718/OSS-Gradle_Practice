import gradio as gr

# 폭죽 애니메이션용 confetti CDN 및 JS 코드 포함 HTML
confetti_html = '''
<div id="confetti-container"></div>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<script>
function fireConfetti() {
  confetti({
    particleCount: 120,
    spread: 90,
    origin: { y: 0.7 }
  });
}
window.fireConfetti = fireConfetti;
</script>
'''

def greet(name, enthusiasm, font_size):
    """사용자의 이름, 열정도, 폰트 크기를 받아 응원 문구를 HTML로 반환"""
    message = f"Cheers {name}! {'🔥'*enthusiasm}!"
    return f'<span style="font-size:{font_size}px">{message}</span>'

def on_submit(name, enthusiasm, font_size):
    # 인삿말 생성 + JS로 confetti 실행 트리거
    from gradio import processing
    html = greet(name, enthusiasm, font_size)
    # JS 실행 스크립트 추가
    html += '<script>if(window.fireConfetti){window.fireConfetti();}</script>'
    return html

with gr.Blocks() as demo:
    gr.Markdown("# Simple greetings app\n이름을 입력하고 열정도, 폰트 크기를 선택하면 응원 문구를 생성합니다.")
    with gr.Row():
        name = gr.Textbox(label="이름", value="홍길동")
        enthusiasm = gr.Slider(minimum=1, maximum=5, step=1, label="열정도", value=3)
        font_size = gr.Slider(minimum=16, maximum=48, step=2, label="폰트 크기", value=24)
    output = gr.HTML(label="인삿말")
    confetti = gr.HTML(confetti_html, visible=True, show_label=False)
    btn = gr.Button("응원받기!")
    btn.click(on_submit, inputs=[name, enthusiasm, font_size], outputs=output)

if __name__ == "__main__":
    demo.launch()