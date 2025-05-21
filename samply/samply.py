import reflex as rx
from components.markdown import markdown

# 示例 Markdown 文本
sample_markdown = """
# 标题

这是一段 **粗体文本** 和 *斜体文本*。

## 列表示例
- 项目 1
- 项目 2
- 项目 3

## 代码示例
```python
def hello_world():
    print("Hello, world!")
"""

class State(rx.State):
    pass    

def index():
    return rx.box(
        rx.heading("Markdown 示例 测试", size="1"),
        rx.divider(),
        markdown(
            content=sample_markdown,
            class_name="markdown-content"
        ),
        padding="2em",
        max_width="800px",
        margin="0 auto",
    )

app = rx.App()
app.add_page(index, route="/")
